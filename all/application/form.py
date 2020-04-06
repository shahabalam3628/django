from django  import forms
import pdb
#from .models import Company,Organization,Post
from .models import *


# create Form without using model

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)




class RegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields =['username','useremail','userpass']
        widgets=  {
                       'username': forms.TextInput(attrs={'class':'form-control','name':'username','id':'username','placeholder':'Enter Name'}),
                       'useremail': forms.TextInput(attrs={'class': 'form-control','name':'useremail', 'id':'useremail'}),
                       'userpass': forms.PasswordInput(attrs={'class': 'form-control','name':'userpass', 'id':'userpass'}),
                        
                           
                  }




class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['per_name','father_name','gender','mobile','per_address','per_pincode','per_photo','per_status']
        widgets=  {
                       'per_name': forms.TextInput(attrs={'class':'form-control','name':'per_name','id':'per_name','placeholder':'Enter Name'}),
                       'father_name': forms.TextInput(attrs={'class': 'form-control','name':'father_name', 'id':'father_name'}),
                       'gender': forms.Select(attrs={'class': 'form-control','name':'gender', 'id':'gender'}),
                       'mobile': forms.TextInput(attrs={'class': 'form-control','name':'mobile', 'id':'mobile'}),
                       'per_address': forms.Textarea(attrs={'class': 'form-control','name':'per_address', 'id':'per_address'}),
                       'per_pincode': forms.TextInput(attrs={'class': 'form-control','name':'per_pincode', 'id':'per_pincode'}),
                       'per_photo': forms.FileInput(attrs={'class': 'form-control','name':'per_photo', 'id':'per_photo'}),
                       'per_status': forms.HiddenInput(attrs={'class': 'form-control','name':'per_status', 'id':'per_status'}),
                        
                           
                  }
        labels    = {
                      'per_name': 'Name',
                      'father_name': 'Father Name',
                      'gender': 'Gender',
                      'mobile':'Mobile',
                      'per_address':'Address',
                      'per_pincode':'Pin Code',
                      'per_photo' : 'Upload Image',
                      


                    }          

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        widgets =   {
                        'title': forms.TextInput(attrs={'class':'form-control','name':'title','id':'title','placeholder':'Enter Title'}),
                        'description': forms.Textarea(attrs={'class': 'form-control','name':'description', 'id':'description'}),
                        
                    }

          
         






class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields  = ['comp_name','comp_email','comp_code','comp_mobile','comp_address']
        


class OrganizationForm(forms.ModelForm):
    class Meta:
        model     = Organization
        fields    = ['orgName','orgEmail','orgContact']
        labels    = {'orgName': 'Name','orgEmail': 'Email','orgContact': 'Contact'}
        widgets   = {
                        'orgName': forms.TextInput(attrs={'class': 'form-control','id':'name','placeholder':'Enter Full Name'}),
                        'orgEmail': forms.TextInput(attrs={'class': 'form-control','id':'email'}),
                        'orgContact': forms.TextInput(attrs={'class': 'form-control','id':'contact'}),
                    }
        help_texts = {'orgName': 'Some useful help text.'}
        error_messages = {'orgName': {'max_length':"This writer's name is too long.",},} 


