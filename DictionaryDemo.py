d={110:"Aman",345:"Sumit",879:"Shruti",908:"Ashesh",333:"Jaymin",111:"Khushvantsinh",256:"Narottam",901:"Ami"}

print(d)
print(d[345])
d1=d.copy()
print(d1)
print(d.get(111))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(111))
print(d)
print(d.popitem())
d2={1:"Ami",2:"Khushvantsinh"}
d.update(d2)
print(d)
d[2]="S.p"
# d[112]="Kuldip"
print(d)

for i in d:
    print(i,"   ",d[i])