
tab = [1,2,3,4,5]

x = 0
#for i in xrange(len(tab)):
while 1:
	n = len(tab)
	i = n-1
	while tab[i-1] > tab[i] and i != 0:
		i = i-1;

	if i == 0:
		print 'DONE'
		break

	pivotIdx = i-1;
	pivotReplacementIdx = i;
	j = i

	while j < n:
		if tab[j] <= tab[pivotReplacementIdx] and tab[j] > tab[pivotIdx]:
			pivotReplacementIdx = j
			j = j+1
		else:
			j = j+1

	temp = tab[pivotIdx]
	tab[pivotIdx] = tab[pivotReplacementIdx]
	tab[pivotReplacementIdx] = temp

	#tidy up the tail
	head = tab[:pivotIdx+1]
	tail = tab[pivotIdx+1:]
	tail.sort()

	tab = head + tail

	print tab
	x = x+1


