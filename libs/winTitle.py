import os
from random import randint
import sys
import shutil
from json import load
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
from JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval



#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()
COLORS_APP       = JSLOAD.json_read(name_file = "database/app_colors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/theme_app" )


#-----------------------------------------------------------------------------------------------

class WintTitle():
    def __init__(self):
        sg.theme("Reddit")

        #-----------------------------------------------------------------------------------------------
        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)
        self.background_color   = THEME_APP_COLORS["background"]
       


        #----------- Layouts ----------------------------------------------------------------------------
        self.one_layouts = [                        
                           
                            #self.layoutText( text_str = "Titulo Project Name" , key_element = "_TEXT_")
                            [sg.Input() ],
                            self.layoutButtons( text_button = "PLUS" , 
                                                key_button  = "_BUTTON_PLUS_ADD_T_",
                                                button_type = 7 ,
                                                button_size = (5 , 2) ) ,
                            #

                            
                            ]

        #--------------------------------------------------------------------------------------------------------------------
        self.windons  = sg.Window( "TITLE",
                                    background_color        = self.background_color,
                                    size                    = (400 , 140) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = False

                                    ).layout(self.one_layouts) 


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

    def update(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break





app = WintTitle()
app.update()