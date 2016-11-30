from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from ..forms import UserProfileForm, UserAccountForm  # , SigninForm
from ..models import UserProfile

class AccountDetailsView(DetailView):
    template_name = 'profiles/profile/account_details.html'
    model = User  # It is equivalent to queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AccountDetailsView, self).get_context_data(**kwargs)
        context['useraccount'] = get_object_or_404(User, pk=self.kwargs['pk'])
        return context


class AccountDetailsEditView(FormView):
    template_name = 'profiles/profile/account_details_edit.html'
    form_class = UserAccountForm
    success_url = 'profiles:account_details'

    def get(self, request, *args, **kwargs):
        loggedInUser = get_object_or_404(User, pk=self.kwargs['pk'])
        form = self.form_class(instance=loggedInUser)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        loggedInUser = get_object_or_404(User, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=loggedInUser)
        if form.is_valid():
            loggedInUser = form.save(commit=False)
            loggedInUser.save()
            return redirect(self.success_url, pk=loggedInUser.pk)

        return render(request, self.template_name, {'form': form})


class PersonalDetailsView(DetailView):
    template_name = 'profiles/profile/personal_details.html'
    model = UserProfile  # It is equivalent to queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PersonalDetailsView, self).get_context_data(**kwargs)
        context['userprofile'] = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return context


class PersoanlDetailsEditView(FormView):
    template_name = 'profiles/profile/personal_details_edit.html'
    form_class = UserProfileForm
    success_url = 'profiles:personal_details'

    def get(self, request, *args, **kwargs):
        loggedInUserProfile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        form = self.form_class(instance=loggedInUserProfile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        loggedInUserProfile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=loggedInUserProfile)
        if form.is_valid():
            loggedInUserProfile = form.save(commit=False)
            loggedInUserProfile.save()
            return redirect(self.success_url, pk=loggedInUserProfile.pk)

        return render(request, self.template_name, {'form': form})

def job_details(request, pk):
    loggedInUser = get_object_or_404(User, pk=pk)
    return render(request, 'profiles/profile/job_details.html', {'user':loggedInUser})




    ################################## Old Implementation ####################################

    # @login_required(login_url='/profiles/login/')    #when somebody directly try to access homepage redirect to login
    # def account_details(request,pk):
    #    loggedInUser = get_object_or_404(User, pk=pk)
    #    return render(request,'profiles/profile/account_details.html',{'useraccount':loggedInUser})   #,'userprofile':loggedInUserProfile})

    # @login_required(login_url='/profiles/login/')    #when somebody directly try to access homepage redirect to login
    # def account_details_edit(request,pk):
    #    loggedInUser = get_object_or_404(User, pk=pk)
    #    if request.method == "POST":
    #        #uform = UserProfileFormA(request.POST, instance=loggedInUserProfile.user)
    #        form = UserAccountForm(request.POST, instance=loggedInUser)
    #        if form.is_valid():# and uform.is_valid():
    #            #loggedInUser = uform.save(commit=False)
    #            #loggedInUser.save()
    #            loggedInUser = form.save(commit=False)
    #            loggedInUser.save()
    #            return redirect('profiles:account_details', pk=loggedInUser.pk)
    #        else:
    #            return render(request,'profiles/profile/account_details_edit.html',{'form':form})#,'uform':uform})
    #    else:
    #        #uform = UserProfileFormA(request.POST, instance=loggedInUser)
    #        form = UserAccountForm(instance=loggedInUser)
    #    return render(request,'profiles/profile/account_details_edit.html',{'form':form})#,'uform':uform})

    # @login_required(login_url='/profiles/login/')    #when somebody directly try to access homepage redirect to login
    # def personal_details(request,pk):
    #    loggedInUser = get_object_or_404(User, pk=pk)
    #    loggedInUserProfile = get_object_or_404(UserProfile, user=loggedInUser)
    #    return render(request,'profiles/profile/personal_details.html',{'userprofile':loggedInUserProfile})   #,'userprofile':loggedInUserProfile})

    # def personal_details_edit(request,pk):
    #    loggedInUser = get_object_or_404(User, pk=pk)
    #    loggedInUserProfile = get_object_or_404(UserProfile, user=loggedInUser)
    #    if request.method == "POST":
    #        #uform = UserProfileFormA(request.POST, instance=loggedInUserProfile.user)
    #        pform = UserProfileFormB(request.POST, instance=loggedInUserProfile)
    #        if pform.is_valid():# and uform.is_valid():
    #            #loggedInUser = uform.save(commit=False)
    #            #loggedInUser.save()
    #            loggedInUserProfile = pform.save(commit=False)
    #            loggedInUserProfile.save()
    #            return redirect('profiles:personal_details', pk=loggedInUserProfile.user.pk)
    #        else:
    #            return render(request,'profiles/profile/personal_details_edit.html',{'form':pform})#redirect('home')
    #    else:
    #        #uform = UserProfileFormA(request.POST, instance=loggedInUser)
    #        pform = UserProfileFormB(instance=loggedInUserProfile)
    #    return render(request,'profiles/profile/personal_details_edit.html',{'form':pform})#,'uform':uform})

    ################################ Reference Material #########################################
    # def signin(request):
    #    usrname = request.POST.get('username')
    #    passwrd = request.POST.get('password')
    #    user = authenticate(username=usrname, password=passwrd)
    #    if user is not None:
    #        login(request, user)
    #        return redirect('home')
    #    else:
    #        form = SigninForm()
    #    return render(request,'profiles/signin.html',{'form':form})
