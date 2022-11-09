from Getters import * 

def story3 (debug = False): 
    if debug: print ("story3 function")
    print ("/n") 
    friendname3 = getword (" enter a friend) ",debug) 
    color3 = getcolor (" enter a color) ",debug) 
    activity3 = getactivity (" enter a activity) ", debug) 
    place3 = getplace ("enter a place) ", debug) 
    sport3 = getsport ( "enter a sport) ", debug) 
    dvd3 = getdvd (" enter a dvd) ", debug) 
    park3 = getpark (" enter a park) ", debug) 
    bike3 = getbike (" enter a bike) ", debug) 
    
    out = "/n" 
    out += "5 years early me and my best friend" + friendname3 
    out += "chosed our favorite" + color3
    out += "we played an" + activity3 
    out += "we drived back to" + place3 
    out += "then we did" + sport3 
    out += "we got a" + dvd3
    out += "we went to the" + park3 
    out += "we rode our" + bike3 
    
    return out 
