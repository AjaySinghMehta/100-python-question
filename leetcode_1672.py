'''

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.'''

length = int(input('enter length'))
accounts = []
for i in range(length):
    user = list(map(int, input().split()))
    accounts.append(user)
print(accounts)

def calculatingWealth(accounts):
    return max(sum(arr) for arr in accounts)

# method 2: 
def maximumWealth(accounts):
        max = float("-inf")
        for holder in accounts:
            wealth = sum(holder)
            if(max<wealth):
                max = wealth
        return max
    
    
output = calculatingWealth(accounts)
print(output)