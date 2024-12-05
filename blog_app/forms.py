from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class contactform(forms.Form):
	name = forms.CharField(label="Name",max_length=100)
	email = forms.EmailField(label="email",max_length=100)
	message = forms.CharField(label="message",max_length=300)
	
class registerform(forms.ModelForm):
	username = forms.CharField(label="username",max_length=100,required=True)
	email = forms.CharField(label="email",max_length=100,required=True)
	password = forms.CharField(label="password",max_length=100,required=True)
	confirm_password = forms.CharField(label="confirm password",max_length=100,required=True)
	
	
	class Meta:
		model = User
		fields = ['username','email','password']
		
		
	def clean(self):  #custom validation
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		
		if password and confirm_password and password!=confirm_password:
			raise forms.ValidationError("Password do not match try again")
		
		
class loginform(forms.Form):
	username = forms.CharField(label="username",max_length=100,required=True)
	password = forms.CharField(label="password", max_length=100, required=True)
	
	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get("username")
		password = cleaned_data.get("password")
		
		if username and password:
			user = authenticate(username=username,password=password)
			
			if user is None:
				raise forms.ValidationError("username and password do not match")
			

class forgotpasswordform(forms.Form):
	email = forms.EmailField(label='email',max_length=254,required=True)
	
	def clean(self):
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		
		if not User.objects.filter(email=email).exists():
			raise forms.ValidationError("No user registered this email")