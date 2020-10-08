from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def parse(self, url):
        self.url = url
        page = requests.get(self.url, self.headers)
        content = BeautifulSoup(page.content, 'html.parser')
        games = content.findAll('div', {'class': 'tab_item_name'})
        games_list = []
        games_link = content.findAll('a', {'class': 'tab_item'})
        games_link_list = []

        for game in games:
            a = game.text
            games_list.append(a)

        for link in games_link:
            a = link['href']
            games_link_list.append(a)

        self.games = ''

        for i, j in enumerate(games_list):
            self.games += '{} - {}\n'.format(j, games_link_list[i])

        return self.games
