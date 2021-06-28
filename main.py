import requests
import json

def download_and_show_robots(url: str):
    url_robots = url + "/robots.txt"
    resp = requests.get(url_robots)
    text = resp.text
    print('start ' + '*' * 50)
    print(text)
    print('finish ' + '*' * 50)


def get_data(url, params):
    r = requests.get(url, params=params)
    print('Requests sent to:', r.url)
    return r.json()

if __name__ == '__main__':
    download_and_show_robots("https://ru.wikipedia.org/")
    data = get_data("https://api.pushshift.io/reddit/comment/search/", {"subreddit": "python"})
    with open("data.json", 'w') as fo:
        json.dump(data, fo)