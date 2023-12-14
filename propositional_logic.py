#Propositional logic deals with propositions, which are declarative statements that are either true or false but not both.

'''Consider the following sentences:
SET -A
1. If it didn’t rain, Harry visited Hagrid today.
2. Harry visited Hagrid or Dumbledore today, but not both.
3. Harry visited Dumbledore today.

i) Represent these knowledge in knowledge base
ii) Check whether “harry visited hagrid”
iii) Check whether “it rained today”'''

from sympy import *
from sympy.logic.inference import valid

p = Symbol("it rained today")
q = Symbol("Harry visited Hagrid")
r = Symbol("Harry visited Dumbledore")

p1 = Implies(Not(p),q)
p2 = Or(q,r)
p3 = Not(And(q,r))
p4 = r

kb = And(p1,p2,p3,p4)
print("KNOWLEDGE BASE")
print(kb)

r1 = valid(Implies(kb,q))
r2 = valid(Implies(kb,p))
print(r1)
print(r2)