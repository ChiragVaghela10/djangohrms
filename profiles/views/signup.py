from django.conf import settings
from django.shortcuts import render, redirect, resolve_url
from django.views import View
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from django.contrib.auth.models import User

from ..forms import SignupForm, UserProfileForm  # , SigninForm
from ..models import UserProfile
from formtools.wizard.views import SessionWizardView

class MyLoginView(View):
    template_name = 'profiles:two_factor:login'
    
    def get(self, request, *args, **kwargs):
        return redirect('profiles:two_factor:login')

#class SignupView(View):     #SessionWizard
#    form_class = SignupForm
#    template_name = 'profiles/account.html'
#    redirect_url = 'profiles:success'
#    
#    def get(self, request, *args, **kwargs):
#        form = self.form_class()
#        return render(request, self.template_name, {'form': form})
#    
#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            reg_user = form.save(commit=False)   #reg_user is 'User' instance and 'form' is SignupForm instance
#            reg_user.set_password(reg_user.password)
#            reg_user.is_active = False
#            send_email(reg_user.email,reg_user.id)
#            reg_user.save()            
#            #creating corresponding user profile
#            userprofile = UserProfile(user=reg_user)
#            userprofile.save()
#            #Sending user mail and ID to 'send_email' function below
#            return redirect(self.redirect_url)
#            
#        return render(request, self.template_name, {'form': form})



class SignupWizard(SessionWizardView):
    #template_name = 'profiles/signup_form.html'
    redirect_url = 'profiles:success'
    form_list = (
        ('account', SignupForm),
        ('profile', UserProfileForm),
    )
    template_list = {
        'account':'profiles/account.html',
        'profile':'profiles/personal.html'
    }
    
    def get_template_names(self):
        return self.template_list[self.steps.current]
    
    def get_context_data(self, form, **kwargs):
        """
        NamedUrlWizardView provides the url_name of this wizard in the context
        dict `wizard`.
        """
        context = super(SignupWizard, self).get_context_data(form=form, **kwargs)
        context['cancel_url'] = resolve_url(settings.LOGIN_URL)
        return context
    
    def done(self, form_list, form_dict, **kwargs):
        for form_key in form_dict.keys():
            form = form_dict.get(form_key)
            if form_key == 'account':
                self.request.user = form.save(commit=False)   #reg_user is 'User' instance and 'form' is SignupForm instance
                reg_user = self.request.user
                reg_user.set_password(reg_user.password)
                reg_user.is_active = False
                reg_user.save()
                send_email(reg_user.email,reg_user.id)            
                #creating corresponding user profile
                userprofile = UserProfile(user=reg_user)
                userprofile.save()
            elif form_key == 'profile':
                userprofile = form.save(commit=False)
                userprofile.user = self.request.user
                userprofile.save()
            else:
                form.save()
        return redirect(self.redirect_url)


def send_email(toaddr, toid):
    msg = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://127.0.0.1:8000/profiles/activation/?id="
    text = msg + str(toid)
    subject = "Profiles App:Activation"
    email = EmailMessage(subject, text, to=[toaddr])  # to=['chiragvaghela10@ymail.com']
    email.send()


class LogoutView(View):
    template_name = 'registration/logged_out.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name, {})


class HomeView(View):
    template_name = 'profiles/profile/home.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        return render(request, self.template_name, {'user': current_user})


class SuccessView(View):
    template_name = 'profiles/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ActivateView(View):
    tmeplate_name = 'profiles/activation.html'

    def get(self, request, *args, **kwargs):
        user_id = int(request.GET.get('id'))
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        return render(request, 'profiles/activation.html')
        

################################## Old Implementation ###################
# def login_view(request):
#    return redirect('profiles:two_factor:login')  #redirect it to default login page

# def signup(request):
#    if request.method == "POST":
#        form = SignupForm(request.POST)
#        if form.is_valid():
#            reg_user = form.save(commit=False)
#            reg_user.set_password(reg_user.password)
#            reg_user.is_active = False
#            reg_user.save()            
#            #creating corresponding user profile
#            userprofile = UserProfile(user=reg_user)
#            userprofile.save()
#            #Sending user mail and ID to 'send_email' function below
#            send_email(reg_user.email,reg_user.id)
#            return redirect('profiles:success')
#    else:
#        form = SignupForm()   
#    return render(request, 'profiles/signup.html', {'form':form})

# @login_required(login_url='/profiles/login/')    #when somebody directly try to access homepage redirect to login
# def home(request):
#    current_user = request.user
#    return render(request,'profiles/profile/home.html',{'user':current_user})

# def success(request):
#    return render(request,'profiles/success.html',{})

# def activate(request):
#    id=int(request.GET.get('id'))
#    user = User.objects.get(id=id)
#    user.is_active=True
#    user.save()
#    return render(request,'profiles/activation.html')

############################ Old Implementation Ends #######################