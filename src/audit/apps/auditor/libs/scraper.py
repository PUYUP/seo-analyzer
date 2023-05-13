import requests

from threading import Thread
from queue import Queue
from bs4 import BeautifulSoup

from apps.auditor.models import News


class Worker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # get worker from the queue and expand the tuple
            href = self.queue.get()
            try:
                extract_cnn_news(href)
            finally:
                self.queue.task_done()


def get_latest_cnn_news():
    url = 'https://edition.cnn.com'
    page = requests.get(url)
    hrefs = []

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        cards_wrapper = soup.find_all('div',
                                      class_='container_lead-plus-headlines__cards-wrapper')

        for card in cards_wrapper:
            links = card.find_all('a', class_='container__link')

            for link in links:
                href = link.get('href', None)

                if href:
                    hrefs.append(f'{url}{href}')

        if len(hrefs) > 0:
            # prepare a queue to communicate with worker threads
            queue = Queue()

            # create 6 worker threads
            for t in range(6):
                worker = Worker(queue)
                worker.daemon = True
                worker.start()

            for href in hrefs:
                queue.put(href)

            queue.join()

        return hrefs
    return None


def extract_cnn_news(url: str):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')

        try:
            headline_subtext = soup.find('div', class_='headline__sub-text')
            title = soup.find(
                'h1', class_='headline__text').get_text(strip=True)
            author = headline_subtext.find(
                'span', class_='byline__name').get_text(strip=True)
            published = headline_subtext.find(
                'div', class_='timestamp').get_text(strip=True)
            published = published.replace('Published', '')
            published = published.replace('Updated', '')
            content = soup.find(
                'div', {'itemprop': 'articleBody'}).get_text(strip=False)

            # save to database
            defaults = {
                'content': content,
                'author_name': author,
                'published_at': published.strip(),
            }

            news, created = News.objects \
                .update_or_create(title=title, defaults=defaults)

            print(news.title)
        except:
            pass
