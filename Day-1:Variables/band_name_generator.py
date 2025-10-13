print("Welcome to Band The Generator.")
city=input("What is the name of the city you grew up?\n")
pet=input("What's your pet's name?\n")
brand_name=city + " " + pet

# solution 1 set the result on brand_name variable
# print(f"Your Brand name could be {brand_name}")

# solution 2 concatinate the variable using python f string
print(f"Your Brand name could be {city} {pet}")
