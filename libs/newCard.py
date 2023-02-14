import os
from random import randint
import sys
import shutil
import json
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg

from libs.JSON import JsonClass
from datetime import date, datetime
from pprint import pprint, pformat
from ast import literal_eval
from PIL import Image


#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()
COLORS_APP       = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/themeApp" )

EXTENTION_IMG    = ".png"

#-----------------------------------------------------------------------------------------------

class NewCards():
    def __init__(self ):
        sg.theme("Dark")
        self.data_hor = datetime.now()

       
        #-----------------------------------------------------------------------------------------------
        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)
        self.background_color   = THEME_APP_COLORS["background"]
        #--------------------
        self.path_tasks_and_img = [ "database/projects_datas/" , "database/projects_datas/tasksImages/"]
        self.title              = ""
        self.descriptions_task  = ""
        self.img_path           = ""
        self.descritons         = ""
        self.list_tags          = []
        self.tags_list          = []
        #----------- Layouts ----------------------------------------------------------------------------
       
        self.two_layouts = [                        

                            [sg.Text( "Tarefa ", 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        pad              = 0 , 
                                        background_color = self.background_color , 
                                        font             = 'Any 10'),

                            sg.Input( key = "INPUT_TITULO")  ],


                            [ sg.Text( "Nome do responsavel" , 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        pad              = 0 , 
                                        background_color = self.background_color , 
                                        font             = 'Any 10'),
                                        
                            sg.Input( key = "NAME_PERSONAL") ],

                            [self.layoutButtons( text_button = "Criar" , 
                                                key_button  = "_BUTTON_PLUS_ADD_Titulo_2",
                                                button_type = 7 ,
                                                button_size = (5 , 2) ),

                            self.layoutButtons( text_button = "Buscar imagem", 
                                                key_button  = "_BUTTON_GET_IMAGE_PATH",
                                                button_type = 2 ,
                                                button_size = (5 , 2) )],

                            [sg.Radio('', 'radio1', key='_Radio_1_',  size=(10,1) )] ,
                            [sg.Radio('Software', 'radio1', key='_Radio_2_',  size=(10,1) )] ,


                            ]


        #-------------------------------------------------------------------------------------------------------------------

        self.windons  = sg.Window( "New Card",
                                    background_color        = self.background_color,
                                    size                    = (640 , 480) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events  = True  ,
                                    use_default_focus       = False ,
                                    resizable               = False ).layout( self.two_layouts )


    def saveValuesCardsTasks( self , name_json , text_desctions , img_path_dir  ):

        data_base_values_news_cards = { name_json : [ name_json , text_desctions , img_path_dir] }


        with open( self.path_tasks_and_img[0] + str(name_json) + '.json', "w" , encoding="utf8") as js_file:
            json.dump( data_base_values_news_cards , js_file , sort_keys = False, indent = 4)
            pass

        pass

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

    def coverResize(self, image_file_name , imagen_resize ):
        with Image.open( image_file_name ) as im:
            im_resized = im.resize(  imagen_resize  )
            return im_resized 
        pass

    def update(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            

            # Criando os valore para um novo CardTask ---------------------------
            if self.events == "_BUTTON_PLUS_ADD_Titulo_2":
                self.title      = self.values["INPUT_TITULO"] 
                self.img_path   = self.values["_BUTTON_GET_IMAGE_PATH"]
                #self.descritons = self.values["MULT_DESCRIPTION"]


                data_today_card     = str(self.data_hor.day) + "/" +  str(self.data_hor.month) + "/" + str(self.data_hor.year)
                hminseg             = self.data_hor.timetuple()
                horas_min_seg       = str(hminseg[3]) + ":" + str(hminseg[4]) + ":" + str(hminseg[5]) 
                data_hor_ms         = data_today_card  + " -|- " +   horas_min_seg 


                imagem              = self.coverResize( image_file_name = self.img_path , imagen_resize = ( 80 , 80 ) )
                imagem.save( fp     = self.path_tasks_and_img[1] + str(self.title) + EXTENTION_IMG  ,  format = None)
                self.img_path       = self.path_tasks_and_img[1] + str(self.title) + EXTENTION_IMG


                self.windons.close()

                return [self.title , self.list_tags ,  self.img_path , data_hor_ms ]


#app         = NewCards()
#name_card   = app.update()