import HOF

hof = HOF.HOF('testing')

hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
hof.add_infosystem('268CY','Kwun Tong Ferry','268C')


print(list(str(i) for i in hof.ddu), list(str(i) for i in hof.infosystem))
