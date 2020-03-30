# WebCrawler
This is Multi-Threaded Web Crawler with a crawling page limiting condition.<br/>
The Crawler takes the URL from the user and scrape the relevant URL's from that page. Then it uses those URL's to further crawl and repeat the scrape until it meets the limiting condition.

It uses ThreadPoolExecutor from concurrent.futures library to support parallel execution and performance optimization.
Also, there is a timeout of 60 seconds for the URL to respond.

## Approach
We utilize a thread pool to submit ‘tasks’ to this thread pool, allowing us to use a callback function to collect our results. This will allow us to continue with execution of our main program, while we await the response from the website.

We initialise a set which will contain a list of URLs which we have crawled so far. We will use this store URLs which have already been crawled, to prevent the crawler from visiting the same URL twice.

We then finally create a Queue which will contain URLs we wish to crawl, we will continue to grab URLs from our queue until it’s empty or it reaches limiting condition. Finally, we place in our base URL to the start of the queue to begin the crawl.

## Setup
We are using BeautifulSoup and requests which are not included by default in python3. Thus, to install manually<br/>
Run `pip3 install requests bs4` <br/>

## Steps to run
Open terminal at Crawler Folder<br/>
Run cmd: `python3 MultiThreadCrawler.py` <br/>

It will prompt you to 
1. Enter the URL
2. No of pages you want to crawl

## Steps to Run Test
run cmd: `python3 runTest.py`

Note: Python 3 is required to run the file
