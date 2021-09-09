from buscaWeb import BuscaWeb
from twittadora import Twittadora
import time


buscaWeb = BuscaWeb()
tuita = Twittadora()


emTeste = False # Para impedir solicitações inuteis nos testes
	
def buscaUltimoVideo(urlCanal):
	if(emTeste):
		return "UUpRh0Z0OvI"

                    
	conteudoPg = buscaWeb.busca(urlCanal)
	posiUrl=conteudoPg.index("videoId")+10
	idUltimoVideo = conteudoPg[posiUrl:posiUrl+11]
	
	return idUltimoVideo


def buscaVideoNovo(urlCanal):
	videoAtual = buscaUltimoVideo(urlCanal)
	ultimoVideo = videoAtual
	print(f"\n\n\n\nÚltimo vídeo: {ultimoVideo}")
	tentativa=1
	while(ultimoVideo==videoAtual):
		videoAtual = buscaUltimoVideo(urlCanal)
		print("\nNenhum vídeo novo:")
		print(videoAtual)
		print(f"Tentativa: {tentativa}")
		tentativa+=1		
		time.sleep(60)
		if(emTeste and tentativa == 3):
			avisaQueSaiu(videoAtual)		
	avisaQueSaiu(videoAtual)

def obterThumb(videoId):
	urlThumb = (f"https://img.youtube.com/vi/{videoId}/maxresdefault.jpg")
	try:
	       status_code = urllib.request.urlopen(urlThumb).getcode() # Verifica se a thumbnail existe nesse tamanho
	except:
	 	urlThumb  =  (f"https://img.youtube.com/vi/{videoId}/mqdefault.jpg")
	
	return(urlThumb)


def avisaQueSaiu(videoAtual):
	print(f"\nVídeo novo!!!\n{videoAtual}")
	thumb = obterThumb(videoAtual)
	mensagem = (f"Oi, aqui é o BotAí. Vídeo novo no ar! \nhttps://youtu.be/{videoAtual}")
	tuita.tweet_imagem(thumb,mensagem)





# urlCanal = "https://m.youtube.com/user/Paradoxo10/videos"
urlCanal = "https://m.youtube.com/channel/UCajKESR0MIWvN5qcPEAleBw/videos"

buscaVideoNovo(urlCanal)


	

