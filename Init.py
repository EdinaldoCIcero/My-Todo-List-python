import os
from random import randint
import sys
import shutil
import json
from tkinter.constants import SEL, TRUE
from traceback import print_tb
import PySimpleGUI as sg
from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import Pass, literal_eval
from libs.winTitle import WintTitle
from main import AppMain

from datetime import date, datetime




#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()

COLORS_APP       = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/themeApp" )
PROJECT_NAME     = JSLOAD.json_read(name_file = "database/projectName" )



#-----------------------------------------------------------------------------------------------
class WindInitApp():
    def __init__(self ):
        sg.theme("Reddit")

        #-----------------------------------------------------------------------------------------------
        #self.data_hor = datetime.now()

        self.trava_comands      = True
        self.buttons_sizes      = (10 , 2)
        self.background_color   = THEME_APP_COLORS["background"]
        self.list_name_append        = [""]

        self.HEADINGS           = [ " "*10 , "DATA" ]
        
        self.dict_name_project  = {  "NAME_PR" : PROJECT_NAME["NAME_PR"]  }

        #print( self.data_selected )


        self.LIST_MATRIZ        = {
                                    "IMGS" : { 
                                               "IMG_COVER_1" : "",
                                               "IMG_COVER_2" : "",
                                             },
                                    
                                    "TABLES_" :{
                                            "TABLE_1" : [ ],
                                            "TABLE_2" : [ ],
                                            "TABLE_3" : [ ],
                                            "TABLE_4" : [ ]
                                            }
                                }
        

        #----------- Layouts ----------------------------------------------------------------------------
        self.one_layouts = [                        
                            #self.layoutText( text_str = "Titulo Project Name" , key_element = "_TEXT_")
                            #[sg.Input(key = "INPUT_TITULO") ],

                            [self.layoutButtons( text_button = "Abrir projeto" , 
                                                key_button  = "_BUTTON_OPEN_PROJECT_",
                                                button_type = 7 ,
                                                button_size = self.buttons_sizes ),

                            self.layoutButtons( text_button = "Novo projeto" , 
                                                key_button  = "_BUTTON_NEW_PROJECT_DATA_",
                                                button_type = 7 ,
                                                button_size = self.buttons_sizes )
                            ],

                            [ self.tabelas( list_heanding = self.HEADINGS  , 
                                            list_values_table =  PROJECT_NAME["NAME_PR"]  , 
                                            key = "_TABLE_PROJECTS_") ]

                            ]


        #--------------------------------------------------------------------------------------------------------------------
        self.windons  = sg.Window( "PROJECT_GAMES_DEVELOPMENT_PROGRESSEC...",
                                    background_color        = self.background_color,
                                    size                    = (640 , 480) ,
                                    #icon                   = "Icon.ico",
                                    #titlebar_icon          = base64.icone , 
                                    #use_custom_titlebar    = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = False

                                    ).layout(self.one_layouts)

    #-------------------------------------------------------------------------------------------------------------------------
    def tabelas( self , list_heanding , list_values_table , key ):
        
        tablets = [sg.Table(
                        values                  = list_values_table, 
                        headings                = list_heanding,
                        select_mode             = sg.TABLE_SELECT_MODE_BROWSE,
                        #change_submits          = False,
                        justification           = 'center',
                        text_color              = COLORS_APP["SINZA_CLARO_1"],
                        background_color        = COLORS_APP["BRANCO_2"],
                        selected_row_colors     = (COLORS_APP["BRANCO_1"] , COLORS_APP["VERDE_CLARO"] ),
                        header_background_color = COLORS_APP["AZUL_CLARO"],
                        
                        enable_events           = True,
                        enable_click_events     = True,
                        bind_return_key         = True,
                        alternating_row_color   = COLORS_APP["LARANJA"],
                        expand_x                = True,
                        expand_y                = True,

                        size                    = ( 5 , 8 ),
                        key                     = key,
                        right_click_menu        = [ "menu" , ["Abrir" , "Excluir"] ],
                        pad                     = 0 ,
                        row_height              = 40,
                        col_widths              = [0 , 0, 0, 0],
                        hide_vertical_scroll    = True
                    )]

        return tablets

    #-------------------------------------------------------------------------------------------------------------------------
    def layoutButtons(self , text_button , key_button , button_type , button_size  ):
        
        buttons  = sg.Button(  button_text           = text_button,
                                button_color         = (self.background_color, COLORS_APP["AZUL_CLARO"]) ,
                                button_type          = button_type ,
                                s                    = button_size, 
                                key                  = key_button ,
                                border_width         = 0,
                                #image_data              = base64.buttons_greens 
                    )

        return buttons

        pass
   
    #-------------------------------------------------------------------------------------------------------------------------
    def saveValuesProject( self , events):
        
        if events == "_BUTTON_NEW_PROJECT_DATA_":
            data_hor = datetime.now()
            #-----------------------
            app     = WintTitle()
            name    = app.update()
            #-----------------------
            
            if name != "":
                self.dict_name_project["NAME_PR"].append( [name , str( data_hor ) ] )
                #self.dict_name_project["NAME_PR"].append( [name] )
                
                
                with open( "database/" + "projectName.json" , "w" , encoding="utf8") as js_file:
                    json.dump( self.dict_name_project , js_file , sort_keys = False, indent = 4)
                    pass

                with open( "database/projects_datas/" + name + ".json" , "w" , encoding="utf8") as js_file:
                    json.dump( self.LIST_MATRIZ , js_file , sort_keys = False, indent = 4)
                    pass
                
                
                PROJECTS = JSLOAD.json_read(name_file = "database/projectName" )
                #self.dict_name_project["NAME_PR"].append( PROJECTS["NAME_PR"] )

                self.windons["_TABLE_PROJECTS_"].update( values = PROJECTS["NAME_PR"]  )

                
        pass
    
    #-------------------------------------------------------------------------------------------------------------------------
    def saveProj(self , name_project ):

        with open( "database/projects_datas/" + name_project + ".json" , "w" , encoding="utf8") as js_file:
            json.dump( self.dict_name_project , js_file , sort_keys = False, indent = 4)
            pass
            
            
        PROJECTS = JSLOAD.json_read(name_file = "database/projectName" )
        #self.dict_name_project["NAME_PR"].append( PROJECTS["NAME_PR"] )

        self.windons["_TABLE_PROJECTS_"].update( values = PROJECTS["NAME_PR"]  )
        
    #-------------------------------------------------------------------------------------------------------------------------
    def selectElementTable(self , events, name_event ):
        
        if events == name_event :
           try:
               table_selected_name = [ self.dict_name_project["NAME_PR"][row] for row in self.values["_TABLE_PROJECTS_"] ][0][0]
               self.list_name_append.append( table_selected_name )
               #print(x)

           except:
            #print('An exception occurred')
            pass

        return self.list_name_append[-1] 
    
    #-------------------------------------------------------------------------------------------------------------------------
    def deletElement(self , events , table_key , matriz_table_name , name_event ):
        

        if events == name_event :
            try:
                data_selected = [ self.dict_name_project["NAME_PR"][row] for row in self.values[ table_key ]]
                

                for i in data_selected:
                    self.dict_name_project["NAME_PR"].remove( i )
                    
                    project_n =  "database/projects_datas/" + i[0] + ".json"

                    with open( "database/" + "projectName.json" , "w" , encoding="utf8") as js_file:
                        json.dump( self.dict_name_project , js_file , sort_keys = False, indent = 4)
                        pass

                    os.remove( project_n )

            except TypeError as e :
                #print(" Erro em codigo ---> " , e )
                pass

            self.windons[ table_key ].update( values = self.dict_name_project["NAME_PR"]  )

    #-------------------------------------------------------------------------------------------------------------------------
    def update(self):
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            
            try:
                self.deletElement( events  = self.events , table_key = "_TABLE_PROJECTS_" , matriz_table_name = ""  , name_event = "Excluir" )
                get_table_name_selected = self.selectElementTable(events = self.events , name_event = "_TABLE_PROJECTS_"  )
                self.saveValuesProject( events = self.events )

                if self.events == "_BUTTON_OPEN_PROJECT_" and get_table_name_selected != "":
                    app = AppMain( project_name = str( get_table_name_selected ))
                    app.main()
                    pass

                elif self.events == "Abrir" :
                    app = AppMain( project_name = str( get_table_name_selected ))
                    app.main()
                    pass


                else:
                    #print("Nenhum projeto selecionado")  # Adicionar telinha PopUp #  
                    pass

            except TypeError as e :
                #print(" Erro em codigo ---> " , e )
                pass
            


#-------------------------------------------------------------------------------------------------------------------------
app = WindInitApp()
app.update()