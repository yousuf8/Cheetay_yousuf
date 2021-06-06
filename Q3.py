def string_fun(str, low, high):
	
	for i in range(low, high + 1):
		print(str[i], end = "")

def longest_string_fun(str):
	n = len(str)
	max = 1
	start = 0
	
	for i in range(n):
		for j in range(i, n):
			flag = 1
		
			for k in range(0, ((j - i) // 2) + 1):
				if (str[i + k] != str[j - k]):
					flag = 0

			if (flag != 0 and (j - i + 1) > max):
				start = i
				max = j - i + 1
				
	print("Longest palindrome subString is: ", end = "")
	string_fun(str, start, start + max - 1)

	return max

	print("\nLength is: ", longest_string_fun(str))

