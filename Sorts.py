
def gnomesort(seq):
	i=0
	while i < len(seq):
		if i == 0 or seq[i-1] <= seq[i]:
			i += 1
		else:
			seq[i], seq[i-1] = seq[i-1], seq[i]
			i -= 1

def mergesort(seq):
	mid = len(seq)//2
	lft, rgt = seq[:mid], seq[mid:]
	if len(lft) > 1: lft = mergesort(lft) 
	if len(rgt) > 1: rgt = mergesort(rgt) 
	res = []
	while lft and rgt:
		if lft[-1] >= rgt[-1]: res.append(lft.pop())
		else: res.append(rgt.pop())
	res.reverse()
	return (lft or rgt) + res

def ins_sort_rec(seq, i): 
	if i==0: return
	ins_sort_rec(seq, i-1)
	j=i
	while j > 0 and seq[j-1] > seq[j]:
		seq[j-1], seq[j] = seq[j], seq[j-1] 
		j -= 1

def ins_sort(seq):
	for i in range(1,len(seq)):
		j=i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j-1], seq[j] = seq[j], seq[j-1] 
			j -= 1


def sel_sort(seq):
	for i in range(len(seq)-1,0,-1):
		max_j = i
		for j in range(i):
			if seq[j] > seq[max_j]: max_j = j 
		seq[i], seq[max_j] = seq[max_j], seq[i]