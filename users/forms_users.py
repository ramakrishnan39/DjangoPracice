from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CUForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'username' , 'email', 'password1', 'password2']
    labels ={
      'first_name' : 'name',
    }
  
  def __init__(self, *args, **kwargs):
        super(CUForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'txt'})
  