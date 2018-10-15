import requests

from main.models import Article, Source


class News:

    def get_news(self):

        res = requests.get(url='https://newsapi.org/v2/top-headlines?',
                        params={'country': 'mx', 'apiKey': 'dc63b5dfd15f4de4b10a5426b42c7b54'})

        if res.status_code == 200:
            data = res.json()

            for article in data['articles']:
                obj, created = Source.objects.get_or_create(
                    name = article['source']['name']
                )

                Article.objects.create(
                    author=article['author'],
                    title=article['title'],
                    description=article['description'],
                    url=article['url'],
                    image=article['urlToImage'],
                    published=article['publishedAt'][0:10],
                    content=article['content'],
                    source=obj
                )



