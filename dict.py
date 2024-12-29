dict1= {2 :"orange" , 1 : "apple"}
dict2= {4 :"cherry"}
print(f"dictionary 1 is : {dict1} ")
l=list(dict1.items())
l.sort()
print('ascending order is:' , l)
l= list(dict1.items())
l.sort(reverse= True )
print('descending order is :', l)
print(f"dictionary 2 is :{dict2}")
dict1.update(dict2)
print(f"dictionary after merging : {dict1} ")
