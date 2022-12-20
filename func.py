n = int(input("Enter a num:"))
temporary = n
reverse = 0
       
while(n>0):
    reminder= n % 10
    reverse = reverse *10 + reminder
    n = n//10
       
    
       
print(reverse)

if (reverse==temporary):
    print("the number is palindrome")
else:
    print("the number aint palindrome")
       