import requests


def getArticles(articleName):
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={articleName}&api-key=MA1X3jOQGn4WLW2mn0KqP4V6um21FNLa"
    response = requests.get(url)
    response = response.json()
    return response['response']['docs']
