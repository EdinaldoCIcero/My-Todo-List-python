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
from JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval
from PIL import Image


#-----------------------------------------------------------------------------------------------
JSLOAD           = JsonClass()
COLORS_APP       = JSLOAD.json_read(name_file = "database/appColors" )
THEME_APP_COLORS = JSLOAD.json_read(name_file = "database/themeApp" )

#-----------------------------------------------------------------------------------------------

class AppLayout():
    def __init__(self):
        sg.theme("Dark")

        #self.type_wind          = type_windtitle
        #-----------------------------------------------------------------------------------------------
        self.trava_comands      = True
        self.buttons_sizes      = (5 , 2)
        self.background_color   = COLORS_APP["PRETO_20%"] #THEME_APP_COLORS["background"]
        #--------------------
        self.index              = 0 
        self.index_col          = 0
        self.col_lists_size     = ( 210 , 300 )

        self.card_lists         = {
                                    "COLUN_1" :  self.new_rows( col_name = "COL_1" ) ,
                                    "COLUN_2" :  self.new_rows( col_name = "COL_2" ) ,
                                    "COLUN_3" :  self.new_rows( col_name = "COL_3" ) ,
                                    "COLUN_4" :  self.new_rows( col_name = "COL_4" ) ,
                                  }
        #----------- Layouts ----------------------------------------------------------------------------

        self.text_layout = [
                        [ sg.Push( background_color = self.background_color ),

                        sg.Text("Fazer"         , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),

                        sg.Text("Fazendo"       , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),    

                        sg.Text("Aprovados"     , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ),

                        sg.Text("Finalizados"   , text_color = COLORS_APP["BRANCO_1"] , background_color = self.background_color , justification='c', font='Any 20' ),
                        sg.Push(background_color = self.background_color ) ]
                            ]


        self.button_lay  = [
                            [self.layoutButtons( text_button = "PLUS" , key_button  = "_ADD_", 
                                                 button_type = 7      , button_size = (5 , 2) )],

                            [self.layoutButtons( text_button = "Conf" , key_button  = "_ADD_",
                                                 button_type = 7      , button_size = (5 , 2) )] 
                                ]

        self.layouts_col = [

                            [
                            sg.Column( self.new_rows( col_name = "COL_1" ) ,
                                        background_color    = self.background_color, size = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only  = True, 
                                        expand_x            = True, expand_y              = True,
                                        pad                 = 0   , key                   = 'COL_1'),


                            #sg.Push(background_color = self.background_color ) ,
                            sg.Column( self.new_rows( col_name = "COL_2") ,
                                        background_color    = self.background_color, size = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only  = True, 
                                        expand_x            = True, expand_y              = True, 
                                        pad                 = 0    , key                 = 'COL_2'),
                            

                            #sg.Push(background_color = self.background_color ) ,
                            sg.Column(self.new_rows( col_name = "COL_3") ,
                                        background_color    = self.background_color,
                                        size                = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only = True, 
                                        expand_x            = True, expand_y             = True, 
                                        pad                 = 0   , key                  = 'COL_3'),
                            

                            #sg.Push(background_color = self.background_color ) ,
                            sg.Column( self.new_rows( col_name = "COL_4" )  ,
                                        background_color    = self.background_color,
                                        size                = self.col_lists_size,
                                        scrollable          = True, vertical_scroll_only = True, 
                                        expand_x            = True, expand_y             = True, 
                                        pad                 = 0   , key                 = 'COL_4'),
                            
                            
                            ]
                        ]



        self.Full_layouts = [
                             
                            [ sg.Column( self.text_layout  , background_color = self.background_color  , pad = 0 , expand_x = True, expand_y = False  ) ],

                            [ 
                             sg.Column( self.button_lay    , background_color = COLORS_APP["BRANCO_1"]  , pad = 0 , size = (60 , 10) , expand_x = False, expand_y = True  ) ,
                             
                             sg.Column( self.layouts_col   , background_color = self.background_color   , pad = 0 , expand_x = True, expand_y = True  ),
                             
                             #sg.Column( [ [ sg.Push(background_color = self.background_color ) ] ]   , background_color = self.background_color   , pad = 0 , expand_x = True, expand_y = True  ),
                             
                             #sg.Push(background_color = self.background_color ),

                            ]

                            ]

        self.windons =  sg.Window( "TITLE",
                            background_color        = self.background_color,
                            size                    = (1024 , 600) ,
                            #icon                   = "Icon.ico",
                            #titlebar_icon          = base64.icone , 
                            #use_custom_titlebar    = False ,
                            return_keyboard_events  = True  ,
                            use_default_focus       = False ,
                            resizable               = True ,
                            finalize                = False ).layout( self.Full_layouts  )
        
        

        #self.windons.maximize()

        #-------------------------------------------------------------------------------------------------------------------

    def new_rows(self  , col_name ):
        global index

        colunn_name = col_name

        list_colors_name = [ "ROXO_#a4" , "BRANCO_2" , "AZUL_CLARO" ]
        ran_color        = randint( 0 , 2 )

        self.index      += 1

        back_color      = COLORS_APP["BRANCO_2"]

        ran_key         = str( randint( 0 , 1100) )


        # -------------------------------------------------------------------------------------------
        lay_imagem   = [ [sg.Image("imgs/tesseract.png", pad = 4 , size=( 60 , 60 ), key="IMG_") ] ]
                       

        layout_texts = [
                        [ sg.Text( "Responsavel : " , text_color = COLORS_APP["PRETO_0"] ,pad = 0 , background_color = back_color , font ='Any 8'),
                          sg.Text( "Nome"       , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_NOME_P") ], 
                        [sg.Text(  "Data/Hora"  , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_DATA_HORA_")],
                        [sg.Text(  "Descrção"   , text_color = COLORS_APP["PRETO_0"] , pad = 0 , background_color = back_color , font ='Any 8' , key= "_DESCRTION_")]

                        

                        # [sg.Multiline(  default_text     = "Digite uma descrição caso queira.",
                        #                size             = (10, 6),
                        #                background_color = COLORS_APP["BRANCO_1"] ,
                        #                text_color       = COLORS_APP["PRETO_0"] , 
                        #                key              = "descrition_out"
                        #                )]


                        ]


        layout_buttons3 = [ 
                            [sg.Button('<', key = ('voltar'   , self.index  , colunn_name ) , pad = 1 ,size = ( 2 , 1 ) )],
                            [sg.Button('X', key = ('X'        , self.index  , colunn_name ) , pad = 1 ,size = ( 2 , 1 ) )],
                            [sg.Button('>', key = ('avancar'  , self.index  , colunn_name ) , pad = 1 ,size = ( 2 , 1 ) )],
                          ]


        full_layout = [ 
                        [sg.Canvas(background_color = COLORS_APP["PRETO_0"] , pad = 0 , size = ( 220 , 2 ) )] ,

                        [
                        sg.Column( lay_imagem       , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  ),
                        #sg.Push(background_color = self.background_color ),

                        sg.Column( layout_texts     , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  ),
                        #sg.Push(background_color = self.background_color ),

                        sg.Column( layout_buttons3  , background_color = back_color , pad = 0 ,expand_x = True, expand_y = True  )

                        ]
                      ]

        return [
                [sg.Frame( f"Titulo -  {self.index:0>2d}" ,
                            full_layout,
                            font             = 'Any 15' ,
                            title_color      = COLORS_APP["PRETO_0"],
                            background_color = back_color ,  #COLORS_APP[ list_colors_name[ ran_color ] ],
                            size             = ( 230 , 130 ),
                            border_width     = 0,
                            pad              = 2,
                            expand_x         = True,
                            expand_y         = True,
                            key              = "Frame" + str( self.index )  ),
                ]
                ]

                



    def delete_widget(self , widget):
        children = list(widget.children.values())

        for child in children:
            self.delete_widget(child)

        widget.pack_forget()
        widget.destroy()
        del widget

    def newLayoutColunn(self):
        ran             = randint( 0 , 10000 )
        titu_text_test  = "Lay_" + str( ran)

        news_lay        = [ [sg.Text( titu_text_test ) ] ]


        return sg.Column( news_lay , background_color = self.background_color )
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
        #frame_id    = self.windons['COL_01'].Widget.frame_id
        #frame       = self.windons['COL_01'].Widget.TKFrame
        
        

        while True:
            self.events , self.values = self.windons.Read( )#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            

            if self.index_col >= 3:
                self.index_col = 4
            
            #if self.index_col <= 1:
             #   self.index_col = 1
            

            try :

                if self.events == "_ADD_":
                    self.index_col = 0

                    self.windons['COL_1'].Widget.update()
                    self.windons['COL_1'].contents_changed()


                    self.windons.extend_layout(  self.windons["COL_1"] , self.new_rows( col_name = "COL_1" ) )



                if self.events[0] == "avancar":

                    events_key_n     = self.events[1]
                    events_key_n_col = self.events[2]


                    name_key_widgets = 'Frame' + str( events_key_n )
                    widget           = self.windons[ name_key_widgets ].Widget

                    #colunn_key_name  = "COL_" + str( self.index_col )
                    #widget_key_coll  =  str(self.windons.AllKeysDict[ colunn_key_name ].key)
                    

                    #print( "---<> " , self.windons.AllKeysDict[ colunn_key_name ].key  )



                    if events_key_n_col == "COL_1":
                        self.windons[ "COL_2" ].Widget.update()
                        self.windons["COL_2" ].contents_changed()
                        self.windons.extend_layout(  self.windons[  "COL_2"  ] , self.new_rows( col_name = "COL_2"  ) )

                        del self.windons.AllKeysDict[ name_key_widgets]
                        self.delete_widget( widget.master )
                    

                    if events_key_n_col == "COL_2":
                        self.windons[ "COL_3" ].Widget.update()
                        self.windons[ "COL_3" ].contents_changed()
                        self.windons.extend_layout(  self.windons[  "COL_3" ] , self.new_rows( col_name = "COL_3"  ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.delete_widget( widget.master )
                    

                    if events_key_n_col == "COL_3":

                        self.windons[ "COL_4" ].Widget.update()
                        self.windons["COL_4" ].contents_changed()
                        self.windons.extend_layout(  self.windons[  "COL_4"  ] , self.new_rows( col_name = "COL_4"  ) )

                        del self.windons.AllKeysDict[ name_key_widgets ]
                        self.delete_widget( widget.master )











                elif self.events[0] == 'X':
                    i                = self.events[1]
                    name_key_widgets = 'Frame' + str( i )
                    widget           = self.windons[ name_key_widgets ].Widget

                    del self.windons.AllKeysDict[ name_key_widgets ]
                    self.delete_widget( widget.master )


            except TypeError as printErro:
                print( f' Esse é o erro --> { printErro }')
                pass



app = AppLayout()
app.update()