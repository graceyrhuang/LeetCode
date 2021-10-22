def distoryHouse(queries):
	arr = [0] * len(queries)

	res = []
	for i, query in enumerate(queries):
		arr[query - 1] = 1
		print(arr)
		for pos in arr


	return res

queries = [2, 1, 3]
print(distoryHouse(queries))