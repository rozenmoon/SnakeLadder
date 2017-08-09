import random
dic = {4:22,10:18,15:36,22:76,56:98,42:7,65:12}
trials = []
i = 0
z = 50000
while i< z:
	i = i+1
	j=1
	num = 0
	while j < 100:
		num = num+1
		j = j+random.randint(1,6)
		if(j in dic):
			j = dic[j]
	trials.append(num)
_sum = 0

for i in trials:
	_sum = _sum+i
print(_sum/z)
