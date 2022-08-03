arr = [0, 1]
def fibonacci(n):
	while 1:
		leng = len(arr)
		if n < leng:
			return(arr[n])
		else:
			arr.append(arr[leng-1]+arr[leng-2])

#для локального запуска
print(fibonacci(70))
input()
