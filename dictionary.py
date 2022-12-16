a={"Name":"Faith", "Age":20, "Class":"Year 11"}

a["Name"]="Clayton"

a.update({"Name":"Joe", "Age":30, "Class":"Year2"})
print(a)
a.update({"Name":"Faith"})
print(a)

print(a.values())
print(a.keys())
