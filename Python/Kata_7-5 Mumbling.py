def accum(s):
	arr = []
	for i in range(len(s)):
		temp = s[i]
		for j in range(i):
			temp += str(s[i])
		temp = temp.capitalize()
		arr.append(temp)
	return '-'.join(arr)
#для локального запуска

print(accum("ZpglnRxqenU"))
input()
