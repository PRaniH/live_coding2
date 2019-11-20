#Length of the longest repeating substring
#Note to self: In a string of several characters it should return the length of the substring that is longest like abcccdeff = 3
#longRepeat("aaaa") = 4
'''Length of Longest Repeating Substring
In this problem you are given a string of alphabetic characters. You need to find the length of the longest substring of repeating characters.
Examples:
longRepeat("aaa") => 3
longRepeat("a") => 1
longRepeat("bdsagbgagggaaatttyyyyau") => 4
longRepeat("abcdefghijklmnopqrstuvwxyz") => 1
longRepeat("") => 0'''
#Algorithm: Compare if current char and last char same, if so increase count of current char count. Once it is different, 
# move current char to old char and start count char again. Last compare if new current char is greater than old char.

import math #What do we import

def longRepeat(user_string):
    count_current_char = 0
    count_last_char = 0
    
    for char in user_string:
        current_char = char
        
        if current_char == user_string[char+1]: #If current char and next char same
            count_current_char =+ 1 #Increase current character count
            #Next compare if current character count > last char count
            if count_current_char > count_last_char:
                count_last_char = count_current_char #Once our current char count is larger, make it equal last char
            else:
                continue

        else:
            #If not the same characters, check to see if count_current_char < count_last_char
            if count_current_char < count_last_char:
                continue #Do nothing, count_last_char is still holding the biggest count
            else:
                count_last_char = count_current_char #Make count_last_char hold the latest
                
        return count_last_char





def __init__ == __main__ ():
    
    user_string = "aaa"

    count_result = longRepeat(user_string)

    print(count_result)
