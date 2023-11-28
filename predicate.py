import pytholog as pl

knowlegde_base = pl.KnowledgeBase()


knowlegde_base([
    "likes(noor, sausage)",
    "likes(melissa, pasta)",
    "likes(dmitry, cookie)",
    "likes(nikita, sausage)",
    "likes(assel, lemonade)",
    "food_type(gouda, cheese)",
    "food_type(ritz, cracker)",
    "food_type(steak, meat)",
    "food_type(sausage, meat)",
    "food_type(lemonade, juice)",
    "food_type(mojito, juice)",
    "food_type(cookie, dessert)",
    "flavor(sweet, dessert)",
    "flavor(savory, meat)",
    "flavor(savory, cheese)",
    "flavor(sweet, juice)",
    "food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z)",
    "dish_to_like(X, Y) :- likes(X, L), food_type(L, T), flavor(F, T), food_flavor(Y, F), L != Y"
])

r1 = knowlegde_base.query(pl.Expr("likes(noor,sausage)"))
result2 = knowlegde_base.query(pl.Expr("likes(noor, pasta)"))
result3 = knowlegde_base.query(pl.Expr("food_flavor(What, sweet)"))
print(r1)
print(result2)
print(result3)