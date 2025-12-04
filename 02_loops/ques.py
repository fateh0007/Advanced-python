items = ["apple", "banana", "cherry", "date", "cherry"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item:", item)
        break
    unique_items.add(item)
    
    
sum = 0

while sum<10:
    sum+=1
    
print(sum)