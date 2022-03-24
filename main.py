import os
import sys
import shutil
from json import load
from tkinter.constants import SEL, TRUE
import PySimpleGUI as sg
from libs.JSON import JsonClass
from pprint import pprint, pformat
from ast import literal_eval

JSLOAD      = JsonClass()
COLORS_APP  = JSLOAD.json_read(name_file = "database/app_colors" )


EXTENSION_FILE = ""
AUTOR_ = """ Edinaldo é o criador desse software """



class AppBook():
    def __init__(self):
        sg.theme("Reddit")
        self.Name_Soft  = (" "*150 + "DTSL Controll" )
        
        #-----------------------------------------------------------------------------------------------
        self.ML_KEY         = '-ML-'
        self.trava_comands  = True
        self.com            = "edinaldo"
        self.buttons_sizes  = (16 , 1)



        #----------- Layouts ----------------------------------------------------------------------------

        self.one_layouts = [                        
                            [sg.Listbox(    values              = [] , #self.list_dtsl  , 
                                            enable_events       = True,
                                            background_color    = COLORS_APP["AZUL_ESCURO_2"],
                                            text_color          = COLORS_APP["BRANCO_1"],
                                            no_scrollbar        = True,
                                            size                = (40,28),
                                            key                 = "_LIST_"
                                            )],

                            [sg.Button(button_text               = "Procurar",
                                            button_color         = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            button_type          = 1 ,
                                            s                    = self.buttons_sizes , 
                                            key                  = "_ADD_DATAS_PATH_",
                                            border_width         = 0, 
                                            ),

                            sg.Button(button_text               = "Atualizar lista",
                                            button_color        = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            #button_type             = 1 ,
                                            s                   = self.buttons_sizes , 
                                            key                 = "_ATUALIZE_LIST_",
                                            border_width        = 0, 
                                            )],

                            [sg.Button(button_text               = "Criar",
                                            button_color        = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            #button_type             = 1 ,
                                            s                   = self.buttons_sizes , 
                                            key                 = "_MAKER_NEW_FILE_",
                                            border_width        = 0, 
                                            ),

                            sg.Button(button_text               = "Deletar",
                                            button_color        = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                            #button_type        = 1 ,
                                            s                   = self.buttons_sizes , 
                                            key                 = "_DELL_",
                                            border_width        = 0, 
                                            )],

                            [sg.Button(    button_text             = "Salvar alterações",
                                                button_color            = ( COLORS_APP["AZUL_ESCURO_SINZENTO"], COLORS_APP["AZUL_CLARO"]) ,
                                                #button_type             = 1 ,
                                                s                       = (34 , 1) , 
                                                key                     = "_SAVE_VALUES_",
                                                border_width            = 0, 
                                                )]

                                ]


        self.lay_texts_informs = [
                                    [sg.Text(   "Nome file ", 
                                                text_color          = 'white',
                                                background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                                key                 = "_TEXT_01_" 
                                                )],

                                    [sg.Multiline(  
                                                size                = (120, 32), 
                                                border_width        = 0,
                                                background_color    = "#4d4d4d",  #COLORS_APP["BRANCO_2"],
                                                text_color          = COLORS_APP["VERDE_CLARO"], 
                                                write_only          = False, 
                                                key                 = self.ML_KEY, 
                                                reroute_stdout      = True,
                                                #focus               = True,
                                                echo_stdout_stderr  = True,
                                                pad                 = 0,
                                                no_scrollbar        = True,
                                                do_not_clear        = True,
                                                )
                                            ],

                                 

                                ]
                            

        self.full_layouts = [ 

                            [   
                                
                                sg.Column( self.one_layouts         , background_color=COLORS_APP["AZUL_ESCURO_SINZENTO"] ) ,
                                sg.VSeparator() ,
                                sg.Column( self.lay_texts_informs   , background_color=COLORS_APP["AZUL_ESCURO_SINZENTO"]  ) 
                            ],

                            ]


        self.windons  = sg.Window( self.Name_Soft,
                                    background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                    size                = (1024,600) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events = True, 
                                    use_default_focus      = False

                                    ).layout(self.full_layouts)

        sg.cprint_set_output_destination(self.windons, self.ML_KEY)
    

    def makerDatas(self):
        layout = [  [sg.Text( "Nome do arquivo dtsl ",text_color = 'white' , 
                    background_color = COLORS_APP["AZUL_ESCURO_SINZENTO"], key = "_TEXT_01_" )],

                    [sg.Input('', enable_events=True,  key='_INPUT_1_') ,
                    sg.Button('Ok', size=(10 , 1), key='_OK_')],

                    [sg.Multiline(  "Digite aquie caso queria adicionar alguma descrição desse banco de datos.",
                                    size                = (80, 10), 
                                    border_width        = 0,
                                    background_color    = COLORS_APP["AZUL_ESCURO_2"],
                                    text_color          = COLORS_APP["VERDE_CLARO"], 
                                    write_only          = False, 
                                    key                 = "_MULTI_DESCRITIONS_", 
                                    reroute_stdout      = True,
                                    #focus               = True,
                                    echo_stdout_stderr  = True,
                                    pad                 = 0,
                                    no_scrollbar        = True,
                                    do_not_clear        = True,
                                    )],

                    ]

        win  = sg.Window( "Maker News Datas",
                                    background_color    = COLORS_APP["AZUL_ESCURO_SINZENTO"],
                                    size                = (480,150) ,
                                    #icon                = "Icon.ico",
                                    #titlebar_icon       = base64.icone , 
                                    #use_custom_titlebar = False ,
                                    return_keyboard_events = True, 
                                    use_default_focus      = False).layout( layout )


        path_ = str( self.values["_ADD_DATAS_PATH_"] ) + "/"

        while True:
            events , values = win.Read()#timeout=10
            if values == sg.WIN_CLOSED or values == "Sair":
                break

            if events == "_OK_":
                try:
                    with open( path_+  str( values["_INPUT_1_"] ) + ".dtsl" , 'w' ) as save_values:
                        save_values.write( "{ }" )

                        #self.windons[self.ML_KEY ].update("")
                    
                        list_files  = self.list_files(path_files = path_ )
                        self.windons["_LIST_"].update( list_files )
                except:
                    pass

    def list_files(self , path_files):
        files = path_files

        try:
            file_list = os.listdir(files)
        except:
            file_list = []

        file_names = [fileN for fileN in file_list if os.path.isfile(os.path.join(files,fileN))
        and fileN.lower().endswith((".dtsl"))] 

        return file_names

    def printCV(self , text_value , editor_text_color ):
        return sg.cprint( text_value ,  text_color = editor_text_color )
        pass

    def main(self):
        
        while True:
            self.events , self.values = self.windons.Read()#timeout=10
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            #if self.events:
               # print( self.events )


            if self.events == "_MAKER_NEW_FILE_":
                self.makerDatas()
                pass

            if self.events == "_ATUALIZE_LIST_" or self.events == "r:82":
                path_       = str( self.values["_ADD_DATAS_PATH_"] ) + "/"
                list_files  = self.list_files(path_files = path_ )
                self.windons["_LIST_"].update( list_files )

            
            if self.events == "_LIST_":
                load_data = {}

                try:
                    with open( path_ + str(self.values["_LIST_"][0]) , 'r' ) as openedfile:
                        load_data_read  = openedfile.read()
                        load_data       = literal_eval( load_data_read  ) 
                        load_formated   = literal_eval( pformat( load_data_read ) )

                        self.windons[self.ML_KEY ].update("")
                        self.printCV( text_value = load_formated , editor_text_color = COLORS_APP["VERDE_CLARO"] )
                        self.windons["_TEXT_01_"].update( str(self.values["_LIST_"][0]) )

                except:
                    pass

                
            if self.events == "_SAVE_VALUES_" or self.events == "s:83" :
            
                try:
                    tx   = str(self.values["_LIST_"][0]) 
                    txt  = tx.split(".dtsl")
                    path_ = str( self.values["_ADD_DATAS_PATH_"] ) + "/"


                    with open( path_+  txt[0] + ".dtsl" , 'w' ) as save_values:
                        save_values.write( self.values[self.ML_KEY] )

                        self.windons[self.ML_KEY ].update("")
                        self.printCV( text_value = load_formated , editor_text_color = COLORS_APP["AZUL_#12"] )

                        list_files  = self.list_files(path_files = path_ )
                        self.windons["_LIST_"].update( list_files )
                except:
                    pass


            if self.events == "_DELL_" or self.events == "x:88":
                try:
                    os.remove( path_ + str(self.values["_LIST_"][0]))
                    self.windons[self.ML_KEY ].update("")
                    list_files  = self.list_files(path_files = path_ )
                    self.windons["_LIST_"].update( list_files )
                except:
                    pass

                pass





app = AppBook()
app.main()