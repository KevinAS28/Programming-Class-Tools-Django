from django.shortcuts import render, redirect, HttpResponse
from django import forms
import os
from django.contrib import messages 
from ProgrammingClass.settings import *
from Judger.judger_checker import static_check as judger_static_checker
#import django.utils.datastructures.MultiValueDictKeyError
# Create your views here.



def public_scoreboard(request):
    if (request.method=="GET"):
        return render(request, "public_scoreboard.html")

def problem_list(request):
    if (request.method=="GET"):
        problem_list = os.listdir(judger_problem_dir)
        problems = []
        index = 0
        for i in problem_list:
            problems.append([i, index])
        
        return render(request, "problem_list.html", {"problems": problems})            

def upload_answer(request):
    if (request.method=="POST"):
        # form = FileUploadForm(request.POST, request.FILES)
        # if (form.is_valid()):
        #     with open("/home/kevin/test", "wb+") as write:
        #         for chunk in request.FILES["script"].chunks():
        #             write.write(chunk)
            return redirect('judger:public_scoreboard')
        
    elif (request.method=="GET"):
        return render(request, "upload.html")


def problem_detail(request, problem):

    if (request.method == 'POST'):
        #check if problem really exist
        problem_list = os.listdir(judger_problem_dir)
        if (problem in problem_list):
            try:
                pyfile = request.FILES[judger_file_var_name]
            except:
                #return render(request, "problem_detail.html")
                return HttpResponse(str(request.FILES))


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
                    messages.info("YAY")
                if (not result):
                    messages.info("NOT YAY")
                if (type(result)==str):
                    messages.error(result)

                return redirect('judger:public_scoreboard')
            else:
                messages.error(request, "Problem not availble!")
        else:
            messages.error(request, "File Cannot be Empty!")
    return render(request, "problem_detail.html")
    

    return render(request, "problem_detail.html", {
        "max_answer_size": judger_answer_max_file,
        "accepted_extension": judger_accepted_extension,
        "file_var_name": judger_file_var_name
        })        