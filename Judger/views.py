from django.shortcuts import render
import ProgrammingClass.settings as settings
import os
# Create your views here.

class Problem:
    title = ""
    problem = ""
    score = ""
    def __init__(self, title, problem, score=50):
        pass

def problem_index(request):
    if (request.method=="GET"):
        problem_dir = os.path.join(settings.BASE_DIR, "problems")
        problem_list = os.listdir(problem_dir)
        problem_m = []
        #for prob in problem_list:
