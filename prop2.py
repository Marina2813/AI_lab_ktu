'''
Question

I. It is not sunny this afternoon and it is colder than yesterday.
II. We will go swimming only if it is sunny.
III. If we do not go swimming then we will take a canoe trip.
IV. If we take a canoe trip, then we will be home by sunset.
 Represent the knowledge base
 Check whether they will be home by sunset

'''
from sympy import *
from sympy.logic.inference import valid

from sympy.logic.inference import valid

p = Symbol("It is sunny")
q = Symbol("Colder than Yesterday")
r = Symbol("go swimming")
s = Symbol("take a canoe trip")
t = Symbol("at home by sunset")

p1 = And(Not(p),q)
p2 = Implies(r,p)
p3 = Implies(Not(r),s)
p4 = Implies(s,t)

knowledge_base = And(p1,p2,p3,p4)
print(knowledge_base)

result = valid(Implies(And(p1,p2,p3,p4),t))
print(result)
