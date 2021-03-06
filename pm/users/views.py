from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from users.forms import RegistrationForm, ProfileForm, UserDataForm
from users.models import Account
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

# Create your views here.


class HomeView(generic.TemplateView):
    """Home page for the Educate project.
    """
    template_name = 'users/home.html'


class UserRegistrationView(generic.FormView):
    """
    Customized registration includes creation of the empty profile.
    """
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    disallowed_url = reverse_lazy('home')
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        """Custom registration view.
        """
        print('Starting registration')
        print(form.cleaned_data)
        u = Account.objects.create_user(
            form.cleaned_data['username'],
            '',
            form.cleaned_data['password1'])
        u.save()
        messages.success(self.request,
                         'Thank you for registering. Now you can log in.')
        return super().form_valid(form)


class ProfileView(generic.TemplateView):
    """View/edit profile data
    """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        acct = user.account
        user_form = UserDataForm(instance=user)
        profile_form = ProfileForm(instance=acct)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate',
            args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy(
            'profileUpdate', args=[acct.pk])
        context.update({
            'profile': get_object_or_404(Account, user=self.request.user),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        return context


class UpdateProfileView(generic.edit.UpdateView):
    """Save updated profile data. Called only with POST.
    """
    model = Account
    fields = ['picture', 'home', 'interests', 'objectives']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(UserWarning, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate', args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy(
            'profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(
                Account, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        return context

    def form_valid(self, form):
        self.kwargs['form_data'] = form.cleaned_data
        messages.success(self.request, 'Profile successfully updated')
        return super(UpdateProfileView, self).form_valid(form)


class UpdateUserDataView(generic.edit.UpdateView):
    """Save updated user data. Called only with POST.
    """
    model = Account
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserDataView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Account, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate', args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate',
                                                       args=[profile.pk])
        context.update({
            'profile':
            get_object_or_404(Account,
                              user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        print('UpdateUserDataView: ', context)
        return context

    def form_invalid(self, form):
        print("form invalid", form)
        messages.error(self.request, 'User data not successfully updated.')
        return super(UpdateUserDataView, self).form_invalid(form)

    def form_valid(self, form):
        print("Form submitted: ", form)
        self.kwargs['form_data'] = form.cleaned_data
        messages.success(self.request, 'User data successfully updated')
        return super(UpdateUserDataView, self).form_valid(form)


class MyHomeView(generic.TemplateView):
    """Home page for each user.
    """
    template_name = 'users/myhome.html'

    def get_context_data(self, **kwargs):
        print('MYHOME')
        context = super(MyHomeView, self).get_context_data(**kwargs)
        print("user is: %s" % self.request.user)
        context.update({
            'profile': get_object_or_404(Account, user=self.request.user),
        })
        print(context)
        return context
