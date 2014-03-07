from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
# from lunarshiftapp.models import A

class UserCreateForm(UserCreationForm):
	"""docstring for UserCreateForm"""
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
	fname = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
	lname = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
	password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

	def is_Valid(self):
		form = super(UserCreateForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form

	class Meta:
		fields = ['email', 'fname', 'lname', 'password1', 'password2']
		model = User

class AuthenticateForm(AuthenticationForm):
	email = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'email'}))
	password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

	def is_valid(self):
		form = super(AuthenticateForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form
