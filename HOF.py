from string import Template
from types import GeneratorType
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Template):  # Assuming 'Template' is your custom class
            return None  # Or however you wish to represent your object
        # Let the base class default method raise the TypeError
        if isinstance(obj,HOF_Hanover.Infosystem.trip):
            return obj.__repr__()
        if isinstance(obj,HOF_Hanover.Infosystem.busstop_list):
            return obj.__repr__()
        return json.JSONEncoder.default(self, obj)
        
class ericcode:
    mapping = {'a': 11, 'b': 12, 'c':13,'d':21,'e':22,'f':23,'g':31,'h':32,'i':33,'j':41,'k':42,'l':43,'m':51,'n':52,'o':53,'p':61,'q':62,'r':63,'s':71,'t':72,'u':73,'v':81,'w':82,'x':83,'y':91,'z':92,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def retstr(self) -> str:
        returnstring = ''.join(self.eric)
        if len(returnstring) < 6:
            returnstring = returnstring + '0'
        return returnstring
    def __init__(self, code: str) -> None:
        self.eric = map(str,[self.mapping[c] for c in (code.lower() if isinstance(code, str) else str(code))])
    def __len__(self) -> int:
        return len(''.join(self.eric))
    def __str__(self) -> str:
        returnstring = ''.join(self.eric)
        if len(returnstring) < 6:
            returnstring = returnstring + '0'
        return returnstring
    def __int__(self) -> int:
        return int(str(self.retstr()))
class gorbacode:
    mapping = {'a': 11, 'b': 12, 'c':13,'d':21,'e':22,'f':23,'g':31,'h':32,'i':33,'j':41,'k':42,'l':43,'m':51,'n':52,'o':53,'p':61,'q':62,'r':63,'s':71,'t':72,'u':73,'v':81,'w':82,'x':83,'y':91,'z':92,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def __init__(self) -> None:
        raise NotImplementedError("Gorba code is not implemented yet")
    '''
    I dont know what code gorba uses, so I will leave this empty for now
    '''


class HOF_Hanover:
    name = 'Default'
    servicetrip = 'Not In Service'
    ddu : list['Busstop_DDU'] = []
    stopreporter : list['Busstop_Stopreporter'] = []
    termini : list['Termini'] = []
    infosystem : list['Infosystem'] = []
    ddu_expected_keys = ['RTNO','Outbound_dir','Inbound_dir','Outbound_price','Inbound_price','sectiontimes_Y','sectiontimes_Z']
    stopreporter_expected_keys = ['name','EngDisplay','ChiSeconds','EngSeconds','Outbound_sectionfare','Inbound_sectionfare','comment']
    termini_expected_keys = ['allexit','eric','destination','busfull','flip','RTID']
    infosystem_expected_keys = ['single_or_dual_dir','route','dir1','dir2','bustoplist1','bustoplist2']
    header_template = Template('''------------------------------------------
Created with Hof Creator for GX7767 Hoilun
https://github.com/FreeHK-Lunity/GX_hof_creator/
------------------------------------------

#####################
    General Info     
#####################
[name]
$name

[servicetrip]
$servicetrip

stringcount_terminus
6

stringcount_busstop
4
#####################
    Destination
#####################
''')
    termini_template = Template('''[addterminus$allexit]
$eric
$destination
$busfull
$pai_page4
$pai_page3
$pai_page2
$pai_page1
$RTID
.........................
''')
    stopreporter_template = Template('''[addbusstop]
$name
$EngDisplay
$ChiSeconds $EngSeconds
$Outbound_sectionfare
$Inbound_sectionfare
.........................$comment
''')
    ddu_template = Template('''[addbusstop]
$RTNO
$Outbound_dir \t\t$sectiontimes_Y
$Inbound_dir \t\t$sectiontimes_Z
$Outbound_price
$Inbound_price
.........................
''')
    trip_template = Template('''[infosystem_trip]
$ericcode
$Destination
$ericcode
$routenoanddir
''')
    busstop_list_template = Template('''\n[infosystem_busstop_list]
$amount_of_stops
$rtno
$busstops

''')
    def __init__(self,name:str='Default',servicetrip:str='Not In Service') -> None:
        self.name = name
        self.servicetrip = servicetrip


    class Termini():
        def __init__(self,allexit:bool = False, eric: int = 0, destination: str = '', busfull: str = '', flip: list[str] = [], RTID: str = '') -> None: #flip is a list of strings, eric will be inputted as '289XZ' and converted to 2899192
            self._allexit = '_allexit' if allexit else ''
            self._eric = eric
            self._destination = destination
            self._busfull = busfull
            self._flip = flip
            self._flup4 = flip[3] if len(flip) > 3 else ''
            self._flup3 = flip[2] if len(flip) > 2 else ''
            self._flup2 = flip[1] if len(flip) > 1 else ''
            self._flup1 = flip[0] if len(flip) > 0 else ''
            self._RTID = RTID
        # def set_allexit(self, allexit: bool) -> None:
        #     self._allexit = '_allexit' if allexit else ''
        # def set_eric(self, eric: str) -> None:
        #     self._eric = str(ericcode(eric))
        #     self._RTID = eric
        # def set_destination(self, destination: str) -> None:
        #     self._destination = destination
        # def set_busfull(self, busfull: str) -> None:
        #     self._busfull = busfull
        # def set_flip(self, flip: list[str]) -> None:
        #     self._flip = flip

        @property
        def eric(self) -> str:
            return str(self._eric)
        @eric.setter
        def eric(self, value: str) -> None:
            self._eric = str(ericcode(value))
            self._RTID = value[:3]
        @property
        def RTID(self) -> str:
            return str(self._RTID)
        @property
        def destination(self) -> str:
            return str(self._destination)
        @destination.setter
        def destination(self, value: str) -> None:
            self._destination = value
        @property
        def busfull(self) -> str:
            return str(self._busfull)
        @busfull.setter
        def busfull(self, value: str) -> None:
            self._busfull = value
        @property
        def flip(self) -> list[str]:
            return self._flip
        @flip.setter
        def flip(self, value: list[str]) -> None:
            self._flip = value
            self._flup4 = value[3] if len(value) > 3 else ''
            self._flup3 = value[2] if len(value) > 2 else ''
            self._flup2 = value[1] if len(value) > 1 else ''
            self._flup1 = value[0] if len(value) > 0 else ''
        @property
        def allexit(self) -> str:
            return self._allexit
        @allexit.setter
        def allexit(self, value: bool) -> None:
            self._allexit = '_allexit' if value else ''
        
        
        def __str__(self) -> str:
            return HOF_Hanover.termini_template.substitute(allexit=self._allexit, eric=self._eric, destination=self._destination, busfull=self._busfull, pai_page4 = self._flup4, pai_page3 = self._flup3, pai_page2 = self._flup2,pai_page1 = self._flup1,RTID=self._RTID)

    class Busstop_Stopreporter:
        def __init__(self, name:str = '',EngDisplay:str = '',ChiSeconds:int = 0,EngSeconds:int = 0,Outbound_sectionfare:float = 0.0,Inbound_sectionfare:float = 0.0,comment: str = '') -> None:
            self._name = name
            self._EngDisplay = EngDisplay
            self._ChiSeconds = str(ChiSeconds).rjust(2,'0')
            self._EngSeconds = str(EngSeconds).rjust(2,'0')
            self._Outbound_sectionfare = f"${Outbound_sectionfare:.1f}" if Outbound_sectionfare != 0.0 else name
            self._Inbound_sectionfare = f"${Inbound_sectionfare:.1f}" if Inbound_sectionfare != 0.0 else name
            self._Autoskip = False
            self._pages = 1
            self._engscroll = self._EngDisplay.count('@') // 2
            self._comment = comment

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, value: str) -> None:
            modified_name = value
            if self._engscroll > 2 and not modified_name[-1] == '!':
                modified_name += "!"
            if self._pages == 2 and not (modified_name[0:1] == '!' or modified_name[0:2] == '_!'):
                modified_name = '!' + modified_name
            if self._pages == 3 and not (modified_name[0:2] == '!!' or modified_name[0:3] == '_!!'):
                modified_name = '!' + modified_name
            if self._Autoskip and not modified_name[-1] == '_':
                modified_name += "_"
            self._name = modified_name

        @property
        def EngDisplay(self) -> str:
            return self._EngDisplay

        @EngDisplay.setter
        def EngDisplay(self, value: str) -> None:
            self._EngDisplay = value
            self._engscroll = self._EngDisplay.count('@') / 2
            if self._engscroll > 2:
                self._name = self._name #this is to trigger the setter of name to add the exclamation mark
        @property
        def ChiSeconds(self) -> int:
            return int(self._ChiSeconds)

        @ChiSeconds.setter
        def ChiSeconds(self, value: int) -> None:
            self._ChiSeconds = str(value).rjust(2, '0')

        @property
        def EngSeconds(self) -> int:
            return int(self._EngSeconds)

        @EngSeconds.setter
        def EngSeconds(self, value: int) -> None:
            self._EngSeconds = str(value).rjust(2, '0')

        @property
        def Outbound_sectionfare(self) -> float:
            return float(self._Outbound_sectionfare.strip('$'))

        @Outbound_sectionfare.setter
        def Outbound_sectionfare(self, value: float) -> None:
            self._Outbound_sectionfare = f"${value:.1f}" if value != 0.0 else self._name

        @property
        def Inbound_sectionfare(self) -> float:
            return float(self._Inbound_sectionfare.strip('$'))

        @Inbound_sectionfare.setter
        def Inbound_sectionfare(self, value: float) -> None:
            self._Inbound_sectionfare = f"${value:.1f}" if value != 0.0 else self._name
        def __str__(self) -> str:
            return HOF_Hanover.stopreporter_template.substitute(name=self._name, EngDisplay=self._EngDisplay, ChiSeconds=self._ChiSeconds, EngSeconds=self._EngSeconds, Outbound_sectionfare=self._Outbound_sectionfare, Inbound_sectionfare=self._Inbound_sectionfare,comment=self._comment)
        
        def add_chi_page(self) -> None:
            if self._pages == 3:
                print("GPSHoilun does not support more than 3 pages")
                return
            self._pages += 1
            self._name = self._name #this is to trigger the setter of name to add the exclamation mark
        @property
        def pass_autoskip(self) -> bool:
            return self._Autoskip
        @pass_autoskip.setter
        def pass_autoskip(self, value: bool) -> None:
            self._Autoskip = value
            self._name = self._name #this is to trigger the setter of name to add the underscore
        # def set_pass(self, value: bool) -> None:
        #     self._Autoskip = value
        @property
        def comment(self) -> str:
            return self._comment
        @comment.setter
        def comment(self, value: str) -> None:
            self._comment = value

        
    class Busstop_DDU:
        def __init__(self, RTNO:str = '',Outbound_dir:str = '',Inbound_dir:str = '',Outbound_price:float = 0.0,Inbound_price:float = 0.0,sectiontimes_Y:int = 0,sectiontimes_Z:int = 0) -> None: 
            self._RTNO = RTNO
            self._Outbound_dir = Outbound_dir
            self._Inbound_dir = Inbound_dir
            self._Outbound_price = f"${Outbound_price:.1f}"
            self._Inbound_price = f"${Inbound_price:.1f}"
            self._sectiontimes_Y = sectiontimes_Y
            self._sectiontimes_Z = sectiontimes_Z
        @property
        def RTNO(self) -> str:
            return self._RTNO
        @RTNO.setter
        def RTNO(self, value: str) -> None:
            self._RTNO = value
        @property
        def Outbound_dir(self) -> str:
            return self._Outbound_dir
        @Outbound_dir.setter
        def Outbound_dir(self, value: str) -> None:
            self._Outbound_dir = value
        @property
        def Inbound_dir(self) -> str:
            return self._Inbound_dir
        @Inbound_dir.setter
        def Inbound_dir(self, value: str) -> None:
            self._Inbound_dir = value
        @property
        def Outbound_price(self) -> float:
            return float(self._Outbound_price.strip('$'))
        @Outbound_price.setter
        def Outbound_price(self, value: float) -> None:
            self._Outbound_price = f"${value:.1f}"
        @property
        def Inbound_price(self) -> float:
            return float(self._Inbound_price.strip('$'))
        @Inbound_price.setter
        def Inbound_price(self, value: float) -> None:
            self._Inbound_price = f"${value:.1f}"
        @property
        def sectiontimes_Y(self) -> int:
            return self._sectiontimes_Y
        @sectiontimes_Y.setter
        def sectiontimes_Y(self, value: int) -> None:
            self._sectiontimes_Y = value
        @property
        def sectiontimes_Z(self) -> int:
            return self._sectiontimes_Z
        @sectiontimes_Z.setter
        def sectiontimes_Z(self, value: int) -> None:
            self._sectiontimes_Z = value
        def __str__(self) -> str:
            return HOF_Hanover.ddu_template.substitute(RTNO=self._RTNO, Outbound_dir=self._Outbound_dir, Inbound_dir=self._Inbound_dir, Outbound_price=self._Outbound_price, Inbound_price=self._Inbound_price, sectiontimes_Y=self._sectiontimes_Y, sectiontimes_Z=self._sectiontimes_Z)
        
    class Infosystem:
        '''
        Modifications of the Infosystem class will be made for enforcing the correct format of infosystems
        (infosystem_trip and infosystem_busstop_list needs to be in a pair for the correct format, and both needs to be in a pair for GPSHoilun to read the hof correctly)
        '''
        valid_infosystem = Template('''
##################1st direction#############
$trip1
////////////////////////////////////////////
$stoplist1
------------------2nd direction-------------
$trip2
////////////////////////////////////////////
$stoplist2
.............................................
''')
        class trip:
            def __init__(self,eric:str =  '',Destination:str = '',RouteNo:str = '') -> None:
                self._ericcode = str(ericcode(eric))
                self._Destination = Destination
                self._routeno = RouteNo
            @property
            def ericcode(self) -> str:
                return str(self._ericcode)
            @ericcode.setter
            def ericcode(self, value: str) -> None:
                self._ericcode = str(ericcode(value))
            @property
            def Destination(self) -> str:
                return self._Destination
            @Destination.setter
            def Destination(self, value: str) -> None:
                self._Destination = value
            @property
            def routeno(self) -> str:
                return self._routeno
            @routeno.setter
            def routeno(self, value: str) -> None:
                self._routeno = f"{value}"
            def __str__(self) -> str:
                return HOF_Hanover.trip_template.substitute(ericcode=self._ericcode, Destination=self._Destination, routenoanddir=f"{self._routeno}")
            def __repr__(self) -> list[str]:
                return [self._ericcode, self._Destination, self._routeno]
        class busstop_list():
            def __init__(self,bus_stops:list[str] = [],rtno:str = '') -> None:
                self._busstops = bus_stops
                self._rtno = rtno
                self._amount_of_stops = len(bus_stops)
            @property
            def busstops(self) -> str:
                return '\n'.join(self._busstops)
            @busstops.setter
            def busstops(self, value: list[str]) -> None:
                self._busstops = value
                self._amount_of_stops = len(value)
            @busstops.deleter
            def busstops(self, deleteion_pos) -> None:
                del self._busstops[deleteion_pos]
                self._amount_of_stops = len(self._busstops)
            @property
            def rtno(self) -> str:
                return self._rtno
            @rtno.setter
            def rtno(self, value: str) -> None:
                self._rtno = value
            @property
            def amount_of_stops(self) -> int:
                return self._amount_of_stops
            @amount_of_stops.setter
            def amount_of_stops(self, value: int) -> None:
                self._amount_of_stops = value
            def __str__(self) -> str:
                return HOF_Hanover.busstop_list_template.substitute(amount_of_stops=self._amount_of_stops, rtno=self._rtno, busstops=self.busstops)
            def __repr__(self) -> list[int | str | list[str]]:
                return [self._amount_of_stops, self._rtno, self._busstops]
            def __iter__(self) -> list[str]:
                return self._busstops


        def __init__(self,single_or_dual_dir:bool = True,route:str='',dir1:str='',dir2:str='',bustoplist1:list[str]=[],bustoplist2:list[str]=[]) -> None: 
            #route must be inputted as '289X', we will automaticllu add Y and Z at the end
            #single_or_dual_dir with True being dual direction and False being single direction
            self._single_or_dual_dir = single_or_dual_dir
            self._trip1 = self.trip(f"{route}Y",dir1,route)
            self._trip2 = self.trip(f"{route}Z",dir2,route)
            self._busstop_list1 = self.busstop_list(bustoplist1,route)
            self._busstop_list2 = self.busstop_list(bustoplist2,route)
        @property
        def single_or_dual_dir(self) -> bool:
            return self._single_or_dual_dir
        @single_or_dual_dir.setter
        def single_or_dual_dir(self, value: bool) -> None:
            self._single_or_dual_dir = value
        @property
        def direction1(self) -> str:
            return self._trip1.Destination
        @direction1.setter
        def direction1(self, value: str) -> None:
            self._trip1.Destination = value
        @property
        def direction2(self) -> str:
            return self._trip2.Destination
        @direction2.setter
        def direction2(self, value: str) -> None:
            self._trip2.Destination = value
        @property
        def route(self) -> str:
            return self._trip1.routeno
        @route.setter
        def route(self, value: str) -> None:
            self._trip1.routeno = value
            self._trip2.routeno = value
            self._busstop_list1.rtno = value
            self._busstop_list2.rtno = value
        @property
        def busstop_list1(self) -> str:
            return str(self._busstop_list1)
        @busstop_list1.setter
        def busstop_list1(self, value: list[str]) -> None:
            self._busstop_list1.busstops = value
        @property
        def busstop_list2(self) -> str:
            return str(self._busstop_list2)
        @busstop_list2.setter
        def busstop_list2(self, value: list[str]) -> None:
            self._busstop_list2.busstops = value
        #enable direct access to trip and busstop_list
        @property
        def trip1_class(self) -> trip:
            return self._trip1
        @property
        def trip2_class(self) -> trip:
            return self._trip2
        @property
        def busstop_list1_class(self) -> busstop_list:
            return self._busstop_list1
        @property
        def busstop_list2_class(self) -> busstop_list:
            return self._busstop_list2
        
        def __str__(self) -> str:
            return self.valid_infosystem.substitute(trip1=self._trip1, stoplist1=self._busstop_list1, trip2=self._trip2, stoplist2=self._busstop_list2)
        


        

        
        
        #check busstop validicity
    def check_busstoplist(self) -> bool:
        flag = True
        # Preprocess stopreporter to a set of names for O(1) lookup
        stopreporter_names = {k.name for k in self.stopreporter}
        
        for info in self.infosystem:
            for bus_stop in info.busstop_list1_class._busstops + info.busstop_list2_class._busstops:
                if bus_stop not in stopreporter_names:
                    print(f"Busstop {str(bus_stop)} not found in stopreporter")
                    flag = False

        return flag
    
    def add_ddu(self, RTNO:str = '',Outbound_dir:str = '',Inbound_dir:str = '',Outbound_price:float = 0.0,Inbound_price:float = 0.0,sectiontimes_Y:int = 0,sectiontimes_Z:int = 0) -> None:
        self.ddu.append(self.Busstop_DDU(RTNO,Outbound_dir,Inbound_dir,Outbound_price,Inbound_price,sectiontimes_Y,sectiontimes_Z))
    def add_stopreporter(self, name:str = '',EngDisplay:str = '',ChiSeconds:int = 0,EngSeconds:int = 0,Outbound_sectionfare:float = 0.0,Inbound_sectionfare:float = 0.0) -> None:
        self.stopreporter.append(self.Busstop_Stopreporter(name,EngDisplay,ChiSeconds,EngSeconds,Outbound_sectionfare,Inbound_sectionfare))
    def add_terminus(self,allexit:bool = False, eric: int = 0, destination: str = '', busfull: str = '', flip: list[str] = [], RTID: str = '') -> None:
        self.termini.append(self.Termini(allexit, eric, destination, busfull, flip, RTID))
    # def add_infosystem(self,eric:str =  '',Destination:str = '',RouteNo:str = '') -> None:
    #     self.infosystem.append(self.Infosystem.trip(eric,Destination,RouteNo))
    # def add_busstop_list(self,bus_stops:list[str] = [],rtno:str = '') -> None:
    #     self.infosystem.append(self.Infosystem.busstop_list(bus_stops,rtno))
    def add_infosystem(self,single_or_dual_dir:bool,route:str='',dir1:str='',dir2:str='',bustoplist1:list[str]=[],bustoplist2:list[str]=[]) -> None:
        self.infosystem.append(self.Infosystem(single_or_dual_dir,route,dir1,dir2,bustoplist1,bustoplist2))
    def showfullhof(self) -> str:
        returnstring = '\n'.join([''.join(self.header_template.substitute(name = self.name,servicetrip = self.servicetrip)),'\n'.join((str(i) for i in self.termini)),'\n'.join(str(i) for i in self.ddu),'\n'.join((str(i) for i in self.stopreporter)),'\n'.join((str(i) for i in self.infosystem))])
        return returnstring
    def export_hof(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.showfullhof())
            print(f"Exported to {filename}, all comments have been destroyed.")
    def save_to_json(self, filename: str) -> None:
        import json
        with open(filename, 'w') as f:
            json.dump({'name': self.name, 'servicetrip': self.servicetrip, 'ddu': [vars(i) for i in self.ddu], 'termini': [vars(i) for i in self.termini],'stopreporter': [vars(i) for i in self.stopreporter], 'infosystem': [vars(i) for i in self.infosystem]}, f, indent=2, cls=CustomEncoder)
    def import_from_json(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.name = data['name']
            self.servicetrip = data['servicetrip']
            self.infosystem = [self._create_infosystem(item) for item in data['infosystem']]
            self.termini = [self._create_termini(item) for item in data['termini']]
            self.ddu = [self._create_ddu(item) for item in data['ddu']]
            self.stopreporter = [self._create_stopreporter(item) for item in data['stopreporter']]
    def _create_infosystem(self, item):
        # print(item)
        temp = self.Infosystem()
        for k, v in item.items():
            attr = k.lstrip('_')
            print(attr,v)

            if attr in ['single_or_dual_dir']:
                # print(v,121)
                setattr(temp, attr, v)
            if attr == 'trip1':
                # print(v,111)
                temp.trip1_class.ericcode, temp.trip1_class.Destination, temp.trip1_class.routeno = v
            if attr == 'trip2':
                # print(v,222)
                temp.trip2_class.ericcode, temp.trip2_class.Destination, temp.trip2_class.routeno = v
            if attr in ['busstop_list1', 'busstop_list2']:
                # print(v,333)
                cls_attr = getattr(temp, f"{attr}_class")
                cls_attr.amount_of_stops, cls_attr.rtno, cls_attr.busstops = v
        return temp

    def _create_termini(self, item):
        temp = self.Termini()
        for k, v in item.items():
            if k != '_RTID':  # Skip _RTID
                setattr(temp, k.lstrip('_'), str(v) if k == '_eric' else v)
        return temp

    def _create_ddu(self, item):
        temp = self.Busstop_DDU()
        for k, v in item.items():
            attr = k.lstrip('_')
            if attr in ['Inbound_price', 'Outbound_price']:
                setattr(temp, attr, float(v[1:]))
            else:
                setattr(temp, attr, v)
        return temp

    def _create_stopreporter(self, item):
        temp = self.Busstop_Stopreporter()
        for k, v in item.items():
            attr = k.lstrip('_')
            if attr in self.stopreporter_expected_keys:
                if attr in ['Inbound_sectionfare', 'Outbound_sectionfare']:
                    try:
                        v = float(v[1:])
                    except ValueError:
                        v = 0.0
                setattr(temp, attr, v)
        return temp

