# importando os módulos  
import os 
import tweepy  
import requests 
 
   
# detalhes pessoais 
consumer_key = "
consumer_secret = "
 
access_token ="
access_token_secret = "

# autenticação do app 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
   
# autenticação do usuário 
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)  
 
 
class Twittadora(object): 
    def init(self): 
        pass 
 
    # Faz um Tweet normal 
    def tweet(self, texto): 
        api.update_status(status = texto) 
 
 
    # Faz um Tweet com imagem 
    def tweet_imagem(self,url, texto): 
        filename = 'temp.jpg' 
        request = requests.get(url, stream=True) 
        if request.status_code == 200: 
            with open(filename, 'wb') as image: 
                for chunk in request: 
                    image.write(chunk) 
 
            api.update_with_media(filename, status= texto) 
            os.remove(filename) 
        else: 
            print("Não foi possível carregar a imagem")
