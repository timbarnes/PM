from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from registration.views import RegistrationView
from users.forms import RegistrationForm, ProfileForm, UserDataForm
from users.models import Profile
# Create your views here.


class MenuMixin(object):
    """Gets public articles, subjects and categories. All tags are public.
    """

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        """
        context['article_list'] = Article.objects.filter(public=True)
        context['subject_list'] = Subject.objects.filter(public=True)
        context['category_list'] = Category.objects.filter(public=True)
        context['tag_list'] = Tag.objects.all()
        """
        return context


class HomeView(MenuMixin, generic.TemplateView):
    """Home page for the Educate project.
    """
    template_name = 'users/home.html'


class UserRegistrationView(RegistrationView):
    """
    Customized registration includes creation of the empty profile.
    """
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    disallowed_url = reverse_lazy('home')

    def register(self, request, **cleaned_data):
        """Custom registration view.
        """
        print('Starting registration')
        print(cleaned_data)
        u = User.objects.create_user(
            cleaned_data['username'],
            '',
            cleaned_data['password1'])
        p = Profile()
        p.user = u
        p.save()
        messages.success(self.request,
                         'Thank you for registering. Now you can login.')


class ProfileView(generic.TemplateView):
    """View/edit profile data
    """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate',
            args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy(
            'profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(
                Profile, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
        })
        return context


class UpdateProfileView(generic.edit.UpdateView):
    """Save updated profile data. Called only with POST.
    """
    model = Profile
    fields = ['picture', 'home', 'interests', 'objectives']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate', args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy(
            'profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(
                Profile, user__username=self.request.user.username),
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
    model = User
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserDataView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=self.request.user)
        profile = get_object_or_404(Profile, user=self.request.user)
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy(
            'userdataUpdate', args=[self.request.user.pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate',
                                                       args=[profile.pk])
        context.update({
            'profile':
            get_object_or_404(Profile,
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
        context.update({
            'profile': get_object_or_404(Profile, user=self.request.user),
        })
        print(context)
        return context
