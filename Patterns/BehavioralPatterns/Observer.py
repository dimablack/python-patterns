from abc import ABC, abstractmethod
from typing import List


class IObserver(ABC):
	@abstractmethod
	def update(self, title: str):
		pass


class IObservable(ABC):
	
	@abstractmethod
	def subscribe(self, observer: IObserver):
		pass
	
	@abstractmethod
	def unsubscribe(self, observer: IObserver):
		pass
	
	@abstractmethod
	def notify(self):
		pass


class Post(IObservable):
	def __init__(self, title: str):
		self.__title = title
		self.__observers: List[IObserver] = []
	
	def update_title(self, title):
		print(f'Update title: {self.__title}')
		self.__title = title
		self.notify()
	
	def subscribe(self, observer: IObserver):
		self.__observers.append(observer)
	
	def unsubscribe(self, observer: IObserver):
		self.__observers.remove(observer)
	
	def notify(self):
		for observe in self.__observers:
			observe.update(self.__title)


class TitleWatcher(IObserver):
	def __init__(self, obj: IObservable):
		self.__post = obj
		obj.subscribe(self)
	
	def update(self, title: str):
		print(f'Title for post was changed to: {title}')


if __name__ == '__main__':
	post = Post('Nice title')
	
	title_watcher = TitleWatcher(post)
	
	post.update_title('Other pretty title')
