'''
Question
Consider the following sentences
   i) If it isn’t raining, then I play football
   ii) If I play football , then I am happy
   iii)It is raining

1.Represent these knowledge in knowledge base 
2.Check whether “I play football”
'''
from sympy import *
from sympy.logic.inference import valid

p = Symbol("it is raining")
q = Symbol("I play football")
r = Symbol("I am happy")

p1 = Implies(Not(r),q)
p2 = Implies(q,r)
p3 = r

kb=And(p1,p2,p3)

result = valid(Implies(kb,q))
print(result)
