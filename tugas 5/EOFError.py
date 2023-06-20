try:
	n = int(input())
	print(n * 10)
	
except EOFError as e:
	print(e)
