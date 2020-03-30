import requests
from queue import Queue, Empty
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor

class Crawler:
    # constructor will initialize the variables
    def __init__(self, base_url, limit):
        self.limit = int(limit)
        self.base_url = base_url
        self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)
        self.visited_page_set = set([])
        self.pool = ThreadPoolExecutor(max_workers=15)
        self.crawl_queue = Queue()
        self.crawl_queue.put(self.base_url)
    
    # links_parser function parse the html of that link using BeautifulSoup
    # get the <a href=?> out of it and create a link to add it the queue
    def links_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            url = link['href']
            if url.startswith('/') or url.startswith(self.root_url):
                url = urljoin(self.root_url, url)
                if url not in self.visited_page_set:
                    self.crawl_queue.put(url)
                    print("     "+url)  

    # scrape_function returns res object if request to URL is successful
    def scrape_page(self, url):
        try:
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return
    
    # callback function to utilize multi-threading
    def after_scrape_callback(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.links_parser(result.text)

    # run_crawler binds all logic together. 
    # It fetches the URL from the queue and add it to the visited set
    # before submitting it to Thread pool
    def run_crawler(self):
        while self.limit > 0:
            try:
                current_url = self.crawl_queue.get(timeout=60)
                self.limit -= 1
                if current_url not in self.visited_page_set:
                    print(current_url)
                    self.visited_page_set.add(current_url)
                    job = self.pool.submit(self.scrape_page, current_url)
                    job.add_done_callback(self.after_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue

if __name__ == '__main__':
    url = input('Enter a URL to crawl(example: http://www.rescale.com/ ): \n')
    result = urlparse(url)
    while(all([result.scheme, result.netloc]) == False):
        url = input('Try Again: ')
        result = urlparse(url)
    limit = input('\nHow many pages should I Crawl: ')
    while(limit.isdigit() == False or int(limit)<=0):
        limit = input('Enter a valid integer value: ')
    output = Crawler(url, limit)
    output.run_crawler()