import time


def calculate_time(start_time):
	end_time = time.time()
	
	elapsed_time = end_time - start_time
	print('Execution time:', elapsed_time * 1000, 'milliseconds')
