import requests

def fetch_news(type_of_news, sec=None):
    """
    Fetches news based on the type specified.
    
    :param type_of_news: str, either 'global' or 'exploit'. Determines the type of news to fetch.
    :param sec: str, optional. Used only if type_of_news is 'exploit' to specify the section of news to fetch.
    :return: list, a list of dictionaries containing the title, description, and URL of each article.
    """
    if type_of_news == 'global':
        # Fetch global news
        news_api = "https://newsapi.org/v2/top-headlines?apiKey=e99372e12b6a4933a13b10e9ea2a7f9d&language=en"
        news = requests.get(news_api)
        global_news = news.json()
        
        # Extract and return the title, description, and link for each article
        articles_info = []
        for article in global_news['articles']:
            title = article['title']
            description = article['description']
            url = article['url']
            articles_info.append({'title': title, 'description': description, 'url': url})
        
        return articles_info[:50]
    elif type_of_news == 'exploit':
        # Fetch exploit news
        if sec:
            news_api = f"https://newsapi.org/v2/everything?q={sec}&apiKey=e99372e12b6a4933a13b10e9ea2a7f9d&language=en"
        else:
            raise ValueError("Section must be specified for exploit news.")
        
        news = requests.get(news_api)
        hacker_news = news.json()
        
        # Extract and return the title, description, and link for each article
        articles_info = []
        for article in hacker_news['articles'][:10]:  # Limit to the first 10 articles
            title = article['title']
            description = article['description']
            url = article['url']
            articles_info.append({'title': title, 'description': description, 'url': url})
        
        return articles_info
    else:
        raise ValueError("Invalid type of news specified.")