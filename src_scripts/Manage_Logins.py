
import PySimpleGUI as sg
from pprint import pprint, pformat
from ast import literal_eval
import re 
import os
import sys

from DTSL import DTSaveLoad


dts = DTSaveLoad()



#dts.Save( name_data_save="TEST" , dict_datas={"":""} )
#dic = dts.Load( name_data_load="TEST" )




Cores = [ "#ffffff"  , "#0091ff"]
SIZE_TEXT_X_Y = ( 12 , 2)


class AppClass():
    def __init__(self):
        #sg.theme("DarkTeal7")
        sg.theme("Reddit")

        

        self.lay0 = [

                [sg.Listbox(values=( self.list_files() ),
                    select_mode=None, 
                    enable_events=True ,
                    size=(40,18),
                    bind_return_key=True,
                    key="list_box")],
                 [sg.Button("Atualizar lista", key="atualizar", size=(17,1)),
                    sg.Button("Deletar_Login", key="del", size=(17,1)) ]

                 ]


        self.lay1 = [
                [sg.Text("Nome   ")],
                [sg.In(key='nome_login_out')],

                [sg.Text("Email  ") ], 
                [sg.In(key='email_login_out')],

                [sg.Text("Senha ") ],
                [ sg.In(key='senha_login_out')],

                [sg.Text("Outro ") ],
                [ sg.In(key='outro_login_out')],

                #[sg.HSeparator()],
                [sg.Canvas(background_color=Cores[0],size=(2, 20) )],

                [sg.Multiline(default_text="Digite uma descrição caso queira.",size=(100, 8),
                    background_color=Cores[0] ,text_color=Cores[1] , key ="descrition_out")], 

                ]


        self.layout_tap_1 = [
                [sg.Canvas(background_color=Cores[0],size=(2, 5) )],
                [sg.Canvas(background_color=Cores[1],size=(720, 10) )],
                
                [sg.Column( self.lay0 ) , sg.VSeparator() ,sg.Column( self.lay1 ) ],
                [sg.Canvas(background_color=Cores[1],size=(720, 20) )],

                            ]


        self.lay2 = [
                [sg.Canvas(background_color=Cores[1],size=(700, 20) )],
                [sg.HorizontalSeparator(color=Cores[0],key="separador6")],

                [sg.Text("Nome_do_site  : " , size=(SIZE_TEXT_X_Y)) , sg.In(key='nome' )],
                [sg.Text("Email_usado   : " , size=(SIZE_TEXT_X_Y)) , sg.In(key='email')],
                [sg.Text("Senha_criada  : " , size=(SIZE_TEXT_X_Y)) , sg.In(key='senha')],
                [sg.Text("Outro              : " , size=(SIZE_TEXT_X_Y)) , sg.In(key='outr' )],

                [sg.Text("Adicionar uma pequena descrição.",size=(40 , 1))],
                [sg.Multiline(default_text="Digite uma descrição caso queira.",size=(100, 10),
                background_color=Cores[0] ,text_color=Cores[1] , key ="descr")],

                [sg.Button("Novo_login", key="new_login", size=(21,1))]

                ]


        self.lay3 = [
                    [sg.Text("Configuranções")],
                    ]

        self.layout_tap_2 = [
                    [sg.Text("Lado outro"),
                    sg.VSeparator(),
                    sg.Column(self.lay3 )]

                    ]


        self.layout = [
                [sg.TabGroup( 
                    [[ sg.Tab('Lista_de_logins',self.layout_tap_1),
                    sg.Tab('Adicionar_novo_logins',self.lay2) ,

                    sg.Tab('Crediots e Confingurações', self.layout_tap_2 ) ]] , border_width=0)]
                ]



        self.janela = sg.Window("MyLogins ",size=(740,480)).layout(self.layout)

#-----------------------------------------------------------------------------------
    def list_files(self):

        files = "conts_files"

        try:
            file_list = os.listdir(files)
        except:
            file_list = []

        file_names = [fileN for fileN in file_list if os.path.isfile(os.path.join(files,fileN))
        and fileN.lower().endswith((".dtsl"))] 

        return file_names


#-----------------------------------------------------------------------------------
    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            #------------------------------------------------------------
            if self.events == "atualizar":
                self.janela["list_box"].update( self.list_files() )

            elif self.events == "del":
                try:
                    os.remove( "conts_files/" + str(self.values["list_box"][0] ) ) 
                    self.janela["list_box"].update( self.list_files() )
                except:
                    pass


            elif self.events == "new_login":
                dts.Save( 
                        name_data_save  = self.values["nome"]  , 
                        dict_datas      = {"Nome_do_site"  : self.values["nome"] ,
                                            "Email_usado"  : self.values["email"] ,
                                            "Senha_criada" : self.values["senha"],
                                            "outros"       : self.values["outr"],
                                            "descrição"    : self.values["descr"]})

            if self.events == "list_box":
                load_data = {}

                try:
                    with open( "conts_files/" + str(self.values["list_box"][0]) , 'r' ) as openedfile:
                        load_data = openedfile.read()
                        load_data = literal_eval( load_data )


                        self.janela["nome_login_out" ].update( load_data["Nome_do_site"] )
                        self.janela["email_login_out"].update( load_data["Email_usado" ] )
                        self.janela["senha_login_out"].update( load_data["Senha_criada"] )
                        self.janela["outro_login_out"].update( load_data["outros"] )
                        self.janela["descrition_out"].update( load_data["descrição"] )
                        
                except:
                    pass
 



class login_wind():
    def __init__(self):

        sg.theme("Reddit")
        self.siz_x_canvs = 1 

        self.lay1 = [

                [sg.Canvas(background_color=Cores[0],s=(1,20) )],

                [sg.Canvas(background_color=Cores[0],s=(self.siz_x_canvs+23 , 1) ),
                sg.Image("Img/imagen_1.png")],

                [sg.Canvas(background_color=Cores[0],s=(self.siz_x_canvs,1) ),
                sg.Input(key="input_nome")],

                [sg.Canvas(background_color=Cores[0],s=(self.siz_x_canvs,1) ),
                sg.Input(key="input_senha")],

                [sg.Canvas(background_color=Cores[0],s=(self.siz_x_canvs+47 ,1) ),
                sg.Button("Entrar", key="entrar", size=(20,3))]

                    ]

        self.win = sg.Window("MyLogins ",size=(320,400) ,no_titlebar=False ).layout(self.lay1)

    #----------------------------------------------------------------------------------
    def Update(self):
        while True:
            self.events, self.values = self.win.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.values["input_nome"] == "Edinaldo" and self.events == "entrar":
                self.win.close()

                app = AppClass()
                app.Update()



appl = login_wind()
appl.Update()

#app = AppClass()
#app.Update()
