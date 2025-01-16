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
# for name in stops_268c:
#     hof.add_stopreporter(name,name,10,10,0.0,0.0)
# hof.add_infosystem(True,'268C','Kwun Tong Ferry','Long Ping Station',stops_268c,stops_268c[::-1])
# stops_31M = ['Lei Pui Street', 'Shek Lei Comm. CPLX', 'Ta Tsuen Ping Street', 'Shek Yi Road', 'Lam Tin Street','Cheung Wing Road','Kwai Chun Court','Sun Kwai Hing Gardens', 'Metroplaza', 'Kwai Fong Station']
# hof.add_infosystem(True,'31M','Lei Pui Street','Kwai Fong Station',stops_31M,stops_31M[::-1])

# print(hof.showfullhof())
# hof.save_to_db("testing")
# hof.load_from_db("testing")
# print(hof.export_hof("testing"))
hof.load_from_hof("Cherryland_VC_KMB_6W.hof")
hof.export_hof("Cherryland_VC_KMB_6W2.hof")
# print(hof.ddu,hof.stopreporter,hof.infosystem,hof.termini)
# for i in hof.infosystem:
# for i in hof.stopreporter:
    # print(i.Inbound_sectionfare,i.Outbound_sectionfare)
#     print(i)
# hof.add_ddu('268C','Kwun Tong Ferry','Long Ping Station',20.1,20.1,1,2)
hof.save_to_db("Cherryland_VC_KMB_6W")
# print(hof.showfullhof())