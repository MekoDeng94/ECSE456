import requests
from bs4 import BeautifulSoup
import re
from langdetect import detect
from runner.console_monochrome import Console
import datetime
import time

logger = Console()

def get_everything(q=None, from_param=None, to=None, language='en',
                   sort_by=None, page=0, page_size=10):
    date1 = datetime.datetime.strptime(from_param, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(to, '%Y-%m-%d')
    day = datetime.timedelta(days=1)

    results = {'articles': []}
    total_article = 0
    while date1 <= date2:
        day_result = get_on_one_day(q, date1.strftime('%m/%d/%Y'), language, sort_by, page, page_size)
        new_articles = len(day_result['articles'])
        total_article += new_articles
        logger.info('Going through page' + str(page) + ' of ' + date1.strftime('%m/%d/%Y') + '. Adding '
                    + str(new_articles) + " articles. Total articles: " + str(total_article))
        results['articles'].extend(day_result['articles'])
        time.sleep(5)
        date1 = date1 + day

    return results


def get_on_one_day(q=None, date=None, language='en',
                   sort_by=None, page=1, page_size=10):
    USER_AGENT = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    url = 'https://www.google.com/search?'
    formated_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    if q:
        url += 'q={0}'.format(q)

    if page_size:
        url += '&num={0}'.format(page_size)

    if date:
        url += '&tbs=cdr:1'

    if date:
        url += ',cd_min:{0},cd_max:{0}'.format(date)

    url += '&tbm=nws'

    if page:
        url += '&start={0}'.format((page-1)*page_size)

    response = requests.get(url, headers=USER_AGENT)
    soup = BeautifulSoup(response.text, 'html.parser')
    found_results = {}

    found_results.update({'status': 'ok'})
    found_results.update({'articles': []})
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        temp_article = {}
        title = result.find('h3', attrs={'class': 'r'})
        link = title.find('a', href=True)
        description = result.find('div', class_='st')

        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#' and (language == None or detect(description) == language):
                temp_article.update({'title': title, 'description': description, 'url': link,
                                     'publishedAt': formated_date, 'content': description, 'author': '',
                                     'language': detect(description)})
                found_results['articles'].append(temp_article)

    return found_results
def remove_tags(self, text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)
