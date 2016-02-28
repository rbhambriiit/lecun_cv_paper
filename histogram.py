vhist=[]
(rows,cols)=gray.shape
for c in range(cols):
    count=0
    for r in range(rows):
        count+=bw2[r,c]
    print("reading coln",c)
    count=count//255
    print("count is",count)
    vhist.append(count)
print(vhist)
