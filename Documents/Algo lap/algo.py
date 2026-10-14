stac1=[]
max_size=6

if len(stac1)<max_size:
    stac1.append(5)
    print("Enqueue",5)
if len(stac1)<max_size:
    stac1.append(15)
    print("Enqueue",15)
if len(stac1)<max_size:
    stac1.append(25)
    print("Enqueue",25)
if len(stac1)>0:
    stac1.pop(0)
    print("Dequeue",0)
if len(stac1)<max_size:
    stac1.append(35)
    print("Enqueue",35)
if len(stac1)<max_size:
    stac1.append(45)
    print("Enqueue",45)
if len(stac1)>0:
    stac1.pop(1)
    print("Dequeue",1)
if len(stac1)<max_size:
    stac1.append(55)
    print("Enqueue",55)
print (stac1.pop(-1))
if len(stac1)<max_size:
    stac1.append(65)
    print("Enqueue",65)
print(stac1)
