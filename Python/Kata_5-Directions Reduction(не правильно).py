arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
i = 0
while len(arr)>1:
	t1 = arr[i]
	t2 = arr[i+1]
	if (t1 == "NORTH" and t2 == "SOUTH") or (t2 == "NORTH" and t1 == "SOUTH") or (t1 == "EAST" and t2 == "WEST") or (t2 == "EAST" and t1 == "WEST"):
		arr.pop(i)
		arr.pop(i)
		i = -1
	i += 1
	if i+1 == len(arr) or len(arr) == 0:
		break
if len(arr) == 0:
	print('nil')
else:
	print(arr)
