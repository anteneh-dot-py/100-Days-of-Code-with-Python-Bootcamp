import random
#option 1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
draw=random.choice(friends)
print(f"{draw} will pay the bill")
# option 2
# draw=friends[random.randint(0,len(friends)-1)]
# print("option 2 draw",draw)