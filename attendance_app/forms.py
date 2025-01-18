from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_city': forms.TextInput(attrs={'class': 'form-control'}),
            'user_zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'user_phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'user_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    