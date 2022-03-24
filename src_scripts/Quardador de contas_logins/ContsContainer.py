
import PySimpleGUI as sg
from pprint import pprint, pformat
from ast import literal_eval
import re 
import os
import sys


sg.theme("DarkBlue")


Cores = [ "#ffffff"  , "#0091ff"]


class NovoCadastroC():
    def __init__(self):

        self.lay1 = [
                [sg.Text("Preencha os espaços abaixo e em seguida click em [Salvar_Login].",size=( 28, 3))],
                [sg.HorizontalSeparator(color=Cores[0],key="separador1")],
                [sg.Text("Nome do site:",size=( 15 , 1))    ,sg.Input(size=(20,1),key="input_1")],
                [sg.Text("Nome de Usuario:",size=( 15 , 1)) ,sg.Input(size=(20,1),key="input_2")],
                [sg.Text("Senha:",size=( 15 , 1))           ,sg.Input(size=(20,1),key="input_3")],
                [sg.Text("Email:",size=( 15 , 1))           ,sg.Input(size=(20,1),key="input_4")],
                [sg.Text("Data:",size=( 15 , 1))            ,sg.Input(size=(20,1),key="input_5")],
                [sg.HorizontalSeparator(color=Cores[0],key="separador2")] ,
                [sg.Canvas(canvas=None, background_color=Cores[1],size=(10, 80) )],
                ]

        self.lay2 = [
                [sg.Text("Escolha uma imagem para representação na lista de contas de logins.", size=( 38, 2))],
                [sg.HorizontalSeparator(color=Cores[0],key="separador3")],
                [sg.Text("IMG"),
                sg.Input(size=(25,1), enable_events=True ,key="FOLDER"),
                sg.FolderBrowse("Buscar") ],
                [sg.Canvas(canvas=None, background_color=Cores[1],size=(300, 200) )]
                ] 

        self.layout = [
                [sg.Canvas(canvas=None, background_color=Cores[1],size=(625, 70) )],
                [sg.HSeparator()],
                [sg.Column(self.lay1),
                sg.VSeparator(),
                sg.Column(self.lay2)
                ],
                [sg.HSeparator() , sg.Button("Salvar_Login", key="salvarlogin", size=(20,1)) , sg.HSeparator()]
                ]



        self.janela = sg.Window("HackerFake",size=(640,420)).layout(self.layout)

    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "salvarlogin":
                savedata = {"Nome_Site": self.values["input_2"] , "Nome_User":" nada_ainda "}

                with open( "conts_files/" + self.values["input_1"] + ".js" , 'w' ) as openedfile:
                    openedfile.write( pformat( savedata ) )
                    print("data saved to " + openedfile.name)
                    

class AppClass():
    def __init__(self):
        
        self.lay1 = [
                [sg.Button("NOVO", key="novo", size=(21,1))],
                [sg.Listbox(values=[] , enable_events=True,size=(22,18),key="list")],
                [sg.Button("Atualizar Lista", key="atu", size=(21,1))]
                ]

        self.lay2 = [
                [sg.Canvas(canvas=None, background_color=Cores[1],size=(400, 200) )],
                [sg.HorizontalSeparator(color=Cores[0],key="separador6")],

                [sg.Text("Nome do site       :"     ,size=( 15 , 1)) , sg.Text("--------------!------",size=( 15 , 1 ), key="tx1") ],
                [sg.Text("Nome de Usuario :"        ,size=( 15 , 1)) , sg.Text("--------------!------",size=( 15 , 1 ), key="tx2") ],
                [sg.Text("Senha                 :"  ,size=( 15 , 1)) , sg.Text("--------------!------",size=( 15 , 1 ), key="tx3") ],
                [sg.Text("Email                  :" ,size=( 15 , 1)) , sg.Text("--------------!------",size=( 15 , 1 ), key="tx4") ],
                [sg.Text("Data                    :",size=( 15 , 1)) , sg.Text("--------------!------",size=( 15 , 1 ), key="tx5") ]
                ]

        self.layout = [
                [sg.Canvas(canvas=None, background_color=Cores[1],size=(625, 70) )],
                [sg.HSeparator()],
                [sg.Column(self.lay1),
                sg.VSeparator(),
                sg.Column(self.lay2)
                ]]



        self.janela = sg.Window("HackerFake",size=(640,480)).layout(self.layout)


    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.events == "novo":
                j2 = NovoCadastroC()
                j2.Update()
                print("NOVA CONTA ")


            if self.events == "atu":
                files = "conts_files"
                try:
                    file_list = os.listdir(files)
                except:
                    file_list = []

                file_names = [
                    fileN
                    for fileN in file_list
                    if os.path.isfile(os.path.join(files,fileN))
                    and fileN.lower().endswith((".js"))
                    ]   
                self.janela["list"].update(file_names)



            elif self.events == "list":
                name = self.janela["list"].get() 
                try:
                    savedata = {}
                    self.janela["tx1"].update( name[0] )

                    with open( "conts_files/" + str(name[0]) , 'r' ) as openedfile:
                        openedfile.read( pformat( savedata ) )
                        print(openedfile)

                except :
                    pass
                








app = AppClass()
app.Update()