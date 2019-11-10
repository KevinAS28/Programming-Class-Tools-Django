from django.shortcuts import render, redirect
from django import forms
import ProgrammingClass.settings as settings
import os
# Create your views here.

class Problem:
    title = ""
    problem = ""
    def __init__(self, title, problem):
        self.title = title
        self.problem = problem

class Counter:
    count = 2
    def increment(self):
        self.count+=50
        return ''

class FileUploadForm(forms.Form):
    script = forms.FileField()

problem_dir = os.path.join(settings.BASE_DIR, "problems")

def upload_file(request):
    if (request.method=="POST"):
        form = FileUploadForm(request.POST, request.FILES)
        if (form.is_valid()):
            with open("/home/kevin/test", "wb+") as write:
                for chunk in request.FILES["script"].chunks():
                    write.write(chunk)
            return redirect('judger:public_scoreboard')
        
    elif (request.method=="GET"):
        return render(request, "upload.html")

def public_scoreboard(request):
    if (request.method=="GET"):
        return render(request, "public_scoreboard.html", {'yay': list(range(10)), "counter": Counter()})

def problem_list(request):
    if (request.method=="GET"):
        problem_list = os.listdir(problem_dir)
        return render(request, "problem_list", {"problems": problem_list})            
            

def problem_detail(request):
    if (request.method=="GET"):
        problem = request.GET["problem"]
        if ((problem==None) or (problem=="") ):
            return redirect('judger:problem_list')
        
        