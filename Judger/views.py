from django.shortcuts import render, redirect, HttpResponse
from django import forms
import ProgrammingClass.settings as settings
import os
# Create your views here.


class FileUploadForm(forms.Form):
    script = forms.FileField()


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
        problem_list = os.listdir(settings.problem_dir)
        problems = []
        index = 0
        for i in problem_list:
            problems.append([i, index])
        
        return render(request, "problem_list.html", {"problems": problems})            
            
def problem_detail(request, problem):
    if (request.method=="GET"):
        print(problem)
    return HttpResponse(problem)
        
        