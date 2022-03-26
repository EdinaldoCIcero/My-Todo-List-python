import os
from random import randint
import sys
import shutil
from json import load
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval



#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()

COLORS_APP       = JSLOAD.json_read(name_file = "database/app_colors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/theme_app" )


#-----------------------------------------------------------------------------------------------




class App():
    def __init__(self):
        sg.theme("Reddit")

        #-----------------------------------------------------------------------------------------------
        self.trava_comands  = True
        self.buttons_sizes  = (5 , 2)
        self.background_color = THEME_APP_COLORS["background"]
        self.HEADINGS         = [ "-- Noma das Tarefas --" ] 
        self.LIST_MATRIZ      = { 
                                "TABLE_1" : [ ],
                                "TABLE_2" : [ ],
                                "TABLE_3" : [ ]
                                }



        #----------- Layouts ----------------------------------------------------------------------------
        self.one_layouts = [                        
                           
                            #self.layoutText( text_str = "Titulo Project Name" , key_element = "_TEXT_")

                            self.layoutButtons( text_button = "PLUS" , 
                                                key_button  = "_BUTTON_PLUS_ADD_T_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) ) ,
                            #

                            self.layoutButtons( text_button = "Configs" , 
                                                key_button  = "_BUTTON_CONFIGS_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) )
                            
                            ]

        #--------------------------------------------------------------------------------------------------------------------
        self.table_1    = [ self.tabelas( list_heanding = self.HEADINGS  , list_values_table = self.LIST_MATRIZ["TABLE_1"] , key = "_TABLE_1_") ]
        self.button_1   = [ self.layoutButtons( text_button = "Passar_1" , 
                                                key_button  = "_BUTTON_1_" , 
                                                button_type = 7 , 
                                                button_size = (5 , 2)) ]

        self.table_2    = [  self.tabelas( list_heanding = self.HEADINGS  , list_values_table = self.LIST_MATRIZ["TABLE_2"] , key = "_TABLE_2_") ]
        self.button_2   = [ self.layoutButtons( text_button = "Passar_2" , 
                                                key_button  = "_BUTTON_2_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) ) ]

        self.table_3    = [  self.tabelas( list_heanding = self.HEADINGS  , list_values_table = self.LIST_MATRIZ["TABLE_3"] , key = "_TABLE_3_") ]



        self.full_tables = [
                            [sg.Canvas(size = ( 147 , 131 )) , sg.Canvas(size = ( 714 , 131 ))],

                            self.layoutText( text_str = "Titulo Project Name" ),
                            
                            [sg.HSeparator() ],

                            [
                                sg.Column( self.table_1     , background_color = self.background_color) ,
                                sg.Column( self.button_1    , background_color = self.background_color ) ,
                                
                                #sg.VSeparator() ,
                                sg.Column( self.table_2     , background_color = self.background_color  ),
                                sg.Column( self.button_2    , background_color = self.background_color ) ,
                                
                                #sg.VSeparator() ,
                                sg.Column( self.table_3     , background_color = self.background_color ) ,
                            ]


                           ]
        

        #--------------------------------------------------------------------------------------------------------------------
        self.full_layouts = [ 

                            [
                                sg.Column( self.one_layouts         , background_color = self.background_color ) ,
                                sg.VSeparator() ,
                                sg.Column( self.full_tables         , background_color = self.background_color  ) 
                            ],

                            ]

        #--------------------------------------------------------------------------------------------------------------------
        self.windons  = sg.Window( "My-Tod-List",
                                    background_color        = self.background_color,
                                    size                    = (1024 , 600) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = True

                                    ).layout(self.full_layouts)
    #--------------------------------------------------------------------------------------------------------------------
    def layoutText(self , text_str  , key_element = "_TEXT_"):
        texts = [sg.Text( text_str , 
                        text_color          = COLORS_APP["BRANCO_1"],
                        background_color    = self.background_color,
                        key                 = key_element 
                        )]
        return texts        

    #--------------------------------------------------------------------------------------------------------------------
    def layoutButtons(self , text_button , key_button , button_type , button_size):
        buttons = [sg.Button(   button_text           = text_button,
                                button_color         = (self.background_color, COLORS_APP["AZUL_CLARO"]) ,
                                button_type          = button_type ,
                                s                    = button_size, 
                                key                  = key_button ,
                                border_width         = 0,
                                #image_data              = base64.buttons_greens 
                                )
                    ] 

        return buttons

        pass

    #--------------------------------------------------------------------------------------------------------------------
    def tabelas( self , list_heanding , list_values_table , key ):

        tablets =   [sg.Table(
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
                        size                    = ( 10 , 8 ),
                        key                     = key,
                        right_click_menu        = [ ["Visualizar"] , "Visualizar" ],
                        pad                     = 0 ,
                        row_height              = 40,
                        col_widths              = [0 , 0, 0, 0],
                        hide_vertical_scroll    = True
                    )]

        return tablets
    
    #--------------------------------------------------------------------------------------------------------------------
    def list_files(self , path_files):
        files = path_files

        try:
            file_list = os.listdir(files)
        except:
            file_list = []

        file_names = [fileN for fileN in file_list if os.path.isfile(os.path.join(files,fileN))
        and fileN.lower().endswith((".dtsl"))] 

        return file_names
    
    #--------------------------------------------------------------------------------------------------------------------
    def deletElement(self , events , table_key , matriz_table_name , name_event ):

        if events == name_event :
            try:
                data_selected = [ self.LIST_MATRIZ[ matriz_table_name ][row] for row in self.values[ table_key ]]
                #file_dir_path = DIR_CAPS + str( data_selected[0][0] ) + EXTENSION_IMG_BOOKS

                for i in data_selected:
                    self.LIST_MATRIZ[ matriz_table_name ].remove( i )
                    

            except:
                pass
            self.windons[ table_key ].update( values = self.LIST_MATRIZ[ matriz_table_name ]  )
    
    #--------------------------------------------------------------------------------------------------------------------    
    def passList(self , events , event_name , matriz_table_name_1 , table_key_1 , matriz_table_name_2 ,  table_key_2   ):

        if events == event_name :
            try:

                data_selected = [ self.LIST_MATRIZ[ matriz_table_name_1 ][row] for row in self.values[ table_key_1 ]]


                self.LIST_MATRIZ[ matriz_table_name_2 ].append( data_selected[0])
                
                self.windons[ table_key_2 ].update( values =  self.LIST_MATRIZ[ matriz_table_name_2 ]  )

                self.deletElement(  events = events  , table_key = table_key_1  , 
                                    matriz_table_name = matriz_table_name_1 , name_event = event_name )
            
            except:
                pass

    #--------------------------------------------------------------------------------------------------------------------
    def main(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "_BUTTON_PLUS_ADD_T_":
                ran = randint( 0 , 1000)

                self.LIST_MATRIZ["TABLE_1"].append( [" meu novo nome " + str( ran )] )
                self.windons["_TABLE_1_" ].update( values =  self.LIST_MATRIZ["TABLE_1"]  )
                print( self.LIST_MATRIZ["TABLE_1"] )

            #if self.events == "_BUTTON_1_":
                
            self.passList(  events              = self.events   , event_name   = "_BUTTON_1_"  , 
                            matriz_table_name_1 = "TABLE_1"     , table_key_1  =  "_TABLE_1_"  , 
                            matriz_table_name_2 = "TABLE_2"     , table_key_2  =  "_TABLE_2_"    
                        )


            self.passList(  events              = self.events   , event_name   = "_BUTTON_2_"  , 
                            matriz_table_name_1 = "TABLE_2"     , table_key_1  =  "_TABLE_2_"  , 
                            matriz_table_name_2 = "TABLE_3"     , table_key_2  =  "_TABLE_3_"    
                        )


            self.deletElement(  events              = self.events   , table_key   = "_TABLE_1_" , 
                                matriz_table_name   = "TABLE_1"     , name_event  = "Visualizar"
                                )     

            self.deletElement(  events              = self.events   , table_key   = "_TABLE_2_" , 
                                matriz_table_name   = "TABLE_2"     , name_event  = "Visualizar"
                                )      

            self.deletElement(  events              = self.events   , table_key   = "_TABLE_3_" , 
                                matriz_table_name   = "TABLE_3"     , name_event  = "Visualizar"
                             )        





app = App()
app.main()