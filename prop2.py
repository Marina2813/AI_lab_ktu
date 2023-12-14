'''
I. It is not sunny this afternoon and it is colder than yesterday.
II. We will go swimming only if it is sunny.
III. If we do not go swimming then we will take a canoe trip.
IV. If we take a canoe trip, then we will be home by sunset.

a. Represent knowledge base
b. check if they are home by sunset'''

from sympy import *
from sympy.logic.inference import valid

p = Symbol("it is sunny")
q = Symbol("It is colder than yesterday")
r = Symbol("Will go swimming")
s = Symbol("will take a conoe trip")
t = Symbol("will be home by sunset")

p1 = And(Not(p),q)
p2 = Implies(r,p)
p3 = Implies(Not(r),s)
p4 = Implies(s,t)

kb = And(p1,p2,p3,p4)
print("Knowledge Base: ")
print(kb)

result = valid(Implies(kb,t))
print("")
print("result: ")
print(result)