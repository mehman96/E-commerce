
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
      
    path('jet/', include('jet.urls', 'jet')),  
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
   


    # path('checkout/', include('order.urls', namespace="checkout")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns += i18n_patterns(
    
    path('about/',include("about.urls",namespace="about"),),
    path('',include("product.urls",namespace="product"),),
    path('',include("shop.urls",namespace="shop"),),
    path('blog/',include("blog.urls",namespace="blog"),),
    path('',include("home.urls",namespace="home"),),
    path('contact/',include("contact.urls",namespace="email"),),
    path('contact/',include("contact.urls",namespace="thanks"),),
    path('account/',include("account.urls",namespace="register"),),
    path('account/',include("account.urls",namespace="login"),),
    path('contact/', include('contact.urls', namespace="feedback")),
    path('social-auth/', include('social_django.urls', namespace="social")),


    # path('orders/', include('orders.urls', namespace='orders')),
    
)