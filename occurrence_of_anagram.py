'''
Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
'''

def search(pat, txt):
        dict = {}
        for i in pat:
            if(i in dict):
                dict[i] += 1
            else:
                dict[i] = 1
        count = 0
        n = len(txt)
        i = 0
        j = 0
        l = len(pat)
        dict2 = {}
        while(j<n):
            if(txt[j] not in dict2):
                dict2[txt[j]] = 1
            else:
                dict2[txt[j]] += 1
            if(j-i+1 < l):
                j+=1
            elif(j-i+1 == l):
                if(dict.items() == dict2.items()):
                    count += 1
                dict2[txt[i]] -= 1
                if(dict2[txt[i]]==0):
                    dict2.pop(txt[i])
                i+=1
                j+=1
            
        return count     

txt = "aabaabaa"
pat = "aaba"

print(search(pat, txt))