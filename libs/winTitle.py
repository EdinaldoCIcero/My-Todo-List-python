import os
from random import randint
import sys
import shutil
import json
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval
from PIL import Image
from datetime import date, datetime

#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()
COLORS_APP       = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/themeApp" )

#-----------------------------------------------------------------------------------------------

class WintTitle():
    def __init__(self ):
        sg.theme("Dark")

        #-----------------------------------------------------------------------------------------------
        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)
        self.background_color   = THEME_APP_COLORS["background"]
        #--------------------
        self.title              = ""
        self.descriptions_task  = ""
        self.img_path           = ""
        self.descritons         = ""
        #----------- Layouts ----------------------------------------------------------------------------
        self.one_layouts = [                        
                           
                            #self.layoutText( text_str = "Titulo Project Name" , key_element = "_TEXT_")
                            [sg.Input(key = "INPUT_TITULO_1") ],
                            [self.layoutButtons( text_button = "PLUS" , 
                                                key_button  = "_BUTTON_PLUS_ADD_Titulo_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) )] ,

                            ]


        #-------------------------------------------------------------------------------------------------------------------
        layouts_dicts = {   "LAYOUT_APP_INIT_PROJECTS_LIST" : [] , "LAYOUT_APP_TABLES_TASKS" : []  }

        self.windons  = sg.Window( "Projwct Name",
                                    background_color        = self.background_color,
                                    size                    = ( 340 , 100) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = False

                                    ).layout( self.one_layouts )

    #---------------------------------------------------------------------------------------------

    def layoutButtons(self , text_button , key_button , button_type , button_size):
        buttons = sg.Button(   button_text           = text_button,
                                button_color         = (self.background_color, COLORS_APP["AZUL_CLARO"]) ,
                                button_type          = button_type ,
                                s                    = button_size, 
                                key                  = key_button ,
                                border_width         = 0,
                                #image_data              = base64.buttons_greens 
                                )
                     

        return buttons
    #---------------------------------------------------------------------------------------------

    def coverResize(self, image_file_name , imagen_resize ):
        
        with Image.open( image_file_name ) as im:
            im_resized = im.resize(  imagen_resize  )

            return im_resized 
        pass
    #---------------------------------------------------------------------------------------------
    def update(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            
            # WIND INIT PROJETOS 
            if self.events == "_BUTTON_PLUS_ADD_Titulo_":
                self.title  = self.values["INPUT_TITULO_1"]
                
                self.windons.close()

                
        return self.title


#app = WintTitle()
#app.update()