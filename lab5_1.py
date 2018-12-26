import sys

list = [1, 1.0, '1', -1, 1]

# def clean_list1(list_to_clean):
# 	for element in range(len(list_to_clean)):
# 		for elem in range(element-1):
# 			if list_to_clean[elem] is list_to_clean[element]:
# 				list_to_clean2 = list_to_clean
# 				list_to_clean = list_to_clean[:element]
# 				for e in range(element, len(list_to_clean)):
# 					list_to_clean[e] = list_to_clean2[e+1]
# 	return (list_to_clean)

# print(clean_list(list_to_clean))

def clean_list(list):
	for e in range(1, len(list)):
		for p in range(list.count(list[e])):
			for i in range(e, len(list)):
				if list[e-1] is list[i]:
					del list[i]

	return (list)

print(clean_list(list))