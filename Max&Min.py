#Final Assignment
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        a=int(num)
    except:
        print('Invalid input')
        continue        
    if a>=largest:
        largest=a
    if smallest is None:
        smallest=a
    if a<smallest:
        smallest=a
print("Maximum is",largest)
print("Minimum is",smallest)
