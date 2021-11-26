import sys
import math

s, m = [int(i) for i in input().split()]
ans = []
outer = []
prev = None
mclist = []
for i in input().split():   
    maxclients = int(i)
    mclist.append(maxclients)
for i in range(m):
    inner = input()
    outer.append([])
    for j in inner.split():
        clients = int(j)
        outer[i].append(clients)
current = [] 
for i in range(m):
    current.append([])
    for j in range(s):
        
        if i == 0:
            ans.append([])            
            ans[i].append(math.ceil(outer[i][j] / int(mclist[j])))
            current[i].append(ans[i][j])            
        else:
            ans.append([])         
            new = math.ceil(outer[i][j] / mclist[j])
            prev = current[i-1][j]
            diff = new-prev
            ans[i].insert(j, diff)
            current[i].insert(j, ans[i][j] + prev)        


lines = "---" * 15
print("\n")
print(f'{lines} Solution {lines}')
print("\n")
for i in ans:
    for j in range(len(i)):
        if j == len(i)-1:
            print(i[j])
        else:
            print(i[j],end=' ')      

      
    
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

 
