# num_list = [0,1,2,3,4,5]
# print(list(map(lambda x:x*2,num_list)))
#
# print(list(filter(None,num_list)))


lst = map(str, [i for i in range(10)])
print(list(lst))
lst_2 = map(str, range(5))
print(list(lst_2))