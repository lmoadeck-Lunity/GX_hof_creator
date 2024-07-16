from string import Template
from types import SimpleNamespace
class ericcode:
    mapping = {'a': 11, 'b': 12, 'c':13,'d':21,'e':22,'f':23,'g':31,'h':32,'i':33,'j':41,'k':42,'l':43,'m':51,'n':52,'o':53,'p':61,'q':62,'r':63,'s':71,'t':72,'u':73,'v':81,'w':82,'x':83,'y':91,'z':92,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def retstr(self) -> str:
        returnstring = ''.join(self.eric)
        if len(returnstring) < 6:
            returnstring = returnstring + '0'
        return returnstring
    def __init__(self, code: str) -> None:
        self.eric = map(str,[self.mapping[c] for c in code.lower()])
    def __len__(self) -> int:
        return len(''.join(self.eric))
    def __str__(self) -> str:
        returnstring = ''.join(self.eric)
        if len(returnstring) < 6:
            returnstring = returnstring + '0'
        return returnstring
    def __int__(self) -> int:
        return int(str(self.retstr()))


class HOF:
    name = 'Default'
    servicetrip = 'Not In Service'
    ddu = []
    stopreporter = []
    termini = []
    infosystem = []
    
    def __init__(self,name:str='Default',servicetrip:str='Not In Service') -> None:
        self.name = name
        self.servicetrip = servicetrip
        self.template = Template('''------------------------------------------
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


    class Termini:
        def __init__(self,allexit:bool = False, eric: int = 0, destination: str = '', busfull: str = '', flip: list[str] = [], RTID: str = '') -> None: #flip is a list of strings, eric will be inputted as '289XZ' and converted to 2899192
            self.template = Template('''[addterminus$allexit]
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
            return self.template.substitute(allexit=self._allexit, eric=self._eric, destination=self._destination, busfull=self._busfull, pai_page4 = self._flup4, pai_page3 = self._flup3, pai_page2 = self._flup2,pai_page1 = self._flup1,RTID=self._RTID)

    class Busstop_Stopreporter:
        def __init__(self, name:str = '',EngDisplay:str = '',ChiSeconds:int = 0,EngSeconds:int = 0,Outbound_sectionfare:float = 0.0,Inbound_sectionfare:float = 0.0) -> None:
            self.template = Template('''[addbusstop]
$name
$EngDisplay
$ChiSeconds $EngSeconds
$Outbound_sectionfare
$Inbound_sectionfare
.........................
                                    ''')
            self._name = name
            self._EngDisplay = EngDisplay
            self._ChiSeconds = str(ChiSeconds).rjust(2,'0')
            self._EngSeconds = str(EngSeconds).rjust(2,'0')
            self._Outbound_sectionfare = f"${Outbound_sectionfare:.1f}" if Outbound_sectionfare != 0.0 else name
            self._Inbound_sectionfare = f"${Inbound_sectionfare:.1f}" if Inbound_sectionfare != 0.0 else name
            self._Autoskip = False
            self._pages = 1
            self._engscroll = self._EngDisplay.count('@') // 2

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
            return self.template.substitute(name=self._name, EngDisplay=self._EngDisplay, ChiSeconds=self._ChiSeconds, EngSeconds=self._EngSeconds, Outbound_sectionfare=self._Outbound_sectionfare, Inbound_sectionfare=self._Inbound_sectionfare)
        
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
        
    class Busstop_DDU:
        def __init__(self, RTNO:str = '',Outbound_dir:str = '',Inbound_dir:str = '',Outbound_price:float = 0.0,Inbound_price:float = 0.0,sectiontimes_Y:int = 0,sectiontimes_Z:int = 0) -> None:
            self.template = Template('''[addbusstop]
$RTNO
$Outbound_dir \t\t$sectiontimes_Y
$Inbound_dir \t\t$sectiontimes_Z
$Outbound_price
$Inbound_price
.........................
                                    ''')
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
            return self.template.substitute(RTNO=self._RTNO, Outbound_dir=self._Outbound_dir, Inbound_dir=self._Inbound_dir, Outbound_price=self._Outbound_price, Inbound_price=self._Inbound_price, sectiontimes_Y=self._sectiontimes_Y, sectiontimes_Z=self._sectiontimes_Z)
        
    class Infosystem:
        '''
        Modifications of the Infosystem class will be made for enforcing the correct format of infosystems
        (infosystem_trip and infosystem_busstop_list needs to be in a pair for the correct format, and both needs to be in a pair for GPSHoilun to read the hof correctly)
        '''
        
        class trip:
            def __init__(self,eric:str =  '',Destination:str = '',RouteNo:str = '') -> None:
                self.template = Template('''[infosystem_trip]
$ericcode
$Destination
$ericcode
$routenoanddir
                                ''')
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
                self._routeno = f"{value} {self._Destination}"
            def __str__(self) -> str:
                return self.template.substitute(ericcode=self._ericcode, Destination=self._Destination, routenoanddir=f"{self._routeno} {self._Destination} ")
        class busstop_list:
            def __init__(self,bus_stops:list[str] = [],rtno:str = '') -> None:
                self.template = Template('''[infosystem_busstop_list]
$amount_of_stops
$rtno
$busstops
                                ''')
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
                return self.template.substitute(amount_of_stops=self._amount_of_stops, rtno=self._rtno, busstops=self.busstops)
    
        def __init__(self,single_or_dual_dir:bool,route:str='',dir1:str='',dir2:str='',bustoplist1:list[str]=[],bustoplist2:list[str]=[]) -> None: 
            #route must be inputted as '289X', we will automaticllu add Y and Z at the end
            #single_or_dual_dir with True being dual direction and False being single direction
            if single_or_dual_dir:
                self.infosystem_busroute_dualdirections = [
                    self.trip(f'{route}Y',dir1,route),
                    self.busstop_list(bustoplist1,f'{route}'),
                    self.trip(f'{route}Z',dir2,route),
                    self.busstop_list(bustoplist2,f'{route}')]
            else:
                self.infosystem_busroute_singledirection = [
                    self.trip(route,dir1,route),
                    self.busstop_list(bustoplist1,route),
                    self.trip(route,dir1,route),
                    self.busstop_list(bustoplist1,route)
                    ]
                    
        def __str__(self) -> str:
            return '\n'.join([str(i) for i in self.infosystem_busroute_dualdirections]) if hasattr(self, 'infosystem_busroute_dualdirections') else '\n'.join([str(i) for i in self.infosystem_busroute_singledirection])
        

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
        returnstring = '\n'.join([''.join(self.template.substitute(name = self.name,servicetrip = self.servicetrip)),'\n'.join((str(i) for i in self.termini)),'\n'.join(str(i) for i in self.ddu),'\n'.join((str(i) for i in self.stopreporter)),'\n'.join((str(i) for i in self.infosystem))])
        return returnstring