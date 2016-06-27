from django import forms
from django.contrib.auth.models import User
#from main.validators import validate_email_unique


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
   # email = forms.CharField(required=True, validators=[validate_email_unique])

    def clean(self):
        '''
        Overridds the clean method
        '''
        cleaned_data = super(SignupForm, self).clean()
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')
