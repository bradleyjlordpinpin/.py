n = int(input("Enter a number:"))
end = int(input("Enter fibonacci's length: "))
list = []
for i in range(1, end):
    list.append(n)
    n += n
    

print(list)