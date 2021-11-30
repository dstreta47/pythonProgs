def inversion_cnt(test, n):
	temp_test = [0]*n
	return main(test, temp_test, 0, n-1)

def main(test, temp_test, left, right):
	inv_count = 0
	if left < right:
		mid = (left + right)//2
		inv_count += main(test, temp_test,left, mid)
		inv_count += main(test, temp_test,mid + 1, right)
		inv_count += merge(test, temp_test, left, mid, right)
	return inv_count

def merge(test, temp_test, left, mid, right):
	i = left
	j = mid + 1
	k = left
	inv_count = 0

	while i <= mid and j <= right:
		if test[i] <= test[j]:
			temp_test[k] = test[i]
			k += 1
			i += 1
		else:
			temp_test[k] = test[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1
	while i <= mid:
		temp_test[k] = test[i]
		k += 1
		i += 1
	while j <= right:
		temp_test[k] = test[j]
		k += 1
		j += 1
	for loop_var in range(left, right + 1):
		test[loop_var] = temp_test[loop_var]
		
	return inv_count

test = [5, 2, 16, 1, 5]
n = len(test)
print(inversion_cnt(test, n))
