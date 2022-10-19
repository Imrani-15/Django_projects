from django.contrib import admin
from modelapp.models import StudentFeedback
# Register your models here.
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Secondname','Phonenumber','EmailId','Feedback']
admin.site.register(StudentFeedback,StudentFeedbackAdmin)