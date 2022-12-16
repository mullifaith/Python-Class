student = ["John", "Samuel", "Jane", "Job"]

for student in student:
    print("The characters in a",student)
    for char in student:
         print(char)

for x in range(20):
    print(x)


for m in range(1,20):
    print(m)


nums = [1, 2, 3, 4, 5, 6]

n = 7

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')
