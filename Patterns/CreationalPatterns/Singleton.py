class SingletonMeta(type):
	_instance = None
	
	def __call__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super().__call__(*args, **kwargs)
		return cls._instance


class DatabaseConnection(metaclass=SingletonMeta):
	connection_count = 0
	
	def __init__(self):
		self.connection_count += 1


if __name__ == '__main__':
	d1 = DatabaseConnection()
	d2 = DatabaseConnection()
	assert id(d1) == id(d2)
	print(f'd1: {d1.connection_count}')
	print(f'd2: {d2.connection_count}')
