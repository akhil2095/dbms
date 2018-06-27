from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

YEARS= [x for x in range(1960,2015)]
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	birth_date = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=YEARS))
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	department = forms.CharField(max_length=100)
	
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'phone',
			'department',
			'birth_date',
			'password1',
			'password2')

		def save(self,commit=True):
			user = super(RegistrationForm, self).save(commit=False)
			user.first_name=self.cleaned_data['first_name']
			user.last_name=self.cleaned_data['last_name']
			user.email=self.cleaned_data['email']
			user.phone=self.cleaned_data['phone']
			user.birth_date=self.cleaned_data['birth_date']
			user.department=self.cleaned_data['department']
			
			if commit:
				user.save()

			return user

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'email',
			'password'
			)