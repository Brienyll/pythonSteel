numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)


name = "brix"

nam = [char.upper() for char in name]

print(nam)

cubes = [i**3 for i in range(5)]

print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
