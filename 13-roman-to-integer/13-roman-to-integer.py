class Solution:
    def romanToInt(self, s: str) -> int:
        values = [1,5,10,50,100,500,100]
        userinput = []
        firstposition = -1
        secondposition = -1
        total = 0
        counted = 0
        for i in s:
            userinput.append(i)
        for i in userinput:
            firstposition +=1
            if (counted == 0):
                if i == "C":
                    if(firstposition < (len(userinput)-1)):
                        secondposition = firstposition+1
                        if((userinput[secondposition])=="D"):
                            total += 400
                            counted = 1
                            
                        elif(((userinput[secondposition])=="M")):
                            total += 900
                            counted = 1
                            
                        else:
                            total+=100
                            
                    else:
                        total+=100
                        
                elif i == "I":
                    if(firstposition < (len(userinput)-1)):
                        secondposition = firstposition+1
                        if((userinput[secondposition])=="V"):
                            total += 4
                            counted = 1
                            
                        elif(((userinput[secondposition])=="X")):
                            total += 9
                            counted = 1
                            
                        else:
                            total+=1
                            
                    else:
                        total+=1
                        
                elif i == "X":
                    if(firstposition < (len(userinput)-1)):
                        secondposition = firstposition+1
                        if((userinput[secondposition])=="L"):
                            total += 40
                            counted = 1
                           
                        elif(((userinput[secondposition])=="C")):
                            total += 90
                            counted = 1
                            
                        else:
                            total+=10
                            
                    else:
                        total+=10
                        
                elif i == "L":
                    total+=50
                    
                elif i == "D":
                    total+=500
                    
                elif i == "M":
                    total+=1000
                    
                elif i == "V":
                    total+=5
                    
            else:
                counted = 0
                continue
        return total
            
            
            
                    
            
        print(total)
                
                
                