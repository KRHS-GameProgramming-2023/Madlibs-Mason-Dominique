from Getters import * 

def story1 (debug = False):
    if debug: print ("story1 function") 
    print ("\n") 
    friendname1 = getWord(" enter a name: ", debug) 
    sport1 = getSport(" enter a sport: ", debug) 
    bodypart1 = getWord(" enter a bodypart: ", debug) 
    place1 = getWord(" enter a place: ", debug) 
    food1 = getWord(" enter a food: ", debug) 
    place2 = getWord(" enter a place: ", debug) 
    game1 = getWord(" enter a game: ", debug) 
    activity1 = getWord(" enter a activity: ", debug) 
    out = "\n" 
    out += " one day me and my friend," + friendname1 
    out += " were out playing " + sport1 
    out += " and he/she hurt their " + bodypart1
    out += ". then we went to " + place1  
    out += ". after, we went and got " + food1
    out += ". then we head back " + place2
    out += " and played " + game1
    out += ". then we decided to do " + activity1
    return out 



