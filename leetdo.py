#LeetCode Grim's contribution

#Function to calculate maximum wealth
def maximum_wealth(account):
    #Temporarily Empty list to keep track of all the total wealth of each account
    total_wealth_list = []
    #Nested loop to go through the 2D list
    for i in accounts:
        #Initialize variable to keep track of total individual account's wealth
        total_sum = 0 #This gets reinitialized to 0 after each i(per account) iteration for reusability
        #Nested loop j
        for j in i:
            #Add the value that j iterates over to the total sum
            total_sum += j

        #Append the value of total_sum after a single iteration of i (one account)
        total_wealth_list.append(total_sum)

    #Find out the maximum value out of all the elements in the total_wealth_list list
    max_wealth = max(total_wealth_list)
    #Return the maximum wealth as expected
    return max_wealth

#Input section
accounts = [[1,2,3],
            [3,2,3]
            ]
#List that keeps the account info [[a,b],[c,d]]
maximum_wealth(accounts)
# print(maximum_wealth(accounts)) --> Uncomment to see the output in terminal



#Below here is the question attached and commented

"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
"""

