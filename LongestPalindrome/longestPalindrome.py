def longestPalindromicSubSstring(string):

    longestPalindromeString = ''

    for i in range(len(string)):
        for j in range(i, len(string)):
            subString = string[i:j+1]
            if len(subString) > len(longestPalindromeString) and isPalindrome(subString):
                longestPalindromeString = subString

    return longestPalindromeString


def isPalindrome(string):

    leftIndex = 0
    rightIndex = len(string) - 1

    while (rightIndex > leftIndex):
        if string[leftIndex] != string[rightIndex]:
            return False

        else:
            leftIndex += 1
            rightIndex -= 1

    return True


print(longestPalindromicSubSstring('dfkjabcdedcbafkdfj'))
