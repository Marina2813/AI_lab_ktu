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
from sympy.logic.inference import satisfiable
from sympy.logic.inference import valid

rain = Symbol("rain") #it  is raining
Hagrid = Symbol("Hagrid") #Harry visited Hagrid
Dumbledore = Symbol("Dumbledore") #Harry visited Dumbledore


p1 = Implies( Not(rain), Hagrid)
p2 = Or(Hagrid,Dumbledore)
p3 = Not(And(Hagrid,Dumbledore))
p4 = Dumbledore

#saving sentences in kb
knowledge_base = And(p1,p2,p3,p4)
print(knowledge_base)
models = satisfiable(knowledge_base,all_models = True)
for model in models:
    print(model)

p5=And(Not(Hagrid),Dumbledore)
p6=Implies(Dumbledore,rain)
print(valid(Implies(And(p5,p6),rain)))

p1=And((rain),Not(Hagrid))
print(p1)
print(satisfiable(p1))


