#TO LOOP THROUGH AN ARRAY AND USE "X" TO GENERATE E as a symbol
#This method can be utilized in other programming languages

numbrs = [5,2,5,2,2]
for x in numbrs:
    print(f"x" * x)
******
numbrs = [5,2,5,2,2,2]
#first iterate over each array
for each_array in numbrs:
    #set a counter for the total array of numbers,
    #here 6 i.e 0-5, initiallizing it to an empty string
    count = ""
    #performing an operation within the range of each array figure
    for x in range(each_array):
        #add letter x to the empty string
        #in the number of times of each array figure
        count = count + "x"
    #print the total number of exes in each array
    print(count)
