
from gtts import gTTS

from playsound import playsound

 


Nome = "Edinaldo"

audio = "speech.mp3"

languange = "pt"

sp = gTTS(text= "Olá!! Meu nome é Seny, muito prazer " + Nome ,
	lang= languange,slow=False)

sp.save(audio)
playsound(audio)
