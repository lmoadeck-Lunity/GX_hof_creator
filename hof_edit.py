# import HOF

# hof = HOF.HOF('testing')

# hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
# hof.add_infosystem('268CY','Kwun Tong Ferry','268C')
# hof.add_busstop_list(['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry'], '268C')
# hof.add_infosystem('268CZ','Long Ping Station','268C')
# hof.add_busstop_list(['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry'][::-1], '268C')


import HOF
hof = HOF.HOF('testing')

hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
stops_268c = ['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry']
hof.add_infosystem(True,'268C','Kwun Tong Ferry','Long Ping Station',stops_268c,stops_268c[::-1])
hof.add_terminus(eric=int((HOF.ericcode('268CY'))),destination='Kwun Tong Ferry',flip=['268CY_1.png','268CY_2.png'],RTID='268C')
print(hof.showfullhof())