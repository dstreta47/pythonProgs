
def test(interval):
    interval.sort(key=lambda x: x[0])
    start = interval[0][0]
    end = interval[0][1]
    m=[]
    for i in range(1,len(interval)):
        xxxx = interval[i][0]
        if interval[i][0]<=end:
            end = max(interval[i][1],end)
            start = min(interval[i][0],start)
        else:
            m.append((start,end))
            start = interval[i][0]
            end = interval[i][1]

    m.append((start,end))        
    return m        

interval = [(1,4),(2,5),(7,9)]
print(test(interval))
