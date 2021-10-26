from django import forms
from django.contrib.auth.models import User
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["author"] # Author will be set by the code to logged in user

class UserLoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')


class UserRegisterForm(forms.ModelForm):    
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        print('in clean...password: ', password, 'confirm password: ', confirm_password)

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password do not match"
            )
