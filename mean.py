# function that finds the mean of the numbers

def mean(*args):
    try:
        sum1 = sum(args)
    except TypeError:
        return "Argument must be an integer or a float"

    n = len(args)
    result = sum1/n
    return result
