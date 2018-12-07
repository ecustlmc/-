from django import forms
class UserForm(forms.Form):
    u_id = forms.CharField(required=True,)
    u_pd = forms.CharField(widget=forms.PasswordInput,required=True)
    u_email = forms.EmailField(required = True)
    pd = forms.CharField(widget=forms.PasswordInput,required=True)

class AddStudent(forms.Form):
    s_id = forms.CharField(required=True)
    s_name = forms.CharField(required=True)
    u_id = forms.CharField(required=True)
    jwc_pwd = forms.CharField(widget=forms.PasswordInput,required=True)
    pd = forms.CharField(widget=forms.PasswordInput,required=True)
