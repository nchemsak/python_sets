# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("Tesla")
showroom.add("Grand Marquis")
showroom.add("Mini Hardtop")
showroom.add("F150")

# Print the length of your set.
print(len(showroom)) #this prints the number '4'

# Pick one of the items in your show room and add it to the set again.
showroom.add("Tesla")

# Print your showroom. Notice how there's still only one instance of that model in there.
print(len(showroom))

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Ranger", "Tacoma"})
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('F150')
print(showroom)
