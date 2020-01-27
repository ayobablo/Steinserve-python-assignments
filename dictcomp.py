list_a=[1,2,3,4,5,6,7,8,9,0]

new_list=[num for num in list_a]

# dictionary comprehension must have a key and a value, {key:value}
dict_a={f"number_{num}": num for num in list_a}

print (new_list)
print (dict_a)
