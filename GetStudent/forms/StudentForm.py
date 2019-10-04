from django import forms  
#from ProgrammingClass.universal_models.Student import Student
from GetStudent.getstudent_models.Student import Student

class StudentForm(forms.ModelForm):  
    index = forms.IntegerField(required=False, widget=forms.HiddenInput())
    class Meta:  
        model = Student
        fields = "__all__"  