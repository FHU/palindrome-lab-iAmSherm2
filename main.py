#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.lower().replace(" ", "")
    if not word:
        return False
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
   user = str(input())
   result = palindrome(user)
   print(result)
