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