import os
from pickle import FALSE
from random import randint
from re import T
import sys
import shutil
import json
from tkinter.constants import SEL, TRUE
from tkinter.tix import Tree

import PySimpleGUI as sg

from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval
from PIL import Image


from libs.newCard import NewCards
from datetime import date, datetime
import elemtens_base64 as bs4

#-----------------------------------------------------------------------------------------------
JSLOAD              = JsonClass()
COLORS_APP          = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS    = JSLOAD.json_read(name_file = "database/themeApp" )

THEMES_APP          = JSLOAD.json_read(name_file = "database/theme" )

TEXTS_TITTLES_COLL_PAD_SIZE = ( 60 , 1)
#-----------------------------------------------------------------------------------------------

class AppLayout():
    def __init__(self , project_name ):
        sg.theme("Dark")
        

        #----------- COLORS THEME UI ELEMENTS ----------------------------------------------------------
        self.theme_mode         = "Dark"

        self.background_color               = THEMES_APP[ self.theme_mode ]["background_general"]
        self.background_colunns_color       = THEMES_APP[ self.theme_mode ]["background_coluns_list_cards"] 

        self.background_cardtask_color      = THEMES_APP[ self.theme_mode ]["background_cards_task"]
        self.titlle_texts_cardtask_color    = THEMES_APP[ self.theme_mode ]["text_tittle_cards_task"]
        self.texts_cardtask_color           = THEMES_APP[ self.theme_mode ]["texts_cards_task"]
        self.lines_cardtask_color           = THEMES_APP[ self.theme_mode ]["line_card_task"]
        self.buttons_cardtask_color         = THEMES_APP[ self.theme_mode ]["buttons_cards_task"]





        # atributos e variaveeis -----------------------------------------------------------------------
        self.data_hor = datetime.now()

        self.name_proj           = project_name
        self.path_tasks_and_img  = [ "database/projects_datas/" , "database/projects_datas/tasksImages/" ]
        self.path_datasbase_cols = "database/projects_datas/" + self.name_proj 
        self.CARDS_DATAS_LOADS   = JSLOAD.json_read( name_file = "database/projects_datas/" + self.name_proj  )

        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)

        self.colunns_keys       = [ "COL_0" , "COL_1" , "COL_2" , "COL_3"]

        self.index              = 0 
        self.index_col          = 0
        self.col_lists_size     = ( 300 , 300 )
        self.list_load_data_cards = self.CARDS_DATAS_LOADS

        #print( self.list_load_data_cards )

        #---------- Demostração do DAtabase de cada projeto o que é salvo e carregado no momento !--------------------------------
        self.database_basic     = {  "Coluna_1" : [ "Nome do cardTastks " , "descrtion" , "path_img" , "data / hora "] } 

        #------ Base do DataBase -------------------------------------------------------
        self.card_lists         = {
                                    self.colunns_keys[0] : [ [ self.layoutButtons( text_button = "+" , key_button  = "_ADD_", 
                                                                button_type = 7   , button_size = ( 38 , 2) )] ] ,
                                    self.colunns_keys[1] : [ ] ,
                                    self.colunns_keys[2] : [ ] ,
                                    self.colunns_keys[3] : [ ] 
                                  }

        #-----------------------------------------------------------------------------------------------
        # -------- CARREGANDO OS VALORES DO DATABASE -------------------------------------------------------------
        for index_list_col1 , list_values_col1 in enumerate( self.list_load_data_cards[ self.colunns_keys[0] ] ):
            card_news_col_0 = self.loadCardsCols(list_load_values = list_values_col1 , col_key_name = self.colunns_keys[0]  )
            self.card_lists[ self.colunns_keys[0] ].append( card_news_col_0[0] )
           

        for index_list_col2 , list_values_col2 in enumerate( self.list_load_data_cards[ self.colunns_keys[1] ] ):
            card_news_col_1 = self.loadCardsCols(list_load_values = list_values_col2 , col_key_name = self.colunns_keys[1]  )
            self.card_lists[ self.colunns_keys[1] ].append( card_news_col_1[0] )
          
        for index_list_col3 , list_values_col3 in enumerate( self.list_load_data_cards[ self.colunns_keys[2] ] ):
            card_news_col_2 = self.loadCardsCols(list_load_values = list_values_col3 , col_key_name = self.colunns_keys[2]  )
            self.card_lists[ self.colunns_keys[2 ] ].append( card_news_col_2[0] )
        

        for index_list_col4 , list_values_col4 in enumerate( self.list_load_data_cards[ self.colunns_keys[3] ] ):
            card_news_col_3 = self.loadCardsCols(list_load_values = list_values_col4 , col_key_name = self.colunns_keys[3]  )
            self.card_lists[ self.colunns_keys[3] ].append( card_news_col_3[0] )


        #----------- Layouts ----------------------------------------------------------------------------

        self.button_lay  = [ ]


        self.coll_1      = [

                            [sg.Column( [[sg.Text("  Fazer"         , 
                                                    text_color       = COLORS_APP["BRANCO_1"] , 
                                                    background_color = self.background_colunns_color[1] , 
                                                    justification    ='c',
                                                    pad              = TEXTS_TITTLES_COLL_PAD_SIZE , 
                                                    font             = 'Any 20' ) ]] ,  background_color      = self.background_colunns_color[1],
                                                                                        element_justification = "center",
                                                                                        expand_x              = True )],
                            [
                                sg.Column(  self.card_lists[ self.colunns_keys[0] ] ,
                                        background_color        = self.background_color ,#self.background_colunns_color[0], 
                                        size                    = self.col_lists_size,
                                        scrollable              = True , 
                                        vertical_scroll_only    = True, 
                                        expand_x                = True , 
                                        expand_y                = True,
                                        #justification          = "center" ,
                                        element_justification   = "left",
                                        vertical_alignment      = "center", 
                                        pad                     = 0 , 
                                        key                     = self.colunns_keys[0]) ] ,

                                

                                ]


        self.coll_2      = [
                            [sg.Column( [[sg.Text("  Fazendo"         , 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        background_color = self.background_colunns_color[2] , 
                                        justification    ='c',
                                        pad              = TEXTS_TITTLES_COLL_PAD_SIZE , 
                                        font             = 'Any 20' )]] ,   background_color = self.background_colunns_color[2] ,
                                                                            element_justification = "center" ,
                                                                            expand_x              = True ) ],
                            [
                               sg.Column(   self.card_lists[ self.colunns_keys[1] ],
                                        background_color        = self.background_colunns_color[0], 
                                        size                    = self.col_lists_size,
                                        scrollable              = True, 
                                        vertical_scroll_only    = True, 
                                        expand_x                = True, 
                                        expand_y                = True,
                                        element_justification   = "left",
                                        vertical_alignment      = "center",
                                        pad                     = 0    , 
                                        key                     = self.colunns_keys[1] )]
                           ]
        

        self.coll_3      = [
                            [sg.Column( [[sg.Text("  Aprovados"         , 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        background_color = self.background_colunns_color[3] , 
                                        justification    ='c',
                                        pad              = TEXTS_TITTLES_COLL_PAD_SIZE , 
                                        font             = 'Any 20' )]] , background_color = self.background_colunns_color[3]  , 
                                                                          element_justification = "center",
                                                                          expand_x              = True  )] ,
                            [
                              sg.Column(   self.card_lists[ self.colunns_keys[2] ] ,
                                        background_color        = self.background_colunns_color[0],
                                        size                    = self.col_lists_size,
                                        scrollable              = True, 
                                        vertical_scroll_only    = True, 
                                        expand_x                = True, 
                                        expand_y                = True,
                                        element_justification   = "left",
                                        vertical_alignment      = "center", 
                                        pad                     = 0   ,
                                        key                     = self.colunns_keys[2] ) ]
                           ]


        self.coll_4      = [
                            [sg.Column( [[sg.Text("Finalizados", 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        background_color = self.background_colunns_color[4] , 
                                        justification    ='c',
                                        pad              = TEXTS_TITTLES_COLL_PAD_SIZE, 
                                        font             = 'Any 20' )]] , background_color = self.background_colunns_color[4]  , 
                                                                          element_justification = "center",
                                                                          expand_x              = True  )] ,
                            [
                               sg.Column(   self.card_lists[ self.colunns_keys[3] ] ,
                                        background_color        = self.background_colunns_color[0],
                                        size                    = self.col_lists_size,
                                        scrollable              = True, 
                                        vertical_scroll_only    = True, 
                                        expand_x                = True, 
                                        expand_y                = True,
                                        element_justification   = "left",
                                        vertical_alignment      = "center", 
                                        pad                     = 0 , 
                                        key                     = self.colunns_keys[3] ) ]
                           ]


        self.layouts_col = [
                            [sg.Column( self.coll_1  , background_color = self.background_colunns_color[0]  , element_justification = "center", pad = 0 , expand_x = True , expand_y = True  ) ,
                             sg.Column( self.coll_2  , background_color = self.background_colunns_color[0]  , element_justification = "center", pad = 0 , expand_x = True , expand_y = True  ) ,
                             sg.Column( self.coll_3  , background_color = self.background_colunns_color[0]  , element_justification = "center", pad = 0 , expand_x = True , expand_y = True  ) ,
                             sg.Column( self.coll_4  , background_color = self.background_colunns_color[0]  , element_justification = "center", pad = 0 , expand_x = True , expand_y = True  ) ]
                            ]


        #-------- FLL LAYOUTS -----------------------
       

        self.Full_layouts = [
                            

                            [sg.Text(    text             = project_name , 
                                        text_color       = COLORS_APP["BRANCO_1"] , 
                                        background_color = self.background_color , 
                                        justification    ='c',
                                        pad              = TEXTS_TITTLES_COLL_PAD_SIZE, 
                                        font             = 'fonts/ubuntu-bold-italic.ttf' )
                            ],
                            


                            [
                            #sg.Column( self.button_lay   , background_color = self.background_color            , pad = 8  , size = (11 , 0 ) , expand_x = True , expand_y = True  ),
                            sg.Column( self.layouts_col  , 
                                                background_color = self.background_colunns_color[0] ,
                                                justification    = 'c', pad = 0  , expand_x = True , expand_y = True  ) ]
                            ]


        #---------- JANELA_ -----------------------------------------------
        self.windons =  sg.Window( "TITLE",
                            background_color        = self.background_color,
                            size                    = (1024 , 600) ,
                            #icon                   = "Icon.ico",
                            #titlebar_icon          = base64.icone , 
                            #use_custom_titlebar    = False ,
                            return_keyboard_events  = True,
                            resizable               = True,
                            finalize                = True,
                            #transparent_color       = self.background_color ,
                            element_justification   = "Left",
                            
                            ).layout( self.Full_layouts  )
        


    #------ MEDOTOS DO APP ---------------------------------------------------------------------------------------------------
    def loadCardsCols(self , list_load_values , col_key_name  ):

        card_make   = self.newCardTask( col_name        = col_key_name , 
                                        title_card      = list_load_values[0] , 
                                        img_card        = list_load_values[2] , 
                                        tags_cards      = list_load_values[1] ,
                                        data_card       = list_load_values[3]
                                        )

        return card_make

    def newCardTask(self  , col_name  , title_card , img_card , tags_cards , data_card ):
        global index
        colunn_name     = col_name
        self.index      += 1
        back_color      = self.background_cardtask_color


        # -------------------------------------------------------------------------------------------
        # Gerar a lista de imagens das tags escolhidas 





        lay_imagem   = [ [sg.Image( img_card , pad = 0 , size=( 71 , 60 ), key="IMG_") ] ]
                       


        layout_texts = [
                        [sg.Text("Nome :" , text_color = self.texts_cardtask_color , 
                                    pad = 0 , 
                                    background_color = back_color , expand_x = False , font ='Any 10' , key= "_NOME_P" ) ], #  , sg.Push(background_color = back_color ) 
                        
                        [sg.Text("Data/H:" + data_card , text_color = self.texts_cardtask_color , 
                                    pad = 0 , 
                                    background_color = back_color , expand_x = False , font ='Any 10' , key= "_DATA_HORA_")  ],
                        ]
                      

        layout_buttons3 = [  

                            [ sg.Button( '' , key = ('voltar'   , self.index  , colunn_name , title_card ), 
                                            button_color            = ( self.buttons_cardtask_color[0] ,  back_color ) ,
                                            mouseover_colors        = ( self.buttons_cardtask_color[1] , self.buttons_cardtask_color[0] ), 
                                            pad                     = 1 , 
                                            #size                    = ( 2 , 1 ),
                                            border_width            = 0 ,
                                            image_data              = bs4.button_voltar
                                            )],


                            [sg.Button( '' , key = ('X'        , self.index  , colunn_name , title_card ) ,
                                            button_color            = ( self.buttons_cardtask_color[0] ,  back_color ) ,
                                            mouseover_colors        = ( self.buttons_cardtask_color[2] , self.buttons_cardtask_color[0] ), 
                                            pad                     = 1 , 
                                            #size                    = ( 2 , 1 ),
                                            border_width            = 0,
                                            image_data              = bs4.button_deletar )],


                            [sg.Button( '' , key = ('avancar'  , self.index  , colunn_name , title_card ) ,
                                            button_color            = ( self.buttons_cardtask_color[0] ,  back_color ) ,
                                            mouseover_colors        = ( self.buttons_cardtask_color[1] , self.buttons_cardtask_color[0] ), 
                                            pad                     = 1, 
                                            #size                    = ( 2 , 1 ),
                                            border_width            = 0,
                                            image_data              = bs4.button_avancar )]
                            ] 


        tags        = [ [sg.Image( img_card , pad = 2 , size=( 57 , 15 ) ) ] ]




        full_layout = [ 
                        [sg.Canvas(background_color = self.lines_cardtask_color , pad = 1 , size = ( 314 , 2 ) )] ,

                        [
                        sg.Column( lay_imagem       , background_color = back_color , element_justification = "center" , pad = 0 ,expand_x = True, expand_y = False  ),

                        sg.Column( layout_texts     , background_color = back_color , element_justification = "left" , pad = 0 ,expand_x = True, expand_y = False  ),

                        sg.Column( layout_buttons3  , background_color = back_color , element_justification = "left" , pad = 0 ,expand_x = True, expand_y = False  )
                        ],

                        [sg.Canvas(background_color = self.lines_cardtask_color , pad = 1 , size = ( 314 , 2 ) )] ,

                        
                      ]


        return [ # Frame do CARD em si  
                [sg.Frame( title_card ,
                            full_layout,
                            font             = 'Any 15' ,
                            title_color      = self.titlle_texts_cardtask_color,
                            background_color = back_color ,
                            size             = ( 310 , 135 ),
                            border_width     = 0,
                            element_justification = "center" ,
                            pad              = 7,
                            expand_x         = False,
                            expand_y         = False,
                            key              = "Frame" + str( self.index )  ),
                ]
                ]

    def deleteCardTask(self , widget):
        children = list(widget.children.values())

        for child in children:
            self.deleteCardTask(child)

        widget.pack_forget()
        widget.destroy()
        del widget

    def layoutButtons(self , text_button , key_button , button_type , button_size):
        buttons = sg.Button(   
                                button_text             = text_button,
                                button_color            = ( THEME_APP_COLORS["branco_texts"] ,  THEME_APP_COLORS["cards_buttons_azul_1"] ) ,
                                mouseover_colors        = ( THEME_APP_COLORS["cards_buttons_azul_1"] , THEME_APP_COLORS["branco_texts"] ), 
                                button_type             = button_type ,
                                s                       = button_size, 
                                key                     = key_button ,
                                pad                     = 5,
                                border_width            = 0,
                                #image_data             = base64.buttons_greens 
                                )
                     

        return buttons

    def saveValuesCardsTasks( self , value_list_database ):
       
        with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
            json.dump( value_list_database , js_file , sort_keys = False, indent = 4)
            pass

        pass


    def passCardInColunns(self , events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add , colunn_numb_delete ):

        self.card_lists[ self.colunns_keys[0] ].clear()
        self.card_lists[ self.colunns_keys[1] ].clear()
        self.card_lists[ self.colunns_keys[2] ].clear()
        self.card_lists[ self.colunns_keys[3] ].clear()

        self.deleteCardTask( widget.master )
        #del self.windons.AllKeysDict[ name_key_widgets ]


        for index_list , list_in_list in enumerate( values_list ):
            self.load_new_lists  = JSLOAD.json_read( name_file = "database/projects_datas/" + self.name_proj  )

            if list_in_list in self.load_new_lists[ self.colunns_keys[ colunn_numb_delete ]  ]:
                name_card = list_in_list[0]
               
                if name_card == events_key_name_card:
                    self.load_new_lists[ self.colunns_keys[ colunn_numb_delete ] ].remove( list_in_list )
                    self.load_new_lists[ self.colunns_keys[ colunn_numb_add ] ].append( list_in_list )
                    
                    with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
                        json.dump( self.load_new_lists , js_file , sort_keys = False, indent = 4)


                    self.windons[ self.colunns_keys[ colunn_numb_add ] ].Widget.update()
                    self.windons[ self.colunns_keys[ colunn_numb_add ] ].contents_changed()
                    self.windons.extend_layout( self.windons[ self.colunns_keys[ colunn_numb_add  ] ] , 
                                                        self.newCardTask(   col_name        = self.colunns_keys[ colunn_numb_add ] , 
                                                                            title_card      = list_in_list[0]  , 
                                                                            img_card        = list_in_list[2]  , 
                                                                            tags_cards      = list_in_list[1]  ,
                                                                            data_card       = list_in_list[3] ) )
                    

       #--------------------------------------------#--------------------------------------------#--------------------------------------------

    def update(self):
        while True:
            self.events , self.values = self.windons.Read( close = False ) #timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            try :
                if self.events == "_ADD_":
                    app_new_car         = NewCards()
                    card_list_values    = app_new_car.update()

                    
                    if card_list_values[0] != "":

                        self.windons[ self.colunns_keys[0] ].Widget.update()
                        self.windons[ self.colunns_keys[0] ].contents_changed()

                        self.windons.extend_layout( self.windons[ self.colunns_keys[0] ] , 
                                                    self.newCardTask(   col_name        = self.colunns_keys[0] , 
                                                                        title_card      = card_list_values[0]  , 
                                                                        img_card        = card_list_values[2]  , 
                                                                        tags_cards      = card_list_values[1]  ,
                                                                        data_card       = card_list_values[3] ) )
                        

                        self.list_load_data_cards[ self.colunns_keys[0] ].append( card_list_values )
                        self.saveValuesCardsTasks( value_list_database = self.list_load_data_cards )

                
                    # AVANÇANDO OS CARDSTASKS PARA AS PROXIMAS COLUNAS -----------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                
                if self.events[0] == "avancar":

                    events_key_n         = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]

                    name_key_widgets     = 'Frame' + str( events_key_n )
                    widget               = self.windons[ name_key_widgets ].Widget

                    card_values_load     = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list          = card_values_load[ events_key_n_col ]


                    if events_key_n_col == self.colunns_keys[ 0 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 1  , colunn_numb_delete = 0)
                    
                    if events_key_n_col == self.colunns_keys[ 1 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 2  , colunn_numb_delete = 1)
                    
                    if events_key_n_col == self.colunns_keys[ 2 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 3  , colunn_numb_delete = 2)

                    pass

                    

                # VOLTANDO OS CARDSTASKS PARA COLUNAS ANTERIORES ---------------------------------------------------
                #---------------------------------------------------------------------------------------------------

                if self.events[0] == "voltar":

                    events_key_n         = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]

                    name_key_widgets    = 'Frame' + str( events_key_n )
                    widget              = self.windons[ name_key_widgets ].Widget

                    card_values_load    = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list         = card_values_load[ events_key_n_col ]

                    # -------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[ 3 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 2  , colunn_numb_delete = 3)
                    
                    if events_key_n_col == self.colunns_keys[ 2 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 1  , colunn_numb_delete = 2)
                    
                    if events_key_n_col == self.colunns_keys[ 1 ] :
                        self.passCardInColunns( events_key_n_col , values_list , events_key_name_card , name_key_widgets , widget , colunn_numb_add = 0  , colunn_numb_delete = 1)

                    pass



                # DELETAMENTO DOS CARDSTASKS -----------------------------------------------------------------------
                #---------------------------------------------------------------------------------------------------

                if self.events[0] == 'X':
                    i                    = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]

                    name_key_widgets    = 'Frame' + str( i )
                    widget              = self.windons[ name_key_widgets ].Widget


                    load_new_lists  = JSLOAD.json_read( name_file = "database/projects_datas/" + self.name_proj  )

                    #card_values_load    = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list         = load_new_lists[ events_key_n_col ][0]
                    
                    name_img_task       = str( self.path_tasks_and_img[1] +  events_key_name_card + ".png" )

                    del self.windons.AllKeysDict[ name_key_widgets ] 
                    self.deleteCardTask( widget.master )
                    
                    load_new_lists[  events_key_n_col ].remove( values_list )
                    os.remove(  name_img_task )

                    with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
                        json.dump( load_new_lists , js_file , sort_keys = False, indent = 4 )

                #---------------------------------------------------------------------------------------------------

            except TypeError as printErro:
                print( f' Esse é o erro --> { printErro }')
                pass

            
#app = AppLayout()
#app.update()