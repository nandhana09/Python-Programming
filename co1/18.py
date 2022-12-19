dict1={"Nandhana":21,"Neena":24}
dict2={"Niketha":21,"Merlin":20}
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)
dict3 = dict2.copy()
dict3.update(dict1)
print("Merge:",dict3)
