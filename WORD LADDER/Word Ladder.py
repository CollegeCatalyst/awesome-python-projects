# Python3 program to find length of the shortest chain transformation from source to target
from collections import deque
 
def shortestChainLen(start, target, D):
     
    if start == target:
      return 0
    if target not in D:
        return 0

    level, wordlength = 0, len(start)
 
   
    Q =  deque()
    Q.append(start)
 
    while (len(Q) > 0):
         
        level += 1
 
        sizeofQ = len(Q)
 
        for i in range(sizeofQ):
 
            word = [j for j in Q.popleft()]
            
 
            for pos in range(wordlength):
              
                orig_char = word[pos]
 
              
                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)
 
                    if ("".join(word) == target):
                        return level + 1
 
                    
                    if ("".join(word) not in D):
                        continue
                         
                    del D["".join(word)]
 
                    Q.append("".join(word))
 
                
                word[pos] = orig_char
 
    return 0
 

if __name__ == '__main__':
     
   
    D = {}
    D["poon"] = 1
    D["plee"] = 1
    D["same"] = 1
    D["poie"] = 1
    D["plie"] = 1
    D["poin"] = 1
    D["plea"] = 1
    start = "toon"
    target = "plea"
     
    print("Length of shortest chain is: ",
    shortestChainLen(start, target, D))