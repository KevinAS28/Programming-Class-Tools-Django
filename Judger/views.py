from django.shortcuts import render, redirect, HttpResponse
from django import forms
import os
from django.contrib import messages 
from ProgrammingClass.settings import *
from Judger.judger_checker import static_check as judger_static_checker
from Judger.models import StuProSco
from django.contrib.auth.decorators import login_required
# Create your views here.



def public_scoreboard(request):
    if (request.method=="GET"):
        return render(request, "public_scoreboard.html", {"data": StuProSco.objects.all()})

def problem_list(request):
    if (request.method=="GET"):
        problem_list = os.listdir(judger_problem_dir)
        problems = []
        index = 0
        for i in problem_list:
            problems.append([i, index])
        
        return render(request, "problem_list.html", {"problems": problems})            

def problem_detail_page(request, additional=dict()):
    options = {
        "max_answer_size": str(judger_answer_max_file),
        "accepted_extension": judger_accepted_extension,
        "file_var_name": judger_file_var_name
        }
    for key in additional:
        options[key] = additional[key]

    return render(request, "problem_detail.html", options)            


def upload_answer(request, problem):
    if (request.method == 'POST'):
        #check if problem really exist
        problem_list = os.listdir(judger_problem_dir)
        if (problem in problem_list):
            try:
                pyfile = request.FILES[judger_file_var_name]
            except:
                #return render(request, "problem_detail.html")
                print(request.FILES)
                return redirect('judger:upload_answer')


            #check if the user upload the file
            if (pyfile):
                upload_dir = judger_answer_upload_dir.format(problem_name=problem, student_id="1")
                
                #check if the directory not exist
                if (not os.access(upload_dir, os.R_OK)):
                    os.makedirs(upload_dir)

                #check if the directory not writeable
                if (not os.access(upload_dir, os.W_OK)):
                    print("cannot write file {filename} to {dir_upload}".format(filename=pyfile.name, dir_upload=upload_dir))
                    messages.error("server error. please report to admin")
                    
                #write the uploaded file to the server
                file_name_to_write = ''
                all_answer = os.listdir(upload_dir)
                if (not len(all_answer)):
                    file_name_to_write = '0.py'
                else:
                    file_name_to_write = str(int(sorted(all_answer)[-1].rstrip('.py'))+1)+'.py'

                with open(os.path.join(upload_dir, file_name_to_write), "wb+") as pyfilewrite:
                    for chunk in pyfile.chunks():
                        pyfilewrite.write(chunk)

                #check the written file
                result = judger_static_checker(problem, 1)
                if (result and (type(result)==bool)):
                    #if the answer correct

                    print("YAY")
                    messages.info(request, f"YAY")
                if (not result):
                    #if the answer incorrect
                    print("NOT YAY")
                    messages.info(request, f"NOT YAY")
                if (type(result)==str):
                    #if error
                    print("ERRORRRRRRRR", result)
                    messages.error(request, result)

                return redirect('judger:public_scoreboard')
            else:
                messages.error(request, "Problem not availble!")
        else:
            messages.error(request, "File Cannot be Empty!")

def problem_detail(request, problem):

    return problem_detail_page(request, {"problem": problem})