from django.conf.urls import url
from .views import Register_user, Login_view
from django.views.generic import TemplateView, RedirectView

urlpatterns = [

    url(r'^$', Login_view.as_view(), name="login_url"),
    url(r'^register$', Register_user.as_view(), name="register"),

]
