#hof editing module

class hof_edit:
    def __init__(self, filename):
        self.filename = filename
        self.friendlyname = ''
        self.num = 0
        self.next_line_is_the_name = False
        self.next_line_is_the_servicetrip = False
        self.servicetrip_validiacy = False
        self.servicetrip = ''
        self.list_of_dest_electronic_disps = []
        self.valid_lines_of_addterminus = 0

    def read_hof(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            hof = f.readlines()
            for i in hof:
                self.num += 1
                if i == '[name]\n':
                    self.next_line_is_the_name = True
                elif self.next_line_is_the_name:
                    self.friendlyname = i
                    self.next_line_is_the_name = False
                if i == '[servicetrip]':
                    self.next_line_is_the_servicetrip = True
                elif self.next_line_is_the_servicetrip:
                    self.servicetrip = i
                    self.next_line_is_the_servicetrip = False
                
    



hof = hof_edit('0_HanoverKMB.hof')
print(hof.read_hof().strip('\n'))
                



    
