
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from account.tools.tokens import account_activation_token

User=get_user_model()
def send_confirmation_mail(user_id,site_address):
    user=User.objects.filter(id=user_id).first()
    from_email = settings.EMAIL_HOST_USER
    # mail kime gedir
    recipient=user.email
    subject='Account tesdiq edin'
    context={
        'user':user,
        'site_address':site_address,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
      
    }
# html file
    body=render_to_string('emails/email.html',context)
    mail=EmailMessage(subject, to=[recipient,], from_email=from_email, body=body )
    # emaile gedecek forma
    mail.content_subtype='html'
    # sayt erorlarini susdurmaq
    mail.send(fail_silently=True)


    # render to string - emaile geden html sehifeni stringe cevir