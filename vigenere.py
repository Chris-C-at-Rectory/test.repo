def keystr(p,key):
	stream=[]
	j=-1
	for i in range(len(p)):
		j=i
		while j>int(len(key))-1:
			j-=len(key)
			
		stream.append(key[j])
	return stream
def vigenere(p,keystream):
	alph='abcdefghijklmnopqrstuvwxyz'
	code=''
	for i in range(len(p)):
		q=alph.index(p[i])
		j=alph.index(keystream[i])
		x=(q+j)%26
		code+=alph[x]
	return code
