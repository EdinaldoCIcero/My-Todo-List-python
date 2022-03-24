import PySimpleGUI as sg
from gtts import gTTS
from playsound import playsound
from fpdf import FPDF
import PyPDF2 as pd




sg.theme("DarkGrey5") #'DarkGrey5'
tb = size=(10,0)

core_app = {"Separadore":"#363636" , 
            "Backgrounds":"#e0e0e0",
            "Butoes":"#1a1a1a"}



Nome = "Edinaldo"

languange = "pt"
audio = "speech.mp3"


#sp = gTTS(text= "Olá!! Meu nome é Seny, muito prazer " + Nome ,
   # lang= languange,slow=False)

#sp.save(audio)




class APP():
    def __init__(self):

        self.layout = [

            [sg.Button("Abrir aquivo TXT", key="criar", button_color=core_app["Butoes"],
                size=tb),sg.Button("Salvar Audio", key="criar", button_color=core_app["Butoes"], size=tb)],

            [sg.HorizontalSeparator(color=core_app["Separadore"] , key="separador1")],
            #[sg.Text("Titulo da pagina",size=(100,1))],

            #[sg.Input(size=(50,1),background_color="#e0e0e0",key="input_1")],

            [sg.HorizontalSeparator(color=core_app["Separadore"] ,key="separador2")],


            [sg.Multiline(default_text="Digite Aqui",autoscroll=True , size=(100, 20),
                background_color=core_app["Backgrounds"] ,text_color=None , key ="Mult")],
       

            [sg.Button("Play audio" , key="play", button_color=core_app["Butoes"] , size=(10,10))]

            ]


        self.janela = sg.Window("Covert Text Audio",
            background_color="#1a1a1a",
            no_titlebar = False, titlebar_background_color ="#5a5a5a", 
            use_custom_titlebar=False ,size=(640,480)).layout(self.layout)



    def main(self):
        while True:
            self.button, self.values = self.janela.Read()
            Space = "------------------ "
            NumbP = "\n-----------------------------------------------Pagina_ "

            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break

            if self.button == "play":
                

                sp = gTTS(text= self.values["Mult"] ,
                    lang= languange,slow=False)
                
                sp.save(audio)
                playsound(audio)



               # with open( str( "pages/" + self.values["input_1"] + ".txt") , "w" ) as openedfile:
                   # openedfile.write( self.values["Mult"] )





tel = APP()
tel.main()