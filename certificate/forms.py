from django import forms    
from .models import Certificate
class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_id','user_id', 'course_id', 'issue_date', 'certificate_url']
        widgets = {
            'certificate_id': forms.NumberInput(),
            'user_id': forms.NumberInput(),
            'course_id': forms.NumberInput(),
            'issue_date': forms.DateInput(attrs={'class': 'form-control'}),
            'certificate_url': forms.TextInput(attrs={'class': 'form-control'}),
        }