from sys import stdin
buyers = dict()
for line in stdin:
    curList = line.split()
    buyer = curList[0]
    product = curList[1]
    if buyer not in buyers:
        buyers[buyer] = dict()
    if product not in buyers[buyer]:
        buyers[buyer][product] = 0
    buyers[buyer][product] += int(curList[2])
for buyer in sorted(buyers):
    print(buyer, ':', sep='')
    cur = buyers[buyer]
    for product in sorted(cur):
        print(product, cur[product])
