from string import Template
from types import SimpleNamespace
class HOF:
    name = 'Default'
    servicetrip = 'Not In Service'
    def __init__(self,name:str='Default',servicetrip:str='Not In Service') -> None:
        self.name = name
        self.servicetrip = servicetrip
    class ericcode:
        mapping = {'a': 11, 'b': 12, 'c':13,'d':21,'e':22,'f':23,'g':31,'h':32,'i':33,'j':41,'k':42,'l':43,'m':51,'n':52,'o':53,'p':61,'q':62,'r':63,'s':71,'t':72,'u':73,'v':81,'w':82,'x':83,'y':91,'z':92,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        def __init__(self, code: str) -> None:
            self.eric = map(str,[self.mapping[c] for c in code])
        def __len__(self) -> int:
            return len(''.join(self.eric))
        def __str__(self) -> str:
            returnstring = ''.join(self.eric)
            if len(returnstring) < 6:
                returnstring = returnstring + '0'
            return returnstring


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
            self._eric = str(HOF.ericcode(value))
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
        @property
        def allexit(self) -> str:
            return self._allexit
        @allexit.setter
        def allexit(self, value: bool) -> None:
            self._allexit = '_allexit' if value else ''
        
        
        def __str__(self) -> str:
            return self.template.substitute(allexit=self._allexit, eric=self._eric, destination=self._destination, busfull=self._busfull, flip=self._flip, RTID=self._RTID)

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
            self._Outbound_sectionfare = f"${Outbound_sectionfare:.1f}"
            self._Inbound_sectionfare = f"${Inbound_sectionfare:.1f}"
        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, value: str) -> None:
            self._name = value

        @property
        def EngDisplay(self) -> str:
            return self._EngDisplay

        @EngDisplay.setter
        def EngDisplay(self, value: str) -> None:
            self._EngDisplay = value

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
            self._Outbound_sectionfare = f"${value:.1f}"

        @property
        def Inbound_sectionfare(self) -> float:
            return float(self._Inbound_sectionfare.strip('$'))

        @Inbound_sectionfare.setter
        def Inbound_sectionfare(self, value: float) -> None:
            self._Inbound_sectionfare = f"${value:.1f}"
        def __str__(self) -> str:
            return self.template.substitute(name=self._name, EngDisplay=self._EngDisplay, ChiSeconds=self._ChiSeconds, EngSeconds=self._EngSeconds, Outbound_sectionfare=self._Outbound_sectionfare, Inbound_sectionfare=self._Inbound_sectionfare)
        
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
        class trip:
            def __init__(self,eric:str =  '',Destination:str = '',RouteNo:str = '') -> None:
                self.template = Template('''[infosystem_trip]
                            $ericcode
                            $Destination
                            $ericcode
                            $routenoanddir
                                ''')
                self._ericcode = str(HOF.ericcode(eric))
                self._Destination = Destination
                self._routeno = RouteNo
            @property
            def ericcode(self) -> str:
                return str(self._ericcode)
            @ericcode.setter
            def ericcode(self, value: str) -> None:
                self._ericcode = str(HOF.ericcode(value))
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
                return self.template.substitute(ericcode=self._ericcode, Destination=self._Destination, routenoanddir=self._routeno)
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


    
