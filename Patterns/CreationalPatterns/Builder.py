from abc import ABC, abstractmethod
from enum import Enum


class Cutlery(Enum):
	pass


class Product(ABC):
	@property
	@abstractmethod
	def name(self):
		pass


class Sushi(Product):
	@property
	def name(self):
		return 'Sushi'


class Burger(Product):
	@property
	def name(self):
		return 'Burger'


class OrderBuilder(ABC):
	
	@abstractmethod
	def serve(self):
		pass
	
	@abstractmethod
	def pack(self):
		pass
	
	@abstractmethod
	def add_cutlery(self, cutlery: Cutlery):
		pass
	
	@abstractmethod
	def add_topings(self):
		pass
	
	@abstractmethod
	def add_gloves(self):
		pass
	
	@abstractmethod
	def get_ready_order(self) -> Product:
		pass


class SushiCutlery(Cutlery):
	FORKS = 'Fork'
	STICKS = 'Sticks'


class SushiOrderBuilder(OrderBuilder):
	
	def serve(self):
		print('Cooking sushi')
	
	def pack(self):
		print('Packed our sushi')
	
	def add_cutlery(self, cutlery: SushiCutlery):
		if cutlery == SushiCutlery.FORKS:
			print('Add forks')
		if cutlery == SushiCutlery.STICKS:
			print('Add sticks')
	
	def add_topings(self):
		print('Add soy sauce and wasabi')
	
	def add_gloves(self):
		pass
	
	def get_ready_order(self):
		return Sushi()


class BurgerOrderBuilder(OrderBuilder):
	
	def serve(self):
		print('Cooking burger')
	
	def pack(self):
		print('Packed our burger')
	
	def add_cutlery(self, cutlery: Cutlery):
		pass
	
	def add_topings(self):
		print('Add BBQ sauce')
	
	def add_gloves(self):
		print('Add gloves')
	
	def get_ready_order(self):
		return Burger()


class Packer:
	
	def __init__(self, order_builder: OrderBuilder):
		self.order_builder = order_builder
	
	def pack_sushi(self, cutlery: SushiCutlery):
		self.order_builder.serve()
		self.order_builder.add_topings()
		self.order_builder.add_cutlery(cutlery)
		self.order_builder.pack()
		return self.order_builder.get_ready_order()
	
	def pack_burger(self):
		self.order_builder.serve()
		self.order_builder.add_topings()
		self.order_builder.add_gloves()
		self.order_builder.pack()
		return self.order_builder.get_ready_order()


if __name__ == "__main__":
	print('Sushi Order:')
	packer = Packer(SushiOrderBuilder())
	order = packer.pack_sushi(SushiCutlery.STICKS)
	print(f'Order {order.name} is ready')
	
	print("-" * 50)
	
	print('Burger Order:')
	packer = Packer(BurgerOrderBuilder())
	order = packer.pack_burger()
	print(f'Order {order.name} is ready')
