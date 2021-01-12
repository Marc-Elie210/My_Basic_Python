def sum_int(num):
    """ This function sums up the integers from zero to num """
    total = 0 # Created an accumalator to store the running total
    if num != int(num): # This is to check if num is not an interger
        print('Answer = 0') 
        print('Wrong input...BYE!')
    else:
        for x in range (num+1): # This loop is looping through the rang of num+1 ex if num = 3 range is (0,4)
            total += x #computing the total for each x 
    return f'Here is your sum, {total}.' 



# num = 3# uncomment and enter a num here
sum_int(num) # calling the function with num in the parameter 