string = input("Enter text : ")

string = string.lower(); 

words = string.split(" ") 


print("Duplicate words in a given string : ")  

for i in range(len(words)):  
    
	count = 1 
    
	for j in range(i+1, len(words)): 

       
   if(words[i] == (words[j])):  
            
		count+=1 
            
		words[j] = "0" 
    
	if(count > 1 and words[i] != "0"):  
        
		print(words[i])  