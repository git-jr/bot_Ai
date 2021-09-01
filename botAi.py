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

videoAtual = buscaUltimoVideo(urlCanal)
ultimoVideo = videoAtual
print(f"\n\n\n\nÚltimo vídeo: {ultimoVideo}")


i=1
while(ultimoVideo==videoAtual):
	videoAtual = buscaUltimoVideo(urlCanal)
	print("\nNenhum vídeo novo:")
	print(videoAtual)
	print(f"Tentativa: {i}")
	i+=1
	
	
print(f"\nVídeo novo!!!\n{videoAtual}")
thumb = obterThumb(videoAtual)
mensagem = (f"Oi, aqui é o BotAí. Vídeo novo no ar! \nhttps://youtu.be/{videoAtual}")

tuita.tweet_imagem(thumb,mensagem)
