def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
 
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
 
    for i in range(0,100):
        print("Third loop")
def my_function_complexity(n):
    # First Loop: Runs (n + 1) times -> O(n)
    # Second Loop: Doubles j each step until n -> O(log n)
    # Third Loop: Runs exactly 100 times -> O(1)
    
    # Total Time Complexity: O(n) + O(log n) + O(1) = O(n)
    print("Total Time Complexity: O(n)")
