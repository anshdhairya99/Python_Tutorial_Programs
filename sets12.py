#SETS :--------


#s = set()
#print(type(s))
#s_from_list = set([1,2,3,4,5,6,7,8,9,10])
#print(s_from_list)
#print(type(s_from_list)) 
#s.add(1)
#s.add(1)
#s.add(2)
"""print(s) 
s1 = s.union({1,2,3})
s2= s.intersection({2,3,4})
print(s,s1)
print(s,s2)
print(len(s))
print(type(s))
print(min(s))
print(max(s))

s3 = {4,5,6}
print(s.isdisjoint(s3))
print(s.remove(2))"""

s1 = set([1,2,3,4,5]) 
print(s1)
print(type(s1))
s1.add(100)
s1.add(200)
s1.add(300)
s1.add(400)
s1.add(500)
print(s1)

s2 = s1.union({1,2,3})
print(s2)
s3 = s1.intersection({1,2,3})
print(s3)

s4 = {2,3,4}
print(s1.isdisjoint(s4))
s5 = {7, 8,9}
print(s1.isdisjoint(s5))
print(len(s4))
print(min(s4))
print(max(s3))
print(s4.remove(3))



