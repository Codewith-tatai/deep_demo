def pattern1(N):
        # Loop for each row
    for i in range(N):
            # Loop to print N stars in each row
        for j in range(i+1):
            print("*", end="")
            # Move to the next row after printing N stars
        print()
    
    # Call the pattern1 function with the argument n
#pattern1(n)
pattern1(5)


#we have to print 

"1
"12
"123
"1234
"12345"

#our code is

#def nForest(n: int) -> None:
def pattern3(N):
    for i in range(1,N+1):
        for j in range (1,i+1):
            print(j,end="")

        print()
        
#pattern3(n)
pattern3(5)