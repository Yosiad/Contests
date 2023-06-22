inp=int(input())
for j in range(len(inp)):
    input_size=list(map(int, input().split()))
    dur=list(map(int, input().split()))
    ent_val=list(map(int, input().split()))
    tmp=0
    ind=-1
    max_val=0
    for i in range(len(dur)):
        if tmp+dur[i]<=input_size[1]:
            if ent_val[i]>max_val:
                ind=i
                max_val=ent_val[i]
        tmp+=1
    if ind!=-1:print(ind+1) 
    else: print(-1)