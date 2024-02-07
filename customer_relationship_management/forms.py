from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class YourRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
        
from .models import stdInsert
class StdInsertForm(forms.ModelForm):
    class Meta:
        model = stdInsert
        fields = '__all__'

from .models import conInsert
class conInsertForm(forms.ModelForm):
    class Meta:
        model = conInsert
        fields = '__all__'

from .models import taskInsert
class taskInsertForm(forms.ModelForm):
    class Meta:
        model = taskInsert
        fields = '__all__'        
        
from .models import billInsert
class billInsertForm(forms.ModelForm):
    class Meta:
        model = billInsert
        fields = '__all__'                 


from .models import accInsert
class accInsertForm(forms.ModelForm):
    class Meta:
        model = accInsert
        fields = '__all__'                 
        
from .models import saleInsert
class saleInsertForm(forms.ModelForm):
    class Meta:
        model = saleInsert
        fields = '__all__'          
        
from .models import dealInsert
class dealInsertForm(forms.ModelForm):
    class Meta:
        model = dealInsert
        fields = '__all__'             