# WebCrawler
Multi-Threaded WebCrawler
This is Multi-Threaded Web Crawler with a crawling page limiting condition.
The Crawler takes the URL from the user and scrape the relevant URL's from that page. Then it uses those URL's to further crawl and repeat the scrape until it meets the limiting condition.

It uses ThreadPoolExecutor from concurrent.futures library to support parallel execution and performance optimization.
Also, there is a timeout of 60 seconds for the URL to respond.

## Steps to Run
Open terminal inside Crawler Folder and run cmd: python3 MultiThreadCrawler.py
It will prompt you to 
1. Enter the URL
2. No of pages you want to crawl

Note: Python 3 is required to run the file
