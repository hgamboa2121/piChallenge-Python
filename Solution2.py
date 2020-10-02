data = None
with open('pi.txt') as f: 
    data = f.readline()

def isPalindrome(s): 
    return s == s[::-1]

def isPrime(n): 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

for i in range(len(data)): 
    seven = data[i:i+7]
    if isPalindrome(seven) and isPrime(int(seven)): 
        print("Answer: %s"%seven)
        break