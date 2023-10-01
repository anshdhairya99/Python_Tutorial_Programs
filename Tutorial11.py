# Set

#s = set()
#print(s)
#print(type(s))
#l = [1, 2, 3,4]
#s_from_list = set(l)
#print(s_from_list)
#print(type(s_from_list))
#s.add(1)
#s.add(1)
#print(s)
#s.add(5)
#s.remove(5)
#print(s)

#s1 = s.union({1,2,3})
#print(s1)
#s1 = s.intersection({1,2,3})
#print(s1)
#print(len(s))
#print(max(s))
#print(s,s1)
#s1 = {4, 6}
#print(s.isdisjoint(s1))


# PRACTICE THE SET------------

s = set()
#print(s)
#print(type(s))
#l = [1,2,3,4,5]
#s_from_list = set(l)
#print(s_from_list)
#s.add(1)
s.add(1)
s.add(23)
#print(s)
#s1= s.union({1,2,3})
s1 = s.intersection({1,2,3})
print(s,s1)
print(len(s))
print(max(s))
s1 = {4,6}
print(s1)
print(s.isdisjoint(s1))