from pprint import pprint, pformat
from ast import literal_eval



class DTSaveLoad():
    def __init__(self):
        
        #self.path = bge.logic.expandPath("//dts/")
        self.path = "dts/"
        self.data_type = ".dtsl"
        
        
    def Save(self , name_data_save , dict_datas):
        self.datas = dict_datas
        
        with open( self.path + str(name_data_save) + self.data_type , 'w' ) as openedfile:
            openedfile.write( pformat( self.datas ) )
            
            
    def Load(self , name_data_load):
        
        with open( self.path + str(name_data_load) + self.data_type , 'r' ) as openedfile:
            load_data = openedfile.read()
            load_data = literal_eval( load_data ) 
       
       
        return load_data
    

    