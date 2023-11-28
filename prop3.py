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

p=Symbol("It is raining")
q=Symbol("Play Football")
r=Symbol("Happy")

p1=Implies(Not(p),q)
p2=Implies(q,r)

knowledge_base=And(p1,p2,r)
print(knowledge_base)

result=valid(Implies(And(p1,p2,r),q))
print(result)
