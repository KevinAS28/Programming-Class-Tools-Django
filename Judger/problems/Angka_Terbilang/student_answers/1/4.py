import numpy as np
from math import *
from fractions import Fraction as frac
from fractions import Fraction
import os
from importlib import reload
from pulp import *

deg = degrees

def bul(x):
    return round(x, 2)

def trigtable(fun, degr):
    table = {
        "sin":  {0: "0", 30: "1/2", "45": "sqrt(2)/2", 60: "sqrt(3)/2", 90: "1"},
        "cos":  {0: "1", 30: "sqrt(3)/2", 45: "sqrt(2)/2", 60: "1/2", 90: "0"},
        "tan":  {0: "0", 30: "sqrt(3)/2", 45: "1", 60: "sqrt(3)", 90: "undefined"},
        "asin": {0: "undefined", 30: "2", 45: "sqrt(2)", 60: "(2*sqrt(3))/3", 90: "1"},
        "acos": {0: "1", 30: "(2*sqrt(3))/3", 45: "sqrt(2)", 60: "2", 90: "undefined"},
        "atan": {0: "undefined", 30: "sqrt(3)", 45: "1", 60: "sqrt(3)/3", 90: "0"}
    }
    return table[fun][degr]

def c():
    os.system("clear")

def barar(a, r, n):
    return a+r*(n-1)

def derar(a, z, n):
    return (n/2)*(a+z)

def bargeo(a, r, n):
    return a*(r**(n-1))

def dergeo(a, r, n):
    if (r>1):
        return (a*(r**n -1))/(r-1)
    elif(r<1):
        return (a*(1-r**n))/(1-r)
    else:
        return "r = 0"

def poly(ini_list):
    """x^2 + 2x + 1 -> [1, 2, 1]"""
    result = np.roots(ini_list)
    print("that is when y = 0")
    return result

def coslaw(a, b, c):
    num = (a**2+b**2)-2*a*b*cos(radians(c))
    return "sqrt(%f)=%f"%(num, sqrt(num))

def coslawinv(a, b, c):
    return "%f deg"%(degrees(acos( (-c**2+a**2+b**2)/(2*a*b))))

def equ(listdlmlist, hasillist):
    """
    x + y + z = 3
    2x + 2y + 2z = 6
    3x + 3y + 3z = 9
    [[1, 1, 1], [2, 2, 2], [3, 3, ,3]], [3, 6, 9]
    """
    equ = np.array(listdlmlist)
    hasil = np.array(hasillist)
    return np.linalg.solve(equ, hasil)


def linprog(x1, y1, z1, x2, y2, z2, x3, y3):

    prob = LpProblem("Anything", LpMaximize)

    # Create problem variables
    x=LpVariable("A",0,None,LpInteger)
    y=LpVariable("B",0, None, LpInteger)

    # The objective function is added to 'prob' first
    prob += x3*x + y3*y, ""
    # The two constraints are entered
    prob += x1*x + y1*y <= z1, ""
    prob += x2*x + y2*y <= z2, ""

    # The problem is solved using PuLP's choice of Solver
    return prob.solve()

def mode(data, freq):
    freq.append(0)
    class_index = freq.index(max(freq))
    tb = data[class_index][0]-0.5
    d1 = freq[class_index] - freq[class_index-1]
    d2 = (freq[class_index] -freq[class_index+1])
    p = data[class_index][1]-data[class_index][0]+1
    return tb + abs(d1/(d1+d2))*p

def median(data, freq):
    n = sum(freq)

    class_index = 0
    n2 = round(n/2)
    temp = 0
    index = 0
    for i in freq:
        temp+=i
        if (n2<=temp):
            class_index = index
            temp-=i
            break
        index+=1

    fs = temp
    tb = data[class_index][0]-0.5
    p = data[class_index][1]-data[class_index][0]+1
    fme = freq[class_index]
    print("n: %f n2: %f fs: %f tb: %f p: %f fme: %f ci: %f"%(n, n2, fs, tb, p, fme, class_index))
    return tb+abs((n2 - fs)/fme)*p

def til(data, freq, c=1, q=4):
    """data, freq, c: dicari ke berapa
    q: quartil/desil/persentil?"""
    n = sum(freq)

    class_index = 0
    inq = (c*n)/q
    temp = 0
    index = 0
    for i in freq:
        temp+=i
        if (inq<=temp):
            class_index = index
            temp-=i
            break
        index+=1    

    fs = temp
    tb = data[class_index][0]-0.5
    p = data[class_index][1]-data[class_index][0]+1
    fme = freq[class_index]
    print("n: %f inq: %f fs: %f tb: %f p: %f fme: %f ci: %f"%(n, inq, fs, tb, p, fme, class_index))
    return tb+abs((inq - fs)/fme)*p

def tilrange(data, freq, q=4):    
    last = til(data, freq, 3, q)
    first = til(data, freq, 1, q)
    return last-first


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


