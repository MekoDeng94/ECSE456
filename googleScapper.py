import requests
from bs4 import BeautifulSoup
import re
from langdetect import detect

class Scrape:
    def __init__(self, term, startDate, endDate):
        """
        :param term: The term you want to search (string)
        :param startDate: The start date mm/dd/yyyy (string)
        :param endDate: The end date mm/dd/yyyy (string)
        """
        self.term = term
        self.startDate = startDate
        self.endDate = endDate
        self.url = 'https://www.google.com/search?q={0}&tbs=cdr:1,cd_min:{1},cd_max:{2}&tbm=nws'.format(self.term, self.startDate, self.endDate)

    def run(self):
        USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        response = requests.get(self.url, headers=USER_AGENT)
        soup = BeautifulSoup(response.text, 'html.parser')
        found_results = []
        rank = 1
        soup.f
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:

            title = result.find('h3', attrs={'class': 'r'})
            link = title.find('a', href=True)
            description = result.find('div', class_='st')

            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                if link != '#' and detect(description) == 'en':
                    found_results.append({'keyword': self.term, 'rank': rank, 'title': title, 'description': description, 'link': link, 'language':detect(description)})
                    rank += 1

        for articles in found_results:
            print(articles)

    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)

a = Scrape('amd', '09/01/2018', '09/01/2018')
a.run()