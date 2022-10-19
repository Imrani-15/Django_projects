from django import forms
from modelapp.models import StudentFeedback

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = '__all__'