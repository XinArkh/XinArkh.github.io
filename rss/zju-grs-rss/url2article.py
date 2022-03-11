import requests
import rss_engine


api_url = 'http://url2api.applinzi.com/article'
my_token = 'BnYZtNTSRK-2mZ6zTtpgxg'


def get_article(url):
    html = rss_engine.get_url_content(url)
    query_string = {'token': my_token, 'url': url,}
    headers = { 'content-type': "text/html", }
    article = requests.post(api_url, params=query_string, headers=headers, data=html.encode('utf-8'))
    if article.status_code != 200:
        raise ValueError('Request response %d, expecting 200!' % article.status_code)

    return article.json()


if __name__ == '__main__':
    article = get_article('http://www.grs.zju.edu.cn/2022/0224/c1335a2500375/page.htm')
    print(article.keys())
    print(article)
