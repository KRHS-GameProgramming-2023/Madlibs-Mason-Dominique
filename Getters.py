def getMenuOption (debug = False) : 
    if debug: print ( "getmenuoption function") 
    
    goodInput = False 
    
    while not goodInput : 
        option = input("please select an option: ")  
        option = option.lower () 
        if option == "q" or option == "quit" or option == "exit": 
            option = "q" 
            goodInput = True 
            
        if option == "1":
            option = "1"
            goodInput = True 
        
        else: 
            print ("please make a valid choice") 
    return option
        



def getWord (prompt, debug = False) : 
    if debug: print ( "getword function") 
    
    goodInput = False 
    
    while not goodInput : 
        word = input(prompt)  
      
        goodInput = True
        if isSwear (word) : 
            goodInput = False 
            print  ("don't use language like that") 
            
    return word


def getSport (prompt, debug = False) : 
    if debug: print ( "getsport function") 
    
    goodInput = False 
    
    sports =  ["soccer",
               "football", 
               "hockey", 
               "wrestling" ] 
    while not goodInput : 
        word = input(prompt)  
      
        goodInput = True
        if isSwear (word) : 
            goodInput = False 
            print  ("don't use language like that") 
        elif word.lower() not in sports:
            goodInput = False 
            print  ("sorry, I don't know that one.")
    return word
        
def isSwear    (word,debug = False):  
    if debug: print ( "isSwear function")  
    if word.lower() in swearlist:
        return True 
    else: 
        return False
     
swearlist = ["poop",
             "pee"
            ] 
