from django.shortcuts import render
from .import forms
def student(request):
     form = forms.StudentForm()
     if request.method == 'POST':
          form = forms.StudentForm(request.POST)
          if form.is_valid():
              form.save(commit=True)
              print("From data inserted into database succesfully")
          return render(request, 'modelapp/thank.html', {'name': form.cleaned_data['Firstname']})

     return render(request, 'modelapp/index.html', {'form': form})
