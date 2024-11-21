# deep_demo
This is my first Git Repository.
Author-deep
def nForest(n:int) ->None:
    # Write your solution here.
    def pattern1(n):
    # This is the outer loop which will loop for the rows.
        for i in range(n):
        # This is the inner loop which here, loops for the columns
        # as we have to print a rectangular pattern.
            for j in range(n):
                print("* ", end="")
        
        # As soon as N stars are printed, we move to the
        # next row and give a line break otherwise all stars
        # would get printed in 1 line.
            print()
    pattern1(n)
