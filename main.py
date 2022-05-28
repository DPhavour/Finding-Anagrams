# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(string1, string2):
    print("sorted string1", sorted (string1))
    if len(string1) != len(string2):
        print ("The words are not equal length.") 
        return False
    return sorted (string1.lower( )) ==sorted(string2.lower()) 

print(find_anagram("below", "elbow"))

