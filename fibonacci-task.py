# First two terms
n1,n2 = 0,1
count = 0

# Showing Fibonacci terms
nterms = int(input("Enter number of terms: "))

# To check valid number of terms
if nterms <= 0:
    print("Plz Enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence to", nterms,":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < nterms:
        print(n1, end = " ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1