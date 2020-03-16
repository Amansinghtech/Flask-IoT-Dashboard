import sys

print("Start Writing here: - ")
user = sys.stdin.readlines()
print(user)

with open("sample.txt" ,"w") as file:
    file.writelines(user)