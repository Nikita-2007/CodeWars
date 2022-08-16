def longest(a1, a2):
	s = a1+a2
	temp, arr = [], []
	for i in s:
		temp.append(i)
	[arr.append(i) for i in temp if i not in arr]
	arr.sort()
	return ''.join(arr)
#для локального запуска
print(longest("aretheyhere", "yestheyarehere"))
input()
#[li.append(x) for x in my_list if x not in li]
