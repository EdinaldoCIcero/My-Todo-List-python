import os
import sys
import shutil
from json import load
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval



#-----------------------------------------------------------------------------------------------
JSLOAD      = JsonClass()

COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )

HEADINGS    = ["Noma das Tarefas"]

LIST_MATRIZ = [  ]
#-----------------------------------------------------------------------------------------------

for i in range(20):
    LIST_MATRIZ.append( [("tarefa_" + str(i) ) , "2:86" ] )




class App():
    def __init__(self):
        sg.theme("Reddit")

        #-----------------------------------------------------------------------------------------------
        
        self.trava_comands  = True
        self.buttons_sizes  = (5 , 2)

        #----------- Layouts ----------------------------------------------------------------------------
        self.one_layouts = [                        
                           
                            [sg.Text("Nome file ", 
                                                text_color          = 'white',
                                                background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                                key                 = "_TEXT_01_" 
                                                )],

                            self.layoutButtons(   text_button = "PLUS" , 
                                                    key_button  = "_BUTTON_PLUS_ADD_T_",
                                                    button_type = 7 ,
                                                    button_size = (5 , 2) ) 

                            
                            ]

        #--------------------------------------------------------------------------------------------------------------------
        self.table_1    = [ self.tabelas( list_heanding = HEADINGS  , list_values_table = LIST_MATRIZ , key = "_TABLE_1_") ]
        self.button_1   = [ self.layoutButtons( text_button = "Passar_1" , 
                                                key_button  = "_BUTTON_1_" , 
                                                button_type = 7 , 
                                                button_size = (5 , 2)) ]

        self.table_2    = [  self.tabelas( list_heanding = HEADINGS  , list_values_table = LIST_MATRIZ , key = "_TABLE_2_") ]
        self.button_2   = [ self.layoutButtons( text_button = "Passar_2" , 
                                                key_button  = "_BUTTON_2_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) ) ]

        self.table_3    = [  self.tabelas( list_heanding = HEADINGS  , list_values_table = LIST_MATRIZ , key = "_TABLE_3_") ]



        self.full_tables = [
                            [
                                sg.Column( self.table_1     , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                                sg.Column( self.button_1    , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                                
                                #sg.VSeparator() ,
                                sg.Column( self.table_2     , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"]  ),
                                sg.Column( self.button_2    , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                                
                                #sg.VSeparator() ,
                                sg.Column( self.table_3     , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                            ]


                           ]
        

        #--------------------------------------------------------------------------------------------------------------------
        self.full_layouts = [ 

                            [
                                sg.Column( self.one_layouts         , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                                sg.VSeparator() ,
                                sg.Column( self.full_tables         , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"]  ) 
                            ],

                            ]

        #--------------------------------------------------------------------------------------------------------------------
        self.windons  = sg.Window( "My-Tod-List",
                                    background_color        = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                    size                    = (1024 , 600) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = True

                                    ).layout(self.full_layouts)


    #--------------------------------------------------------------------------------------------------------------------
    def layoutButtons(self , text_button , key_button , button_type , button_size):
        buttons = [sg.Button(   button_text           = text_button,
                                button_color         = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                button_type          = button_type ,
                                s                    = button_size, 
                                key                  = key_button ,
                                border_width         = 0,
                                #image_data              = base64.buttons_greens 
                                )
                    ] 

        return buttons

        pass

    def tabelas( self , list_heanding , list_values_table , key ):

        tablets =   [sg.Table(
                        values                  = list_values_table, 
                        headings                = list_heanding,
                        select_mode             = sg.TABLE_SELECT_MODE_BROWSE,
                        change_submits          = False,
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
                        size                    = ( 4 , 8 ),
                        key                     = key,
                        right_click_menu        = [ ["Visualizar"] , "Visualizar" ],
                        pad                     = 0 ,
                        row_height              = 40,
                        col_widths              = [22, 22, 22, 22],
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
    def main(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

        pass








app = App()
app.main()