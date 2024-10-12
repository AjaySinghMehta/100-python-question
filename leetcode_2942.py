'''
ou are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

 

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1
'''
def findWordsContaining(words, x: str):
        result = []
        for i in range(len(words)):
            if(x in words[i]):
                result.append(i)
        return result
    
words = list(map(str,input().split()))
x = input('enter the alphabet')
print(words)
print(x)
output = findWordsContaining(words, x[0])
print(output)