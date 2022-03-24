
import PySimpleGUI as sg





Cores = [ "#ffffff"  , "#0091ff"]



class AppClass():
    def __init__(self):
        
        self.lay1 = [
                [sg.Image("Img/loginimg.png")],
                #[sg.Canvas(background_color=Cores[1],size=(220, 200))],
                [sg.Canvas(background_color=Cores[1],size=(28, 5)) , sg.Text("FAÇA O SEU LOGIN "  ,size=( 15 , 1))],

                [sg.HorizontalSeparator(color=Cores[0],key="s1")],

                [sg.Input(size=(30,1),background_color="#e0e0e0",key="input_1")],

                [sg.Input(size=(30,20),background_color="#e0e0e0",key="input_2")],

                [sg.Canvas(background_color=Cores[1],size=(8, 5)) , sg.Button("ENTRAR", key="novo", size=(21,1))],

                ]



        self.lay2 = [
                [sg.Canvas(background_color=Cores[1],size=(400, 200))],
                [sg.HorizontalSeparator(color=Cores[0],key="separador6")],

                ]

        self.layout = [

                [ sg.Canvas(background_color=Cores[1],size=(625, 70)) ] ,
                #[sg.HSeparator()],

                [sg.Canvas(background_color=Cores[1],size=(180, 20)),
                sg.Column(self.lay1)]

                ]




        self.janela = sg.Window("Istliza",size=(640,480)).layout(self.layout)



    def Update(self):
        while True:
            self.events, self.values = self.janela.Read()

            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break







app = AppClass()
app.Update()