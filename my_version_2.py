#Caitlin McLaughlin, Lindsey Baratta, Matthew Mandelbaum
#I pledge my honor that I have abided by the Stevens Honor System.
#CS 115 Group Project, part 2

#############################
#Current Issues::

#Most user likes is sometimes returning wrong user

#save and quit file adds a new user for exitsing users, it doesn't rewrite the old one

#how popular is doesnt account for the current user

#show most popular doesnt work when there is one person

# preferences can duplicate !!!!
    #either show preferences or how preferences are saved has an issue

#delete preferences kinda doesn't work

#get reccomendations wont recommend for current user, it isnt icluding them i think
#       get recommendations also doen't work when one user, need to fix that
#   get matches - len of a none type object
#   the info seems to be saming as seperate lists which is stopping get recs from working

userName = ""
allUserPrefs = []
userPrefs = []
users = {}
def enterUser():
    '''Caitlin
    This function takes a users name and then takes their preferences.'''
    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ").title()
    return userName

def enterPreference():
    """
    returns a list of a the artist a user likes 
    """
    pref="startingstring"
    while pref != "":
        pref=input("Enter an artist that you like (Enter to finish): ").title()
        
        if pref =="":
            break
        if pref not in userPrefs:
            userPrefs.append(pref)
    users[userName] = userPrefs
    return userPrefs

def deletePreference():
    global userPrefs
    #check if the user has any preferences to delete
    if len(userPrefs) != 0:
        print("Current Preferences")
        count = 1
        for pref in userPrefs:
            print(str(count)+". "+pref)
            count = count + 1
        num = int(input("Please type in the number preference you would like to delete: "))-1
        #check if user entered a valid number
        if num < len(userPrefs):
            userPrefs = userPrefs[0:num] + userPrefs[num+1:]
    else:
        print("You have no preferences to delete")


def getReccomentdations():
    '''Matt'''
    best_match, amt_matches = findBestUser()
    #check if best_match is a valid user in allUserPrefs
    if best_match >= len(allUserPrefs):
        print("No recommendations available at this time.")
        return
    recs = getNonMatches(allUserPrefs[best_match])
    if amt_matches == 0:
        print("No recommendations available at this time.")
    else:
        for i in range(len(recs)):
            print(recs[i])
def getNonMatches(currUserPrefs):
    '''Matt'''
    r = []
    for i in range(len(currUserPrefs)):
        if currUserPrefs[i] not in r and currUserPrefs[i] not in userPrefs:
            r.append(currUserPrefs[i])
    return r

def getMatches(currUserPrefs):
    '''Matt'''
    r = []
    for i in range(len(sortedUserP)):
        if userPrefs[i] not in r and userPrefs[i] in currUserPrefs:
            r.append(userPrefs[i])
    return r

def findBestUser():
    '''Matt'''
    max_matches = 0
    best_index = 0
    for i in range(len(allUserPrefs)):
        matches = findMatches(allUserPrefs[i])
        if matches > max_matches and matches != len(allUserPrefs[i]):
            max_matches = matches
            best_index = i
    return best_index, max_matches

def findMatches(currUserPrefs):
    '''Matt'''
    matches = 0
    userPrefs.sort()
    currUserPrefs.sort()
    a = 0
    b = 0
    while a < len(userPrefs) and b < len(currUserPrefs):
        if(userPrefs[a] == currUserPrefs[b]):
            matches += 1
            a += 1
            b += 1
        elif(userPrefs[a] < currUserPrefs[b]):
            a += 1
        else:
            b += 1
    return matches

def showMostPop():
    ''' returns the most popular artist'''
    counter = 0
    num = allUserPrefs[0]
    if allUserPrefs:
        for i in allUserPrefs:
            curr_freq = allUserPrefs.count(i)
            if (curr_freq>counter):
                counter = curr_freq
                num = i
    else:
        for i in userPrefs:
            curr_freq = userPrefs.count(i)
            if (curr_freq>counter):
                counter = curr_freq
                num = i
    print("The most popular artist is: ", num)
    return num
    

#How Popular is the most popular artist-Lindsey

def howPopmostPop(): #just switch to universal dictionaty
    """
    returns the count of an artist who appears the most of
    users preferences -Lindsey Baratta
    """
    art_dict={}
    for key in users.keys():
        #check if user is in private mode
        if key[-1] != "$":
            for artist in users[key]:
                if artist in art_dict:
                    art_dict[artist] = art_dict[artist] + 1
                else:
                    art_dict[artist] = 1
                
    likes = list(art_dict.values())
    likes.sort()
    if len(likes) == 0:
        print("Sorry, no artists found.")
    else:
        print("The most liked artist has ",likes[-1], " likes.")
    print()
    
    

def MostArtisitLikes(user_list):
    """
    helper function for HowPopmostPop;returns the artist that
    has received the most likes -Lindsey Baratta
    """
    likes_dictionary={}
    for i in user_list:
        if i in likes_dictionary:
            likes_dictionary[i]+=1
        else:
            likes_dictionary[i]=1

    artist_likes=[]
    for n in likes_dictionary:
        artist_likes +=[n,likes_dictionary[i]]
        
    final_list.sort(key=lambda a:a[0])
    final_list.reverse()
    return final_List[0][0]
    
def saveAndQuit():
    with open("musicrecplus.txt", "w") as file_object:
        for key in users.keys():
            if key != userName:
                file_object.write(key + ":" + ",".join(users[key])+"\n")
        file_object.write(userName + ":" + ",".join(userPrefs)+"\n")
        file_object.close()

#Who likes the most artists-Lindsey
def mostUserlikes(): 
    """
    returns the user that likes the most artists -Lindsey Baratta
    """
    #only returnig current user
    max_likes = 0
    max_likes_key = 0
    for key in users.keys():
        '''check if user is in private mode'''
        if key[-1] != "$":
            curr_likes= len(users[key])
            if curr_likes > max_likes:
                max_likes = curr_likes
                max_likes_key = key
    if max_likes == 0:
        print("Sorry, no artists found.")
    else:
        print(max_likes_key)
    print()

def showPreferences():
        """
        Returs updated list of users preferences -Lindsey Baratta
        """
        if userName in users:#dicitornary is for however we are storing data
            return print("Current Preferences: ", users[userName], "\n")
        else:
            return print("No preferences found \n")
        
def togglePrivateMode():
    global userName
    if userName[-1] == "$":
        users.pop(userName)
        userName = userName.strip("$")
        #users[userName] = userPrefs
        #testing to remove duplictes
        print("Private mode now off")
    else:
        users.pop(userName)
        userName = userName + "$"
        #users[userName] = userPrefs
        #testing to remove duplicates
        print("Private mode now on")

def convert_to_user(line):
    colon = line.find(":")
    if colon != -1:
        user_name = line[0:colon]
        prefs_as_string = line[colon+1:]
        prefs = prefs_as_string.split()
        return user_name, prefs
    else:
        return "", ""

def start():
    """Matt
        Function that sets up program for the main loop.
        Checks if user aleady exists, gets prefences, etc.
    """
    global userName, userPrefs, users, allUserPrefs
    #grab user name
    userName = enterUser()
    #open musicrecplus.txt, or create it if it does not exist
    with open("musicrecplus.txt", "a") as file:
        file.close()
    #now the file has been created if it didn't exist before, check if current user exists in file
    with open("musicrecplus.txt", "r") as music_recs:
        Lines = music_recs.readlines()
        for line in Lines:
            name, recs = convert_to_user(line)
            #if error occurs while converting to strings, don't covert
            if name != "":
                users[name] = recs
                #if recs are not connected to current user, and aren't private, add to allUserPrefs
                if name != userName and name[-1] != "$":
                    allUserPrefs.append(recs)
        music_recs.close()
    #check to see if user exists in the database
    #if user enters name in private mode, check if username not in private mode exist.
    #and check other way around if the opposite is true
    if userName[-1] == "$":
        check = userName.strip("$")
    else:
        check = userName + "$"
    if userName in users:
        #user already exists, show the menu
        userPrefs = users[userName]
        main()
    elif check in users:
        #user exists in database but not in format given by the user
        userPrefs = users[check]
        #save user in users dictionary in the mode they specified
        users.pop(check)
        users[userName] = userPrefs
        main()
    else:
        #user does not exist, prompt them to enter their preferences
        userPrefs = enterPreference()
        #users[userName]= userPrefs
        main()

def main():
    global userPrefs
    '''Caitlin
    Main function to call and orginize the other functions.'''
    a = ("Enter a letter to choose an option:\n"
         "e - Enter preferences\n"
         "r - Get recommendations\n"
         "p - Show most popular artists\n"
         "h - How popular is the most popular\n"
         "m - Which user has the most likes\n"
         "s - show preferences \n"
         "d - delete preference \n"
         "t - toggle private mode on or off \n"
         "q - Save and quit\n")
    functionCall = input(a)
    if functionCall == "e":
        userPrefs = userPrefs + enterPreference()
        #users[userName] = userPrefs
    elif functionCall == "r":
        getReccomentdations()
    elif functionCall == "p":
        showMostPop()
    elif functionCall == "h":
        howPopmostPop()
    elif functionCall == "m":
        mostUserlikes()
    elif functionCall == "s":
        showPreferences()
    elif functionCall == "d":
        deletePreference()
    elif functionCall == "t":
        togglePrivateMode()
    elif functionCall == "q":
        saveAndQuit()
        return print("Goodbye!")
    else:
        functionCall = input(" Invalid input, please try again. \n" + a)
    main()
        
start()
