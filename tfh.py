import random
mylist = random.sample(range(25,40), random.randint(3, 7))
print(mylist)
a=mylist[1]
b=mylist[-2]
c=mylist[-3]
newlist=[a]+[b]+[c]
print(newlist)
import random
random.shuffle(newlist)
print(newlist)
