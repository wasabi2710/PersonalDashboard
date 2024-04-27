import requests

#global module
def fetch_global_news():
    # Adjust the endpoint to fetch articles
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
    
    return articles_info[:10]

#hackernews (any news)
def fetch_exploit_news(sec):
    news_api = f"https://newsapi.org/v2/everything?q={sec}&apiKey=e99372e12b6a4933a13b10e9ea2a7f9d&language=en"
    news = requests.get(news_api)
    hacker_news = news.json()
    return hacker_news