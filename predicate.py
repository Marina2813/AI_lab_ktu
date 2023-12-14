'''Question:- Set A
Create a knowledge base with the following facts and find out the answer for the queries listed
below
1.Noor likes sausage ,it’s food type is meat and the flavour of meat is savoury.
2. Dmitry likes cookies ,it’s food type is dessert and the flavour of cookie is sweet.
3. Aisel likes lemonade,it’s food type is juice and the flavour of juice is sweet.
4. Mellissa likes pasta ,it’s food type is cheese and the flavour of cheese is savoury.

I) Recommend dishes to persons based on taste preferences.
II) Find out the food flavour of a dish liked by a person
III) Check whether Noor likes pasta.'''

import pytholog as pl

k_base = pl.KnowledgeBase()
k_base([
    "likes(noor,sausage)",
    "likes(dmitry,cookies)",
    "likes(aisel,lemonade)",
    "likes(mellissa,pasta)",
    "food_type(sausage,meat)",
    "food_type(cookies,dessert)",
    "food_type(lemonade,juice)",
    "food_type(pasta,cheese)",
    "flavour(meat,savoury)",
    "flavour(dessert,sweet)",
    "flavour(juice,sweet)",
    "flavour(cheese,savoury)",
    "food_flavour(X,Y):-food_type(X,Z),flavour(Z,Y)",
    "recomend_dish(X,Y):-likes(X,L),food_type(L,Z),flavour(Z,f),food_flavour(L,f),L!=Y"
])

r1 = k_base.query(pl.Expr("likes(noor,sausage)"))
r2 = k_base.query(pl.Expr("likes(noor,pasta)"))
r3 = k_base.query(pl.Expr("food_flavour(What,savoury)"))
print(r1)
print(r2)
print(r3)
print(k_base.query(pl.Expr("flavour(What,sweet)")))
print(k_base.query(pl.Expr("recomend_dish(noor,cheese)")))
