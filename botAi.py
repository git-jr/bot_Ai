from buscaWeb import BuscaWeb
from twittadora import Twittadora

buscaWeb = BuscaWeb()
tuita = Twittadora()

def buscaUltimoVideo(urlCanal):
	conteudoPg = buscaWeb.busca(urlCanal)
	posiUrl=conteudoPg.index("videoId")+10
	idUltimoVideo = conteudoPg[posiUrl:posiUrl+11]
	
	return idUltimoVideo

def obterThumb(videoId):
	urlThumb = (f"https://img.youtube.com/vi/{videoId}/maxresdefault.jpg")
	
	return(urlThumb)



urlCanal = "https://m.youtube.com/user/Paradoxo10/videos"

urlCanal = "https://m.youtube.com/channel/UCajKESR0MIWvN5qcPEAleBw/videos"

video = buscaUltimoVideo(urlCanal)
print(f"\n\n\n\nÚltimo vídeo: {video}")


while(video==video):
	video = buscaUltimoVideo(urlCanal)
	print("\nNenhum vídeo novo:\n")
	print(video)
	
	
print(f"\nVídeo novo!!!\n{video}")
thumb = obterThumb(video)
mensagem = (f"Oi, aqui é o BotAí. Vídeo novo no ar! \nhttps://youtu.be/{video}")

tuita.tweet_imagem(thumb,mensagem)
