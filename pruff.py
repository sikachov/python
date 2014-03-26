number=raw_input("Enter the number: ")
number=number.split(" ")
pruf=[]
count=range(1,len(number)+3)
edges_el=[]
edges_code=[]
k=0
for i in number:
    pruf.append(int(i))


for i in xrange(1,len(pruf)+2):
    if i not in pruf:
        edges_el.append(i)
        edges_code.append(pruf[0])
        count.remove(i+1)
        pruf.remove(pruf[0])
        print i
        print pruf
        k+=1
edges_el.append(count[0])
edges_code.append(count[1])
print '\n'
print edges_el
print edges_code
