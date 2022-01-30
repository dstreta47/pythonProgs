from collections import deque

def coinchnage(coins, amount):
    if amount == 0:
        return 0

    if amount in coins:
        return 1

    queue = deque([(amount,0)])
    lookup = set([amount])

    while queue:
        RA, CU = queue.popleft()
        if RA ==0:
            return CU

        for coin in coins:
            if RA-coin >=0 and RA-coin not in lookup:
                queue.append((RA-coin,CU+1))
                lookup.add(RA-coin)

    return -1   



coins = [2]
amount = 3
print(coinchnage(coins,amount))                         
