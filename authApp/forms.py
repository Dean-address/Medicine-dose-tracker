from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

class SignupForm(forms.Form):
    first_name = forms.CharField(label='FirstName', required=True)
    last_name = forms.CharField(label='LastName', required=True)
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(max_length=32,required=True, widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'border p-8'
        self.helper.layout = Layout(
              Div(
             'email',
             'password',
        ),
          
            
            Submit('submit', 'Submit', css_class='mt-4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"'),
        )
    
    
