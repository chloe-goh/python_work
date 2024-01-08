# changing the value of one element in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

# adding elements to the end of a list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append('ducati')
print(motorcycles)

## usually start by defining an empty list that will hold users' values, and append accordingly

# inserting elements into a list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# removing an item using del
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# removing an item using pop
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

## the popped value is the last item of the list (if not defined), and is stored separately
## use del when you want to delete an item and not use it anymore, use pop when you still need the item after removing it

# removing an item by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)