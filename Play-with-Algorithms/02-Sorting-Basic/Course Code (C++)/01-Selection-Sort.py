def selectionSort(num_list_const:list) -> list:
	num_list = list(num_list_const)
	for i in range(len(num_list)):
		min_index = i
		for j in range(i,len(num_list)):
			if num_list[j] < num_list[min_index]:
				min_index=j
			num_list[i],num_list[min_index]=num_list[min_index],num_list[i]
	return num_list
		
if __name__ == '__main__':
	a = [10,9,8,7,6,5,4,3,2,1]
	b = selectionSort(a)
	print(a)
	print(b)