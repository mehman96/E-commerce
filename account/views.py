from django.shortcuts import render,redirect
from .forms import RegisterterForm,LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from account.tools.tokens import account_activation_token
from account.tasks import send_confirmation_mail
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import get_user_model,authenticate,login as django_login,logout as django_logout
User = get_user_model()



def register (request):
    form=RegisterterForm()
    if request.method=="POST":
        form=RegisterterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password=form.cleaned_data["password1"]
            user.is_active=False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_confirmation_mail(user_id=user.id, site_address=site_address)
            messages.success(request,'Siz ugurla qeydiyyatdan kecdiz :)')
            return redirect(reverse_lazy('home:index'))
    context ={
        'form': form
    }

    return render(request, 'register.html',context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('home:index'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('account:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('account:register'))

def login(request):
    form = LoginForm()
    if request.method =='POST':
        # foruma gelen data requset metod olur
        form=LoginForm(data=request.POST)
        if form.is_valid():
            # html  icerisindeki data
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            authenticate(username=email, password=password)
            user=authenticate(username=email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'Siz  login oldunuz')
                return redirect(reverse_lazy('home:index'))
                
            else:
                messages.success(request, 'Siz login ola bilmediniz')

    context ={
        'form':form
    }

    return render(request, 'login.html', context )

# login olub olmadigini sessionla yozlayacaq
@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('account:login'))

    # login olanda session id verir onda backende hashlenir ve yoxluyur ki bu sehifeye bizim icazemiz varsa session id genarete edir
    # commit false - biz orda password yoxlayariq ona gore  yazdigimiz kodu 
    # database yazmasin deye yaziriq
    # valid- password ucun yazdifgimiz validation
    # save- database de saxlanilmasi ucun 
    # reverse_lazy - redirect de /  ile yazilir name namaspace den istidafe etmek olmur
    # ama burda url yazmaq yerine name ve namaspace ile istiqamet vere bilrik
    # is activate - tehlukesizlik baximindan ve etibarli musteri oldugunu bildirmek ucun activ musterileirn siyahisina
    # dusmek ucun hansiki hemin sayt ozu bize email gonderir . onu activ etmek ucundur
    # emaile link gelir ona tiklamaqla tesdiq edirik.
    # uthenticate - user email ve parol goturub yoxluyur(database le elaqelendirir)