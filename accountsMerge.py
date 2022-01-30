from collections import defaultdict

def accountsMerge(accounts):
    em_to_name = {}
    em_graph = defaultdict(set)

    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            em_graph[acc[1]].add(email)
            em_graph[email].add(acc[1])
            em_to_name[email] = name

    seen = set()
    ans = []
    for email in em_graph:
        if email not in seen:
            seen.add(email)
            q = [email]
            component = []
            while q:
                edge = q.pop(0)
                component.append(edge)
                for n in em_graph[edge]:
                    if n not in seen:
                        seen.add(n)
                        q.append(n)
            ans.append([em_to_name[email]]+ sorted((component)))    

    return ans            






accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
            
print(accountsMerge(accounts))

[['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], 
['Mary', 'mary@mail.com'],
 ['John', 'johnnybravo@mail.com']]
