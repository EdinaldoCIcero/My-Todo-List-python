from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
import os
import sys
import shutil
from pprint import pprint, pformat
from ast import literal_eval

from PySimpleGUI.PySimpleGUI import Print

from libs.creator_folders import CreatorFolders
from libs.dataSaveLoad import DataSaveLoad

from PIL import Image

import img_base64 as base64 

EXTENSION_FILE_BOOKS = ".fbook"
DIR_BOOKS            = "books/"
DIR_CAPS             = "books/capas/"
EXTENSION_IMG_BOOKS  = ".png"

COLORS_APP          = { 
    "AZUL_ESCURO_SINZENTO"  : "#242b2f",
    "VERDE_CLARO"           : "#40c173",
    "SINZA_CLARO_1"         : "#4f5457",
    "CINZA_CLARO_2"         : "#656a71",
    "AZUL_CLARO"            : "#5a7aff",
    "BRANCO_1"              : "#ffffff",
    "BRANCO_2"              : "#fafafa",
    "LARANJA"               : "#f5b559",
    "AMARELO"               : "#f9d46d"

}



####################################################################################################
# CLASSE APPBOOK MAIN ##############################################################################
# --------------------------------------------------------------------------------------------------
class AppBook():
    def __init__(self):
        sg.theme("Reddit")

        self.creato_folder  = CreatorFolders()
        self.datals         = DataSaveLoad( path = DIR_BOOKS)

        self.up_list_folder    = self.creato_folder.listFiles(folder_files = DIR_BOOKS , 
                                                            extencion_file = EXTENSION_FILE_BOOKS )

        self.list_folder_capas = self.creato_folder.listFiles(folder_files = DIR_CAPS, 
                                                            extencion_file = EXTENSION_IMG_BOOKS )                                          
        #-----------------------------------------------------------------------------------------------
        self.lista_covers         = []
        self.lista_cover_selected = []
        self.LisrTable_values     = []

        self.forrange() 
        self.head = [ "Nome do Livro " , "Pessoa " , "Data" , "Horas" ]
        
#############################################################################
#----------------- LAYOUTS AND ELEMENTS OF COLUNNS   ------------------------
#----------------------------------------------------------------------------
        self.capas_cover  = [ 
                                [
                                sg.Canvas(background_color =COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 18 ,2 ) ), 
                                sg.Image( DIR_CAPS + "padrao.png" ,size=(150 , 226), key="_IMGTAB_1_")
                                ] 
        ]

        self.inputs_white = [   [ #sg.Text("LISTA", background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"]),

                                sg.Button(button_text               = "",
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_ESCURO_SINZENTO"]) ,
                                            #button_type             = 2 ,
                                            #s                       = (17 , 1) , 
                                            key                     = "_Op_",
                                            border_width            = 0,
                                            image_data              = base64.butao_creditos 
                                            )
                                ],

                                [sg.Canvas(background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 0 ,50) )],
                                
                                [
                                sg.Text("Nome do livro "                    , text_color = 'white', background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) , 
                                sg.Text("             Nome da pessoa "      , text_color = 'white', background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) , 
                                sg.Text("         Data "                    , text_color = 'white', background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] ) , 
                                sg.Text("                          Hora "   , text_color = 'white', background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] )           
                                ],
                                
                                [
                                sg.In(key='_BOOKNAME_'  , size = ( 20 ,2 ) , border_width=0 ,pad=None ), 
                                sg.In(key='_PESSOA_'    , size = ( 20 ,2 ) , border_width=0 ,pad=None ), 
                                sg.In(key='_DATA_'      , size = ( 20 ,2 ) , border_width=0 ,pad=None ), 
                                sg.In(key='_HORA_'      , size = ( 20 ,2 ) , border_width=0 ,pad=None ) 
                                ],

                                [sg.Canvas(background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 0 ,55) )],

                                [   sg.Canvas(background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 50 ,1 ) ),

                                    sg.Button(button_text              = "Adicionar imagem de capa",
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_ESCURO_SINZENTO"]) ,
                                            button_type             = 2 ,
                                            s                       = (17 , 1) , 
                                            key                     = "_ADDCAPA_",
                                            border_width            = 0,
                                            image_data              = base64.buttons_greens 
                                            ),

                                sg.Button(button_text              = "Exclir da lista"  , 
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_ESCURO_SINZENTO"]) ,
                                            key                     = "_DELET1_LIST_"    , 
                                            size                    = (17,1) , 
                                            border_width            = 0 ,
                                            image_data              = base64.buttons_greens 
                                            ),


                                sg.Button(button_text              = "Adicionar na lista" ,
                                            button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_ESCURO_SINZENTO"]) ,
                                            key                     = "_ADDBOOK_", 
                                            size                    = (17,1) ,
                                            border_width            = 0,
                                            image_data              = base64.buttons_greens 
                                            )],

                               
                            ]

       


        self.colun_table    = [ [sg.Table(
                                        values                  = self.LisrTable_values, 
                                        headings                = self.head,
                                        #col_widths            = [30],
                                        auto_size_columns       = False,
                                        select_mode             = sg.TABLE_SELECT_MODE_BROWSE,
                                        display_row_numbers     = True, 
                                        change_submits          = True, 
                                        justification           = 'center',
                                        text_color              = COLORS_APP["SINZA_CLARO_1"],
                                        background_color        = COLORS_APP["BRANCO_2"],
                                        selected_row_colors     = (COLORS_APP["BRANCO_1"] , COLORS_APP["VERDE_CLARO"] ),
                                        header_background_color = COLORS_APP["AZUL_CLARO"],
                                        num_rows                = 3000,
                                        enable_events           = True,
                                        enable_click_events     = True,
                                        bind_return_key         = True,
                                        alternating_row_color   = 'lightblue',
                                        expand_x                = True,
                                        key                     = '_TABLE_',
                                        right_click_menu        = [ ["Excluir"] , "Excluir" ],
                                        pad                     = 0 ,
                                        row_height              = 35,
                                        col_widths              = [22, 22, 22, 22],
                                        )] 
                                    ] 

############################################################################################
#------------------------- LAYOUTS MAIN  ---------------------------------------------------

        self.layouts_full =  [ 

                    [
                    sg.Image( data = base64.imagem_icon , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"]  ),
                    sg.Canvas(background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 10 ,1 ) ),
                    sg.Column( self.inputs_white , background_color=COLORS_APP["AZUL_ESCURO_SINZENTO"] ) , 
                    sg.Column( self.capas_cover  , background_color=COLORS_APP["AZUL_ESCURO_SINZENTO"] ) 
                    ],

                    [self.colun_table]

                    ]


        self.windons  = sg.Window( "The List of Books",
                                    background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                    size                = (1024,600) ,
                                    resizable           = TRUE,
                                    no_titlebar         = False ,
                                    icon                = "Icon.ico",
                                    titlebar_icon       = base64.icone , 
                                    use_custom_titlebar = False

                                    ).layout(self.layouts_full)

        
####################################################################################################
#-----------------------FUNÇÕES PRINCIPAIS DO LAYOUT ---------------------------------------------
#----------------------------------------------------------------------------------------------------
    def coverResize(self, image_file_name , imagen_resize ):
        
        with Image.open( image_file_name ) as im:
            im_resized = im.resize(  imagen_resize  )

            return im_resized 

            #img = shutil.copy( self.values["_ADDCAPA_"]  , DIR_BOOKS + "capas" )
        pass    


    def getCoverName(self):
        for root , dirs , files in os.walk( DIR_BOOKS ):
                for file in files:
                    if EXTENSION_FILE_BOOKS in file:
                        resu   = self.datals.loadDataListExtencioJoin(name_data_file = file )
                        lista_values = resu[0]
                        self.lista_covers.append( lista_values )

        pass


    def forrange(self):
            for root , dirs , files in os.walk( DIR_BOOKS ):
                for file in files:
                    if EXTENSION_FILE_BOOKS in file:
                        resu   = self.datals.loadDataListExtencioJoin(name_data_file = file )
                        self.LisrTable_values.append( resu[1] )
                    
            pass


    def loadBookInfo(self , list_book_info , book_name ):
        with open(  DIR_BOOKS + str(book_name) + EXTENSION_FILE_BOOKS , 'w' ) as save_file:
            save_file.write( pformat( save_file ) )
            print(save_file , "in ")
        pass


    def readBookInfo(self):
        with open(  DIR_BOOKS + str(self.values["_LISTBOX_"][0]) , 'r' ) as load_file:
            data      = load_file.read()
            load_data = literal_eval(data) 
            return load_data
        pass


    def eventsTab_1(self):
        #Eventos do TAB-1 adicionamento dos livros na lista.

        if self.events == "_TABLE_":
            self.LisrTable_values
            data_selected = [ self.LisrTable_values[row] for row in self.values["_TABLE_"]]
            try:
                self.lista_covers = []
                self.getCoverName()
                self.windons["_IMGTAB_1_"].update( self.lista_covers[ int( self.values["_TABLE_"][0] )  ] )
            except:
                pass
          

        if self.events == "_DELET1_LIST_" or self.events == "Excluir" :
            data_selected = [ self.LisrTable_values[row] for row in self.values["_TABLE_"]]
            file_dir_path = DIR_CAPS + str( data_selected[0][0] ) + EXTENSION_IMG_BOOKS

            try:
                os.remove( DIR_BOOKS + str( data_selected[0][0]  ) + EXTENSION_FILE_BOOKS  )
                os.remove( file_dir_path  )

            except:
                pass

            self.LisrTable_values = []
            self.forrange()
            self.windons["_TABLE_" ].update(values = self.LisrTable_values )



        if self.events == "_ADDBOOK_": 

            try:
                #img     = shutil.copy( self.values["_ADDCAPA_"] , DIR_BOOKS + "capas" )

                img_res = self.coverResize(image_file_name = self.values["_ADDCAPA_"] , imagen_resize = ( 150 , 226) )
                file_dir_path = DIR_CAPS + str(self.values["_BOOKNAME_"] ) + EXTENSION_IMG_BOOKS
                img_res.save(fp = file_dir_path  , format=None)

            except:
                file_dir_path  = DIR_CAPS + "padrao.png"
                

            self.datals.saveDataList(
                                    list_datas = [  file_dir_path  , [
                                                        self.values["_BOOKNAME_"] , 
                                                        self.values["_PESSOA_"] , 
                                                        self.values["_DATA_"] ,
                                                        self.values["_HORA_"]
                                                        ]
                                                ],

                                    name_data_file = self.values["_BOOKNAME_"]  , 
                                    extension_file = EXTENSION_FILE_BOOKS 
                                    )

            self.LisrTable_values = []
            self.forrange() 
            self.windons["_TABLE_" ].update(values = self.LisrTable_values )

            self.lista_covers = []
            self.getCoverName()

    def creditsWindon(self):
        sg.theme('Reddit') 
        texto = """ 
    The List of Book é software simples para listagem 
de livros muito útio para bibliotecas e livrarias.
Criado por mim Edinaldo Cicero com o intuito de 
aprendizagem e produto comercial.
Feito com python + pysimpleGUi sua funcionalidade 
é claro facilitar a marcação de livros alucados 
para pessoas descartando o forma padrão e trabalhosa 
de anotar em cadernos e folhas que em  algums momento 
iram fica lotados e é para isso que o The List of Book 
foi feito, pra facilitar sua vida!
Obrigado ha você que esta a usar o TLB agradeço muito 
por usar um de nossos programas.
"""

        layout = [
            [
            sg.Canvas(background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"] , s=( 200, 1 ) ),
            sg.Image( data = base64.imagem_icon , background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"])
            ],

            [
            sg.Text( texto , 
            font                = 'Courier 12' ,
            text_color          = 'white',
            background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"])]
            ]


        window = sg.Window( "Creditos",
                            background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                            size                = (600,530) ,
                            resizable           = TRUE,
                            no_titlebar         = False ,
                            icon                = "Icon.ico",
                            titlebar_icon       = base64.icone ,
                            use_custom_titlebar = False ).layout( layout )

        
    
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: 
                break

        window.close()


        pass
####################################################################################################
#----------------------- FUNÇÃO DE RUN DO APP      --------------------------------------------------
#----------------------------------------------------------------------------------------------------

    def main(self):
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
            
            if self.events == "_Op_":
               self.creditsWindon()


            self.eventsTab_1()
                
        pass


def splashArt():
    #IMAGE_FILE_NAME = r'imagens/SplashScreen.png'
    DISPLAY_TIME_MILLISECONDS = 4000

    layout_art = [
             [sg.Image( data = base64.splash_art ) ] 
    ]

    sg.Window('WindowTitle', layout_art , 
                                    transparent_color   = sg.theme_background_color(), 
                                    no_titlebar         = True, 
                                    keep_on_top         =True
                                    ).read(timeout      = DISPLAY_TIME_MILLISECONDS, close = True)

    app = AppBook()
    app.main()



splashArt()