# -*-coding:utf8;-*-

import urllib.request
from unicodedata import normalize

import urllib.parse
import urllib.request

class BuscaWeb(object):
    def __init__(self):
        pass

    def gerarUrl(self, chave, site):  # Recebe uma palavara ou frase chave e a prepara para busca
        texto_busca = chave.replace(" ",
                                    "-")  # No lugar dos espaços vamos colocar sinais de adição "-" pois é assim que essa url de busca deve ser montada

        url = str(site + texto_busca)
        return url

    def busca(self, url):  # Faz uma busca com a URL (link) e devolve o código HTML da página
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
                   'Accept-Charset': 'ascii'}

        req = urllib.request.Request(url, headers=headers)
        retorno = str(urllib.request.urlopen(req).read()).encode("utf-8")
        retorno = retorno.decode("unicode-escape")
        # Os passo de "encode" e "decode" acima garatem que caracteres acentuados possam ser reconhecidos

        return retorno.replace("\n", " ")  # Retirada das quebras de linha (opcional)

    def buscaAscii(self, url):  # Faz uma busca com a URL (link) e devolve o código HTML da página
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
                   'Accept-Charset': 'ascii'}

        req = urllib.request.Request(url, headers=headers)
        retorno = urllib.request.urlopen(req).read()
        retorno = retorno.decode("utf8")
        # Os passo de "encode" e "decode" acima garatem que caracteres acentuados possam ser reconhecidos
       
        return retorno.replace("\n", " ")  # Retirada das quebras de linha (opcional)


    def start(self, busca, site, busca_padrao = True):
        try:
            cb = BuscaWeb()
            url = cb.gerarUrl(busca, site)

            if(busca_padrao):
                resultado = cb.responder(cb.busca(url))
            else:
                resultado = cb.responder(cb.buscaAscii(url))

            if resultado == "nenhum resultado":
                return resultado, False
            else:
                resultado = str(resultado)
                return resultado, True
        except:
            resultado = "não foi possivel concluir a busca"
            return resultado, False

