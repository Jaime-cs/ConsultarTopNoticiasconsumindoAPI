import requests
from config import CHAVE_API, URL_BASE_TOP_HEADLINES

def top_noticias(pais):
    """
    Retorna as top noticias do site newsapi.org
    :param pais: inserir o pais para perquisar as noticias
    :return: Lista de noticias do pais

    """
    url = f"{URL_BASE_TOP_HEADLINES}country={pais}&apiKey={CHAVE_API}"

    # COLETANDO DADOS EM FORMATO JSON
    resposta = requests.get(url).json()
    #print(resposta)

    #Pegando todos os artigos
    artigos = resposta['articles']
    #print(artigos)

    #Lista vazia para preencher com noticias
    noticias= []

    for artigo in artigos:
        noticias.append(f"{artigo['title']} ,"
                        f"Imagem: {artigo['urlToImage']}, "
                        f"Publicado em: {artigo['publishedAt']}")

        #print(noticias)
        return noticias




