import time
from abc import ABC, abstractmethod
from helper import calculate_time

import requests as requests

cache = dict()


class Downloader(ABC):
	
	@abstractmethod
	def download(self, url: str):
		pass


class SimpleDownloader(Downloader):
	
	def download(self, url: str):
		print('Download real url')
		response = requests.get(url)
		content = response.content
		print('Downloaded bytes: ', len(content))
		return content


class CacheProxy(Downloader):
	
	def __init__(self, simple_downloader: SimpleDownloader):
		self._simple_downloader = simple_downloader
	
	def download(self, url):
		
		if url not in cache:
			print('CacheProxy skipped')
			content = self._simple_downloader.download(url)
			cache[url] = content
		else:
			print('CacheProxy iz in da house: Retrieving result from cache')
		
		return cache[url]


def client_code(downloader: Downloader):
	url = 'https://coinmarketcap.com/'
	downloader.download(url)


if __name__ == "__main__":
	st = time.time()
	print("Client: Download site from real")
	simple_download = SimpleDownloader()
	client_code(simple_download)
	calculate_time(st)
	
	print('-' * 55)
	
	st = time.time()
	print("Client: Download site from real")
	proxy = CacheProxy(simple_download)
	client_code(proxy)
	calculate_time(st)
	
	print('-' * 55)
	
	st = time.time()
	print("Client: Download site from cache")
	proxy_next_time = CacheProxy(simple_download)
	client_code(proxy_next_time)
	calculate_time(st)
	
	print('-' * 55)
