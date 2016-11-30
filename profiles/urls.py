from django.conf.urls import include, url
#from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
app_name='profiles'
urlpatterns = [
    #url('^', include('django.contrib.auth.urls')), #refer this:https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views
    url(r'', include('two_factor.urls', namespace='two_factor')), #two-factor urls
    url(r'^$',views.MyLoginView.as_view(), name='login_page'),  #empty link will be redirected to login page
    url(r'^signup/$',views.SignupWizard.as_view(), name='signup'),
    url(r'^success/$',views.SuccessView.as_view(),name='success'),
    url(r'^activation/',views.ActivateView.as_view(), name='activation'),
    url(r'^home/$',login_required(views.HomeView.as_view()),name='home'),
    url(r'^logout/$',views.LogoutView.as_view(),name='logout'),
    url(r'^profile/account/(?P<pk>\d+)/$', login_required(views.AccountDetailsView.as_view()), name='account_details'),
    url(r'^profile/account/(?P<pk>\d+)/edit$', login_required(views.AccountDetailsEditView.as_view()), name='account_details_edit'),
    url(r'^profile/personal/(?P<pk>\d+)/$', login_required(views.PersonalDetailsView.as_view()), name='personal_details'),
    url(r'^profile/personal/(?P<pk>\d+)/edit$', login_required(views.PersoanlDetailsEditView.as_view()), name='personal_details_edit'),
    url(r'^profile/job/(?P<pk>\d+)/$', views.job_details, name='job_details'),
]