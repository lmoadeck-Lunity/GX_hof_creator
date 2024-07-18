# import HOF

# hof = HOF.HOF('testing')

# hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
# hof.add_infosystem('268CY','Kwun Tong Ferry','268C')
# hof.add_busstop_list(['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry'], '268C')
# hof.add_infosystem('268CZ','Long Ping Station','268C')
# hof.add_busstop_list(['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry'][::-1], '268C')


import HOF
hof = HOF.HOF_Hanover('testing')

# hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
# stops_268c = ['Long Ping Station', 'YOHO Mall II', 'YOHO Mall I','Tai Lam Tunnel BBI', 'Kwun Tong Ferry']
# hof.add_infosystem(True,'268C','Kwun Tong Ferry','Long Ping Station',stops_268c,stops_268c[::-1])
# stops_31M = ['Lei Pui Street', 'Shek Lei Comm. CPLX', 'Ta Tsuen Ping Street', 'Shek Yi Road', 'Lam Tin Street','Cheung Wing Road','Kwai Chun Court','Sun Kwai Hing Gardens', 'Metroplaza', 'Kwai Fong Station']
# hof.add_infosystem(True,'31M','Lei Pui Street','Kwai Fong Station',stops_31M,stops_31M[::-1])
# for m31 in stops_31M + stops_268c:
#     hof.add_stopreporter(m31,m31,6,6)
# hof.add_terminus(eric=int((HOF.ericcode('268CY'))),destination='Kwun Tong Ferry',flip=['268CY_1.png','268CY_2.png'],RTID='268C')
# a = hof.infosystem[1]
# a.trip1_class.routeno , a.trip1_class.Destination, a.trip1_class.ericcode = ['872X', 'goons', '872X']
# # # print(hof.showfullhof())
# # # print(hof.check_busstoplist())
# # # # hof.export_hof('268C.hof')
# # hof.save_to_json('268C.json')
hof.import_from_json('268C.json')
# print(hof.Infosystem.trip().__repr__())

print(hof.showfullhof())