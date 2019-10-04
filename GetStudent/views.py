from django.shortcuts import render, redirect
from GetStudent.getstudent_models.Student import Student
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from random import choice
from GetStudent.forms.StudentForm import StudentForm

# Create your views here.


def index(request):
    if (request.method=="GET"):
        students = list(Student.objects.all())
        return render(request, "student_list.html", {"students": students, "distance": range(0, len(students)*10, 10)})
        
        #return HttpResponse(str(len(students)), content_type="text")


def register(request):
    max_student = 16
    form = StudentForm(request.POST or None)
    if (request.method=="POST"):
        if (form.is_valid()):
            #get the all index
            students_index = set([i.index for i in Student.objects.all()])
            all_pos = list(set([i for i in range(1, max_student+1)]) - students_index)

            if (not (len(all_pos)<=0)):
                new_index = choice(all_pos)
                name = form.cleaned_data["name"]
                kelas  = form.cleaned_data["kelas"]
                new_student = Student(name=name, kelas=kelas, index=new_index)
                new_student.save()
            return redirect("get_student:student_list")
    return render(request, "student_form.html", {'form':form})
        

# class StudentCreate(CreateView):
#     model = Student
#     fields = ['name', 'kelas']
#     success_url = reverse_lazy('get_student:student_list')
#     max_student = 16

#     def form_valid(self, form):
#         nama = form.cleaned_data['name']
#         kelas = form.cleaned_data['kelas']
        
#         #get the all index
#         students_index = set([i.index for i in Student.objects.all()])
#         all_pos = list(set([i for i in range(1, self.max_student+1)]) - students_index)
#         new_index = choice(all_pos)
#         new_student = Student(name=nama, kelas=kelas, index=new_index)
#         new_student.save()

#         return redirect(self.request, "all")


#     def get_context_data(self, **kwargs):
#         context = super(StudentCreate, self).get_context_data(**kwargs)
#         context = super().get_context_data(**kwargs)
#         context["max_student"] = str(list(range(100)))
#         return context

        





    