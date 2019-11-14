
from ProgrammingClass.settings import judger_problem_dir
from Judger.checker import py_static_check
import os

problem_dir = judger_problem_dir

def static_check(problem_name, student_id):
    '''
    static_check(problem_name, student_id)
    (string) problem_name. the name of problem that located in settings.judger_problem_dir
    (string|int) student_id. the student id in database and a folder name inside the answer folder of problem name dir
    '''
    student_answer_dir = os.path.join(problem_dir, problem_name, str(student_id))
    writeup_file = os.path.join(problem_dir, problem_name, 'writeup', 'static.py')

    last_answer = ''
    all_answers = os.listdir(student_answer_dir)
    if (len(all_answers)):
        last_answer = sorted()[-1]
        answer_file = os.path.join(student_answer_dir, last_answer)
        return py_static_check(writeup_file, answer_file)
    
    return "There is no answer file in %s"%(student_answer_dir)
    
    

        
    
    