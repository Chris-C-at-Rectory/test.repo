a="abcdefghijklmnopqrstuvwxyz"
pt=input("Put in plaintext: ").lower()
k=input("inpput a key: ").lower()

ks=""
ct=""

#a for loop that generates keystream
for i in range(len(pt)):
	if i>=len(k):
		i-=len(k)
	ks+=k[i]

for i in range(len(pt)):
	x=a.index(pt[i])+a.index(ks[i])
	if x>=26:
		x-=26
	ct+=a[x]
print(ct)
