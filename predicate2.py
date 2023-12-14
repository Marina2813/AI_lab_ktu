'''Map Coloring Problem
The problem is to color each city using only three colors but no adjacent cities can be colored
the same.
'''
import pytholog as pl

kb = pl.KnowledgeBase()

kb([
    "different(red,green)",
    "different(red,blue)",
    "different(blue,green)",
    "different(blue,red)",
    "different(green,red)",
    "coloring(A,M,G,T,F):-different(M,T),different(A,T),different(G,T),different(M,A),different(A,G),different(G,F),different(A,F)",
])

print(kb.query(pl.Expr("coloring(Alabama,Mississpi,Georgia,Tennesse,Florida)"),cut=True))