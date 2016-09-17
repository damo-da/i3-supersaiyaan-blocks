# does not need a shebang line because it is not meant to be executable

def get_bars_as_text(percentage, num_sticks=6):
    '''Returns bars in form of text to display controls like volume and brightness.

    Example: It returns the following lines
    ||||....
    ||||||||
    ........

    '''

    interval = int(100/num_sticks)

    sticks = int( (percentage+interval/2)/ interval)

    return "|"*sticks + "."*(num_sticks-sticks)


    while percentage > 10:
        ret[ret.index('.')] = '|'
        percentage -= 10
    return ret
 
if __name__ == "__main__":
    print(get_bars_as_text(10))
