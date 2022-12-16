print("Enter the size of the file")
s1= int(input(" enter size 1 :"))
s2= int(input("enter size 2 :"))

total_size = s1 * s2
print(total_size)

total_bits = total_size * 24
print(f"the total size in bits is:{total_bits}")

total_bytes = total_bits / 8
total_bytes = int(total_bytes)
print(f"the total size in bytes is:{total_bytes}")
