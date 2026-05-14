# Linear Search Program

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number to search: "))

found = False

for i in numbers:
    if i == search:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")
