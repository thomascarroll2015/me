TODO: Reflect on what you learned this week and what is still unclear.

Technical debt 
debt acquired from insufficient modularity or robustness

Naming is important and should always help the user in some way.

Comment as much as needed.

for i in range(3, 7):
        for j in range(3):
            r = requests.get(url + str(i))
            wd[i].append(r.text)