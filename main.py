# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True






def find_anagrams(exp1, exp2):
    exp1_no_space = exp1.replace(" ","")
    exp2_no_space = exp2.replace(" ","")    
    #print(exp1_no_space)
    #print(exp2_no_space)
    
    if len(exp1_no_space) == len(exp2_no_space):
        exp1_lower = exp1_no_space.lower()
        exp2_lower = exp2_no_space.lower()

        #rint(exp1_lower)
        #print(exp2_lower)
        re_order1 = ''.join(sorted(exp1_lower))
        re_order2 = ''.join(sorted(exp2_lower))
        
        
        #print(re_order1)
        #print(re_order2)        
        if re_order1 == re_order2:            
            return True
        else:
            return False
    else:
        return False


expression1 = input("Enter an expression: ")
expression2 = input("Enter second expression: ")
anagram_final_verdict = find_anagrams(expression1, expression2)
print(anagram_final_verdict)