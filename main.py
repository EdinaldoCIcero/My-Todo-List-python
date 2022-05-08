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

#-----------------------------------------------------------------------------------------------
JSLOAD              = JsonClass()
COLORS_APP          = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS    = JSLOAD.json_read(name_file = "database/themeApp" )

#-----------------------------------------------------------------------------------------------

class AppLayout():
    def __init__(self , project_name ):
        sg.theme("Dark")
        

        # atributos e variaveeis -----------------------------------------------------------------------
        self.data_hor = datetime.now()
        self.name_proj           = project_name
        self.path_tasks_and_img  = [ "database/projects_datas/" , "database/projects_datas/tasksImages/" ]
        self.path_datasbase_cols = "database/projects_datas/" + self.name_proj 
        self.CARDS_DATAS_LOADS   = JSLOAD.json_read( name_file = "database/projects_datas/" + self.name_proj  )

        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)
        self.background_color   = COLORS_APP["PRETO_20%"]
        self.colunns_keys       = [ "COL_1" , "COL_2" , "COL_3" , "COL_4"]

        self.index              = 0 
        self.index_col          = 0
        self.col_lists_size     = ( 210 , 300 )

        self.list_load_data_cards = self.CARDS_DATAS_LOADS


        #---------- Demostração do DAtabase de cada projeto o que é salvo e carregado no momento !--------------------------------
        self.database_basic     = {  "Coluna_1" : [ "Nome do cardTastks " , "descrtion" , "path_img" , "data / hora "] } 


        #------ Base do DataBase -------------------------------------------------------
        self.card_lists         = {
                                    "COLUN_1" : [ ] ,
                                    "COLUN_2" : [ ] ,
                                    "COLUN_3" : [ ] ,
                                    "COLUN_4" : [ ] 
                                  }

        #-----------------------------------------------------------------------------------------------

        # -------- CARREGANDO OS VALORES DO DATABASE -------------------------------------------------------------
        for index_list_col1 , list_values_col1 in enumerate( self.list_load_data_cards[ self.colunns_keys[0] ] ):
            print( list_values_col1 )
            card_news_col_1 = self.loadCardsCols(list_load_values = list_values_col1 , col_key_name = self.colunns_keys[0]  )
            self.card_lists["COLUN_1"].append( card_news_col_1[0] )

        for index_list_col2 , list_values_col2 in enumerate( self.list_load_data_cards[ self.colunns_keys[1] ] ):
            card_news_col_1 = self.loadCardsCols(list_load_values = list_values_col2 , col_key_name = self.colunns_keys[1]  )
            self.card_lists["COLUN_2"].append( card_news_col_1[0] )
        
        for index_list_col3 , list_values_col3 in enumerate( self.list_load_data_cards[ self.colunns_keys[2] ] ):
            card_news_col_1 = self.loadCardsCols(list_load_values = list_values_col3 , col_key_name = self.colunns_keys[2]  )
            self.card_lists["COLUN_3"].append( card_news_col_1[0] )
        
        for index_list_col4 , list_values_col4 in enumerate( self.list_load_data_cards[ self.colunns_keys[3] ] ):
            card_news_col_1 = self.loadCardsCols(list_load_values = list_values_col4 , col_key_name = self.colunns_keys[3]  )
            self.card_lists["COLUN_4"].append( card_news_col_1[0] )
        





        #----------- Layouts ----------------------------------------------------------------------------

        self.text_layout = [
                        [ sg.Push( background_color = self.background_color ),

                        sg.Text("  Fazer"         , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),

                        sg.Text("  Fazendo"       , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),    

                        sg.Text("  Aprovados"     , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),

                        sg.Text(" Finalizados"   , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ) ]
                            ]


        self.button_lay  = [
                            [self.layoutButtons( text_button = "PLUS" , key_button  = "_ADD_", 
                                                 button_type = 7      , button_size = (5 , 2) ),

                            self.layoutButtons( text_button = "Conf" , key_button  = "_ADD_",
                                                 button_type = 7      , button_size = (5 , 2) )]

                            ]


        self.layouts_col = [

                            [
                            sg.Column(  self.card_lists["COLUN_1"] ,
                                        background_color    = self.background_color, size = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only  = True, 
                                        expand_x            = True, expand_y              = True,
                                        justification       = "center" ,
                                        #element_justification = "center",
                                        #vertical_alignment  = "center", 
                                        pad                 = 0 , 
                                        key                 = self.colunns_keys[0]),


                           
                            sg.Column(  self.card_lists["COLUN_2"],
                                        background_color    = self.background_color, size = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only  = True, 
                                        expand_x            = True, expand_y              = True,
                                        element_justification = "center",
                                        #vertical_alignment  = "center",
                                        pad                 = 0    , 
                                        key                 = self.colunns_keys[1] ),
                            

                            
                            sg.Column(  self.card_lists["COLUN_3"] ,
                                        background_color    = self.background_color,
                                        size                = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only = True, 
                                        expand_x            = True, expand_y             = True,
                                        element_justification = "center",
                                        #vertical_alignment  = "center", 
                                        pad                 = 0   ,
                                        key                 = self.colunns_keys[2] ),
                            

                           
                            sg.Column(  self.card_lists["COLUN_4"] ,
                                        background_color    = self.background_color,
                                        size                = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only = True, 
                                        expand_x            = True, expand_y             = True,
                                        element_justification = "center",
                                        #vertical_alignment  = "center", 
                                        pad                 = 0   , 
                                        key                 = self.colunns_keys[3] ),

                            ]

                        ]


        #-------- FLL LAYOUTS -----------------------
        self.Full_layouts = [
                             
                            self.button_lay,
                            [ sg.Column( self.text_layout  , background_color = self.background_color  , element_justification = "center", pad = 0 , expand_x = True, expand_y = False  ) ],
                            [ sg.Column( self.layouts_col   , background_color = self.background_color   , pad = 10 , expand_x = True, expand_y = True  ) ]
                            ]


        #---------- JANELA_ -----------------------------------------------
        self.windons =  sg.Window( "TITLE",
                            background_color        = self.background_color,
                            size                    = (1024 , 600) ,
                            #icon                   = "Icon.ico",
                            #titlebar_icon          = base64.icone , 
                            #use_custom_titlebar    = False ,
                            return_keyboard_events  = True  ,
                            use_default_focus       = False ,
                            resizable               = True ,
                            finalize                = True,
                            #transparent_color       = self.background_color ,
                            element_justification   = "center" 
                            ).layout( self.Full_layouts  )
        


    #------ MEDOTOS DO APP ---------------------------------------------------------------------------------------------------
    def loadCardsCols(self , list_load_values , col_key_name  ):

        card_make   = self.newCardTask( col_name        = col_key_name , 
                                        title_card      = list_load_values[0] , 
                                        img_card        = list_load_values[2] , 
                                        descrtions_card = list_load_values[1] ,
                                        data_card       = list_load_values[3]
                                        )

        return card_make

    def newCardTask(self  , col_name  , title_card , img_card , descrtions_card , data_card ):
        global index

        colunn_name     = col_name

        self.index      += 1
        back_color      = COLORS_APP["BRANCO_2"]


        # -------------------------------------------------------------------------------------------
        lay_imagem   = [ [sg.Image( img_card , pad = 4 , size=( 60 , 60 ), key="IMG_") ] ]
                       

        layout_texts = [
                        [ sg.Text( "Responsavel : "  , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8'),
                          sg.Text( "Nome"            , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_NOME_P") ], 
                        [sg.Text(  "Data/Hora : " + data_card , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_DATA_HORA_")],
                        #[sg.Text(  "dd" , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_DATA_HORA_")],
                        
                        [sg.Text(  "Descrção  : \n" + descrtions_card    , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_DESCRTION_")]
                        ]

        
        layout_buttons3 = [ 
                            #[
                            
                            #]

                          ]


        full_layout = [ 
                        [sg.Canvas(background_color = COLORS_APP["PRETO_0"] , pad = 0 , size = ( 260 , 3 ) )] ,

                        [
                        sg.Column( lay_imagem       , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  ),
                        #sg.Push(background_color = self.background_color ),
                        sg.Column( layout_texts     , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  ),
                        #sg.Column( layout_buttons3  , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  )
                        ],
                        [
                        sg.Push(background_color = back_color ),

                        sg.Button( '<' , key = ('voltar'   , self.index  , colunn_name , title_card ) , pad = 1 , size = ( 2 , 1 ) ),
                        sg.Button( 'X' , key = ('X'        , self.index  , colunn_name , title_card ) , pad = 1 , size = ( 2 , 1 ) ),
                        sg.Button( '>' , key = ('avancar'  , self.index  , colunn_name , title_card ) , pad = 1 , size = ( 2 , 1 ) )
                        ] 

                      ]

        return [
                [sg.Frame( title_card ,
                            full_layout,
                            font             = 'Any 15' ,
                            title_color      = COLORS_APP["PRETO_0"],
                            background_color = back_color ,  #COLORS_APP[ list_colors_name[ ran_color ] ],
                            size             = ( 260 , 130 ),
                            border_width     = 0,
                            pad              = 2,
                            expand_x         = True,
                            expand_y         = True,
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
        buttons = sg.Button(   button_text           = text_button,
                                button_color         = (self.background_color, COLORS_APP["AZUL_CLARO"]) ,
                                button_type          = button_type ,
                                s                    = button_size, 
                                key                  = key_button ,
                                border_width         = 0,
                                #image_data              = base64.buttons_greens 
                                )
                     

        return buttons

    def saveValuesCardsTasks( self , value_list_database ):
       
        with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
            json.dump( value_list_database , js_file , sort_keys = False, indent = 4)
            pass

        pass

    def saveDatabaseCardsTasks(self ,list_values , col_key_add , col_key_del ):

        self.list_load_data_cards[ col_key_add ].append( list_values )
        self.list_load_data_cards[ col_key_del ].remove( list_values )

        with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
            json.dump( self.list_load_data_cards , js_file , sort_keys = False, indent = 4)


        pass

    def update(self):

        while True:
            self.events , self.values = self.windons.Read( )#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            
            if self.index_col >= 3:
                self.index_col = 4
            

            try :
                if self.events == "_ADD_":
                    self.index_col   = 0
                    app_new_car      = NewCards()
                    card_list_values = app_new_car.update()

                    self.windons[ self.colunns_keys[0] ].Widget.update()
                    self.windons[ self.colunns_keys[0] ].contents_changed()

                    self.windons.extend_layout(  self.windons[ self.colunns_keys[0] ] , 
                                                self.newCardTask(  col_name        = self.colunns_keys[0] , 
                                                                    title_card      = card_list_values[0] , 
                                                                    img_card        = card_list_values[2] , 
                                                                    descrtions_card = card_list_values[1],
                                                                    data_card       = card_list_values[3]
                                                                        ) )
                    
                    self.list_load_data_cards[ self.colunns_keys[0] ].append( card_list_values )
                    
                    self.saveValuesCardsTasks( value_list_database = self.list_load_data_cards )


            #----------------------------------------------------------------------
            #----------------------------------------------------------------------

                if self.events[0] == "avancar":

                    events_key_n         = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]


                    name_key_widgets = 'Frame' + str( events_key_n )
                    widget           = self.windons[ name_key_widgets ].Widget

                    card_values_load = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list      = card_values_load[ events_key_n_col ][0]


                    # AVANÇO DA COLUNA 1 PARA A 3 ----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[0] :

                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[1] , 
                                                    col_key_del = self.colunns_keys[0] )

                        self.windons[ self.colunns_keys[1] ].Widget.update()
                        self.windons[ self.colunns_keys[1] ].contents_changed()
                        self.windons.extend_layout(  self.windons[ self.colunns_keys[1] ] , 
                                                    self.newCardTask(   col_name        = self.colunns_keys[1] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3] ) )

                        del self.windons.AllKeysDict[ name_key_widgets]
                        self.deleteCardTask( widget.master )


                    # AVANÇO DA COLUNA 2 PARA A 3----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[1]:
                        
                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[2] , 
                                                    col_key_del = self.colunns_keys[1] )

                        self.windons[ self.colunns_keys[2] ].Widget.update()
                        self.windons[ self.colunns_keys[2] ].contents_changed()

                        self.windons.extend_layout(  self.windons[  self.colunns_keys[2] ] , 
                                                    self.newCardTask(  col_name        = self.colunns_keys[2] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3] ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.deleteCardTask( widget.master )

                        
                    # AVANÇO DA COLUNA 3 PARA A 4 ----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[2]:

                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[3] , 
                                                    col_key_del = self.colunns_keys[2] )

                        self.windons[ self.colunns_keys[3] ].Widget.update()
                        self.windons[ self.colunns_keys[3] ].contents_changed()

                        self.windons.extend_layout(  self.windons[  self.colunns_keys[3] ] , 
                                                    self.newCardTask(  col_name        = self.colunns_keys[3] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3] 
                                                                        ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.deleteCardTask( widget.master )
                #---------------------------------------------------------------------------------------------------------


                if self.events[0] == "voltar":

                    events_key_n         = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]


                    name_key_widgets = 'Frame' + str( events_key_n )
                    widget           = self.windons[ name_key_widgets ].Widget

                    card_values_load = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list      = card_values_load[ events_key_n_col ][0]


                    # AVANÇO DA COLUNA 1 PARA A 3 ----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[3] :

                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[2] , 
                                                    col_key_del = self.colunns_keys[3] )

                        self.windons[ self.colunns_keys[2] ].Widget.update()
                        self.windons[ self.colunns_keys[2] ].contents_changed()
                        self.windons.extend_layout(  self.windons[ self.colunns_keys[2] ] , 
                                                    self.newCardTask(   col_name        = self.colunns_keys[2] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3]   ) )

                        del self.windons.AllKeysDict[ name_key_widgets]
                        self.deleteCardTask( widget.master )


                    # AVANÇO DA COLUNA 2 PARA A 3----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[2]:
                        
                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[1] , 
                                                    col_key_del = self.colunns_keys[2] )

                        self.windons[ self.colunns_keys[1] ].Widget.update()
                        self.windons[ self.colunns_keys[1] ].contents_changed()

                        self.windons.extend_layout(  self.windons[  self.colunns_keys[1] ] , 
                                                    self.newCardTask(  col_name        = self.colunns_keys[1] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3]  ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.deleteCardTask( widget.master )

                        
                    # AVANÇO DA COLUNA 3 PARA A 4 ----------------------------------------------------------------------
                    #---------------------------------------------------------------------------------------------------
                    if events_key_n_col == self.colunns_keys[1]:

                        self.saveDatabaseCardsTasks( list_values = values_list , 
                                                    col_key_add = self.colunns_keys[0] , 
                                                    col_key_del = self.colunns_keys[1] )

                        self.windons[ self.colunns_keys[0] ].Widget.update()
                        self.windons[ self.colunns_keys[0] ].contents_changed()

                        self.windons.extend_layout(  self.windons[  self.colunns_keys[0] ] , 
                                                    self.newCardTask(  col_name        = self.colunns_keys[0] , 
                                                                        title_card      = values_list[0] , 
                                                                        img_card        = values_list[2] , 
                                                                        descrtions_card = values_list[1] ,
                                                                        data_card       = values_list[3] ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.deleteCardTask( widget.master )



                # DELETAMENTO DOS CARDSTASKS -----------------------------------------------------------------------
                #---------------------------------------------------------------------------------------------------
                elif self.events[0] == 'X':
                    i                    = self.events[1]
                    events_key_n_col     = self.events[2]
                    events_key_name_card = self.events[3]

                    name_key_widgets = 'Frame' + str( i )
                    widget           = self.windons[ name_key_widgets ].Widget

                    card_values_load = JSLOAD.json_read( name_file = self.path_datasbase_cols )
                    values_list      = card_values_load[ events_key_n_col ][0]

                    name_img_task    = str( self.path_tasks_and_img[1] +  events_key_name_card + ".png" )

                    del self.windons.AllKeysDict[ name_key_widgets ]
                    self.deleteCardTask( widget.master )
                    
                    self.list_load_data_cards[ events_key_n_col ].remove( values_list )
                    os.remove(  name_img_task )
                    

                    with open( self.path_datasbase_cols + '.json', "w" , encoding="utf8") as js_file:
                        json.dump( self.list_load_data_cards , js_file , sort_keys = False, indent = 4)
                #---------------------------------------------------------------------------------------------------


            except TypeError as printErro:
                print( f' Esse é o erro --> { printErro }')
                pass
       


#app = AppLayout()
#app.update()