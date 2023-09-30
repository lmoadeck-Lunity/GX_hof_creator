#hof editing module
import json
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
        self.dist_of_dest_electronic_disps = {}
        self.valid_lines_of_addterminus = 0
        self.next_line_is_section = False
        self.commentcount = 0
        self.num_of_addterminus = 0

    def read_hof(self, section): #only for single lined sections
        with open(self.filename, 'r', encoding='utf-8') as f:
            hof = f.readlines()
            for i in hof:
                if i == f'{section}\n':
                    self.next_line_is_section = True
                elif self.next_line_is_section:
                    value = i
                    self.next_line_is_section = False
                    break
            return value.strip('\n')
    def create_list_of_dest_electronic_disps(self,stringcount_terminus,commentcount):
        list_of_dest_electronic_disps = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            hof = f.readlines()
            for i in hof:
                #print(int(int(stringcount_terminus)+1+int(commentcount)))
                self.num += 1
                # print(i.strip('\n'),self.num)
                if i == '[addterminus]\n' or i == '[addterminus_allexit]\n':
                    self.num = 0
                    self.next_line_is_section = True
                    
                    self.num_of_addterminus += 1
                if self.num == int(int(stringcount_terminus)+2+int(commentcount)) and not self.num_of_addterminus<=1:
                    self.num = 0
                    self.next_line_is_section = False
                    break
                elif self.next_line_is_section:
                    list_of_dest_electronic_disps.append(i.strip('\n'))
        return list_of_dest_electronic_disps

    def fit_addterminus_into_dictionary(self, list_of_dest_electronic_disps):
        '''
        first value = eric code
        second value = TTDATA name
        third value = busfull name
        fourth value = fourth electronic display
        fifth value = third electronic display
        sixth value = second electronic display
        seventh value = first electronic display
        eighth value = readable eric code (comment)
        any other value after 7 = comment, will not be read by omsi
        '''
        '''
        show it like this:
        {name:TTDATA_name,properties:{
            eric_code:eric_code,
            TTData_name:TTData_name,
            busfull_name:busfull_name,
            electronic_displays:{1:1,2:2,3:3,4:4},
            readable_eric_code:readable_eric_code
            }
        }
        '''
        self.num = 0
        addterminus_count = 0
        dist_of_dest_electronic_disps = {}
        for i in list_of_dest_electronic_disps:
            
            self.num += 1
            if i == '[addterminus]' or i == '[addterminus_allexit]':
                self.num = 0
                self.next_line_is_section = True
                addterminus_count += 1
                addterminus_state = i

            if self.num == 1 and self.next_line_is_section:
                eric_code = i
            elif self.num == 2 and self.next_line_is_section:
                
                entry = {}
                entry['properties'] = {}
                entry['properties']['eric_code'] = eric_code
                entry['properties']['TTData_name'] = i
                if addterminus_state == '[addterminus_allexit]':
                    entry['properties']['PassAllExit'] = True
                else:
                    entry['properties']['PassAllExit'] = False
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}'] = entry
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['name'] = i
            elif self.num == 3 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['busfull_name'] = i
            elif self.num == 4 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['electronic_displays'] = {}
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['electronic_displays'][1] = i
            elif self.num == 5 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['electronic_displays'][2] = i
            elif self.num == 6 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['electronic_displays'][3] = i
            elif self.num == 7 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['electronic_displays'][4] = i
            elif self.num == 8 and self.next_line_is_section:
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties']['readable_eric_code'] = i
            elif self.num > 8 and self.next_line_is_section:
                comment_no = self.num - 8
                dist_of_dest_electronic_disps[f'entry_{addterminus_count - 1}']['properties'][f'comment_{comment_no}'] = i
            elif self.num > 10:
                self.next_line_is_section = False
        with open(f"{self.filename}.json", "w") as outfile:
             # write the dictionary to the file
            json.dump(dist_of_dest_electronic_disps,outfile, indent = 8)
        return dist_of_dest_electronic_disps
    



hof = hof_edit('.gitignore_folder/31M_8w_2015.hof')
print(hof.read_hof('stringcount_terminus'))

#hof.create_list_of_dest_electronic_disps(hof.read_hof('addterminus'))
dest_electronic_disps = hof.create_list_of_dest_electronic_disps('6', '2')
print(hof.fit_addterminus_into_dictionary(dest_electronic_disps))





                



    
