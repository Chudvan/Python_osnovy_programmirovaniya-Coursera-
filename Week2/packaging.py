l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())

if w1 > l1:     # w1 <= l1
    (l1, w1) = (w1, l1)
if w2 > l2:     # w2 <= l2
    (l2, w2) = (w2, l2)
if wc > lc:     # wc <= lc
    (lc, wc) = (wc, lc)

H = max(h1, h2)
W1 = max(w1, w2)
L1 = l1 + l2
if W1 > L1:
    (L1, W1) = (W1, L1)
W2 = max(w1, l2)
L2 = l1 + w2
if W2 > L2:
    (L2, W2) = (W2, L2)
W3 = max(w2, l1)
L3 = w1 + l2
if W3 > L3:
    (L3, W3) = (W3, L3)
W4 = max(l1, l2)
L4 = w1 + w2
if W4 > L4:
    (L4, W4) = (W4, L4)
if W1 <= wc and L1 <= lc and H <= hc:
    print('YES')
elif W2 <= wc and L2 <= lc and H <= hc:
    print('YES')
elif W3 <= wc and L3 <= lc and H <= hc:
    print('YES')
elif W4 <= wc and L4 <= lc and H <= hc:
    print('YES')
elif l1 <= lc and w1 <= wc and l2 <= lc and w2 <= wc and h1 + h2 <= hc:
    print('YES')
else:
    print('NO')
