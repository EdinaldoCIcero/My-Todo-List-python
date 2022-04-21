from github import Github
import requests

# using an access token

gh      = Github("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")
repo    = gh.get_repo("EdinaldoCIcero/GitHubTestAPI")

user = gh.get_user()
print( "Nome de usuario ---> ", user.name ) 


dic     = { 
    "Nome" : " " , 
    "Idade" : " "
    }

imagem_test = "imgs/tesseract.png"


def downloadFile( url_f , endereço ):
    resposta = requests.get( url=  url_f )

    if resposta.status_code == requests.codes.OK:
        with open( endereço , "wb" ) as novo_file:
            novo_file.write( resposta.content )


#repo.create_file("img_test.png", "UpImagem" ,  str( imagem_test ) )

# LISTANDO CONTEUDOS DO RESPOSITORIO #
contents = repo.get_contents("")
test     = repo.get_contents( "datas.json" )
arq_txt  = repo.get_contents( "arquivo_novo.txt")

arq_png  = repo.get_contents( "tesseract.png")

list_contents   = []
url_down        = test.download_url
imag_url        = arq_png.download_url

avatar = user.avatar_url

downloadFile( url_f = imag_url , endereço = "IMAGEM_DOWNLOAD.png" )

downloadFile( url_f = avatar   , endereço = "GitHubAvatar.png" )

print( "Donwload Concluido com sucesso !")





#for content_file in contents:
    #list_contents.append( content_file )



#repo.update_file( path = arq_txt.path , message ="Atualização_0005 ", content = "Outro valor" , sha = arq_txt.sha )

#print( contents )
#print( test.path )



#-----------------------------------------------





#{'content': ContentFile(path="test.txt"), 'commit': Commit(sha="5b584cf6d32d960bb7bee8ce94f161d939aec377")}





