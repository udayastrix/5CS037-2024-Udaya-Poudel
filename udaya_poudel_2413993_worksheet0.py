#Task 1
temps = [8.2, 17.4, 14.1, 7.9, 18.0, 13.5, 9.0, 17.8, 13.0, 8.5,
16.5, 12.9, 7.7, 17.2, 13.3, 8.4, 16.7, 14.0, 9.5, 18.3, 13.4, 8.1,
17.9, 14.2, 7.6, 17.0, 12.8, 8.0, 16.8, 13.7, 7.8, 17.5, 13.6, 8.7,
17.1, 13.8, 9.2, 18.1, 13.9, 8.3, 16.4, 12.7, 8.9, 18.2, 13.1, 7.8,
16.6, 12.5]
Cold=[]
Mild=[]
Comfortable=[]
for temp in temps:
    if temp<10:
      Cold.append(temp)
      Cold.sort()
    if temp>10 and temp<15:
        Mild.append(temp)
        Mild.sort()
    if 10<= temp < 20:
        Comfortable.append(temp)
        Comfortable.sort()
print("The cold temps are:",Cold, "\n")
print("The mild temps are:",Mild, "\n")
print("The comfortable temps are:",Comfortable, "\n")
#Task 2 
print("The total numbers of times it was mild was ",len(Mild) )
print("The total numbers of times it was mild was ",len(Comfortable) )
print("The total numbers of times it was mild was ",len(Cold) ,"\n")
#Task 3
Fahlist=[]
for temp in temps:
  Fah=(temp*9/5)+32
  Fahlist.append(Fah)
print("The temperature when converted to fahrenheit is given as", Fahlist,"\n" )
#Task 4 
Day=[]
Evening=[]
Night=[]
for temp in temps:
  if 0<=temp>8:
    Day.append(temp)
  if 8<=temp>16:
    Evening.append(temp)
  if 16<=temp>24:
    Night.append(temp)
print("The average temp in day is:", sum(Day) / len(Day) )

#Nested loop

#1
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
def sum_nested_list(nested_list):
    fsum=0
    for i in nested_list:
        if type(i) is list:
            fsum+=sum_nested_list(i)
        else:
            fsum+=i
    return fsum
print(f"The sum of nested list is {sum_nested_list(nested_list)}")

#2
def generate_permutations(s, i=0):

    if i == len(s):   
        print("".join(s))

    for j in range(i, len(s)):

        words = [c for c in s]
   
        # swap
        words[i], words[j] = words[j], words[i]
    
        generate_permutations(words, i + 1)

print(generate_permutations('abc'))

directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}

#3
def  calculate_directory_size(dir):
    fsum=0
    for i in dir:
        if type(dir[i]) is dict:
            fsum+= calculate_directory_size(dir[i])
        else:
            fsum+=dir[i]
    return fsum
print(f"The total size of directory is { calculate_directory_size(directory_structure)}")

#dynamic programming

#1
coins=[1,2,5]
amount=11
def min_coins(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1
print(f"{min_coins(coins,amount)}")

#2
string1="abcde"
string2="ace"
def longest_common_subsequence(s1,s2):
    dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)] 
    for i in range(len(s1) -1,-1,-1):
        for j in range(len(s2) -1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]
longest_common_subsequence(string1,string2)

#3
weights=[1,3,4,5]
values=[1,4,5,7]
capacity=7
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
knapsack(weights, values, capacity)

