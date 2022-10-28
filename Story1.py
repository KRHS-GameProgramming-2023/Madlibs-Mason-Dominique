from Getters import * 

def story1 (debug = False):
    if debug: print ("story1 function") 
    print ("\n") 
    friendname1 = getWord(" enter a name: ", debug) 
    sport1 = getSport(" enter a sport: ", debug) 
    
    out = "\n" 
    out += " one day me and my friend," + friendname1 
    out += " were out playing " + sport1 
    
    return out 



