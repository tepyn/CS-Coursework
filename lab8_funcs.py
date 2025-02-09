'''
No description needed at this point. Fill in the functions below
according to the description provided. 

'''


# --------------------------------------------------------------
# 1) Numeric string sum
# --------------------------------------------------------------

def sum_words(items): #done
    '''
    Assume that items is a list of strings, which may or may not
    contain valid integers. For example, one such list might be:
    
    [ '1', '8', 'hello', '3', '5ive', '42'  ] (sum = 54)
    
    This function should return the sum of the integers, without
    crashing on non-digit strings. That is, 'hello' and '5ive'
    in the above example should not cause your function to crash.

    You can use the int() function to parse integer values from
    the strings, but you'll have to use a try/except block to 
    avoid runtime errors when parsing non-integer strings.

    Do NOT use if/else logic to test the strings. Use try/except 
    to catch runtime errors if they happen.

    '''
    total = 0
    for i in range(len(items)):
        try:
            total += int(items[i])
        except ValueError:
            i += 1
    return total # replace 'pass' with a return statement.
    
# --------------------------------------------------------------
# 2) Maximum population
# --------------------------------------------------------------

def max_pop(items): #done
    '''
    Assume that items is a list of tuples (country, population).
    Return the country with the largest population.
    Use exception handling to deal with a bad tuple, in which 
    case you return None.

    For example:
    
    max_pop([('China', 1389618778), ('India', 1311559204), ('US', 331883986)])
    would return 'China'

    max_pop([('China'), ('India', 1311559204), ('US', 331883986)])
    would return None, because ('China') is missing the population

    max_pop([('China', 1389618778), ('India', 'lots'), ('US', 331883986)])
    would return None, because 'lots' is not a valid integer

    Do NOT use if/else logic to test the tuple. Use try/except to 
    catch runtime errors if they happen.

    HINT: you do not need to say the type of exception, just say except

    '''
    try:
        biggest_pop = 0
        max_country = None
        
        for i in items:
            #unpack tuple
            country, population = i
            
            if population > biggest_pop:
                    biggest_pop = population
                    max_country = country
       
        return max_country
    except:
        return None # replace 'pass' with a return statement.
    
# --------------------------------------------------------------
# 3) Product by index
# --------------------------------------------------------------

def product_by_index(items, ids) :
    '''
    Assume items is a list of numbers.
    Assume ids is a list of integers.
    This function should return the product of the elements of 
    items at every index in ids
    If either items or ids is empty, return None.

    For example:
    product_by_index([5, 2, 9], [1, 0, 1, 1]) would return 40, 
    since 2 * 5 * 2 * 2 = 40.

    Use exception handling to handle IndexError exceptions
    when the index is out of bounds. In this case, return None.

    For example: 
    productindex([5, 2, 9], [1, 0, 1, 1, 5]) would return None.

    Do NOT use if/else to test index ranges. You should use
    a try/except block.    

    '''
    
    result = [1] * len(items)
    product = 1
    
    try:
        for i in ids:
            #multiple number base on occurence
            result[i] *= items[i]
        
        for j in result:
            #multiple all again
            product *= j
        
        return product    
    except IndexError:
        return None # replace 'pass' with a return statement.


# --------------------------------------------------------------
# 4) Coin counter
# --------------------------------------------------------------

def coins(s) :
    '''
    Assume s is a string representing coins, where q is for 
    quarter, p is for penny, d is for dime, and n is for nickel.

    Return the total amount of money that the string represents.
    
    If the string contains characters that cannot be converted 
    to coins, you should raise a ValueError exception.

    For example, 
    money('ppp') returns 3
    money('pnqqqnd') returns 96
    money('43') raises ValueError

    '''
    #variables
    pennies = 0
    nickels = 0
    quarters = 0
    dime = 0
        
    for i in s:
        #how many time the coin appears
        if i not in 'pndq':
            raise ValueError
        elif i == 'p':
            pennies += 1
        elif i == 'n':
            nickels += 1
        elif i == 'd':
            dime += 1
        elif i == 'q':
            quarters += 1
        
    total_coins = (25 * quarters) + (10 * dime) + (5 * nickels) + pennies
    return total_coins # replace 'pass' with a return statement.

# --------------------------------------------------------------
# 5) Name checker
# --------------------------------------------------------------

def check_name(first, last): #to do

    '''
    Assume first and last are strings. This function should
    check if first and last are valid names. A valid name begins
    with a capital letter, and the rest of the characters are 
    lowercase. 
    
    If the names are valid, return their concatenation in the 
    following form: 'last, first'. For example, if first is
    'Alex' and last is 'Ufkes', return 'Ufkes, Alex'

    If either name is not valid, raise a ValueError exception.
    '''
    try:
        #check for capital in both
        if not first or not last or not first.isalpha() or not last.isalpha():
            raise ValueError
        
        elif not first[0].isupper() or not last[0].isupper() or not first[1:].islower() or not last[1:].islower():
            raise ValueError
        
        return last +", " + first    
    
    except ValueError as e:
        raise e
    # replace 'pass' with a return statement.


# --------------------------------------------------------------
# 6) Integers from iterators
# --------------------------------------------------------------

def get_next_int(it): #to do

    ''' 
    Assume that 'it' is an iterator, NOT a list/sequence. Given
    the iterator, this function returns the next integer value
    produced by the iterator.

    If the iterator runs out of elements, and cannot produce 
    another integer, return None.

    Hint: Use the next() function to get elements, and be sure 
    to catch the StopIteration error when it occurs. 

    '''
    while True:
        try:
            value = next(it) 
            if isinstance(value, int):
                return value # replace 'pass' with a return statement.
        except StopIteration:
            return None

