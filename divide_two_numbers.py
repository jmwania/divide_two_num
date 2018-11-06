def divider_two_nummbers(x,y):
    #Raise exception to avoid a divide-by-zero

    if y == 0:
            raise ValueErro('Cannot divide by zero')
    return  float(x)/float(y)