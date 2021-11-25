
def check_long_pali(test):
    current_longest = [0,1]
    for i in range(1,len(test)):
        odd = check_long2(test,i  - 1, i + 1)
        even = check_long2(test, i - 1 , i)
        longest = max(odd,even, key=lambda x: x[1]-x[0])
        current_longest =max(longest,current_longest,key=lambda x: x[1]-x[0])
    return test[current_longest[0]:current_longest[1]]

def check_long2(test,start,end):
    while start>=0 and end < len(test):
        if test[start] != test[end]:
            break
        start -=1
        end +=1
    return [start+1,end]    


test = 'abaxyzzyxf'
print(check_long_pali(test))
