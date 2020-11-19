#Text Adventure: The Time Loop v.2.0

#Things that the player has to collect.
ApolloSong = False
ApolloMet = False
AsclepioFavour = False
scroll_piece2 = False
scroll_piece1 = False
ArtemisFavour = False
MoiraeHelped = False

#How users respond.

answer_A = ("A", "a")
answer_B = ("B", "b")
answer_C = ("C", "c")
answer_D = ("D", "d")
answer_E = ("E", "e")

answer_Y = ("Y", "y")
answer_N = ("N", "n")

#The intro is the "true" starting point of the game. When the loop is "restarted" it goes to the intro.
def intro():
    print("(EVERYTHING IS DARK)"
         "\nYou use your hands in an attempt to know where"
         "\nyou are. The ground is wet and covered in thick"
         "\nvines."
         "\nYou are... in a cave?"
         "\nWhen you press a stone, a mechanism is activated"
         "\nand releases the gigant boulder that was blocking"
         "\nthe entrance to the cave."
         "\n"
         "\nWhat do you do now?"
         "\n A. Go out directly through the entrance of the "
         "\ncave, towards the light."
         "\n B. Explore the depths of the cave, in darkness."
         "\n C. Descend the vines that extend through a "
         "\nbottomless hole.")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Cave_GetOut()
        elif response in answer_B:
            Cave_Explore()
        elif response in answer_C:
            Cave_Descend()
        else:
            print("Enter a valid choice")

def Cave_GetOut():
    print("You go out through the entrance of the cave. There "
          "\nis a incredible clarity but your eyesight adjusts "
          "\nto continue. "
          "\nYou look at your surroundings and see that you are "
          "\nnear a very high mountain, higher than coulds "
          "\nthemselves. You have never seen anything like it "
          "\nbefore. "
          "\nIn the distance you see a path that extends through "
          "\na small grove. "
          "\n"
          "\nNow what? "
          "\nA. A guy calls for you in the distance. See who they are."
          "\nB. Ignore the guy and just explore the surroundings.")
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            Outside_Apollo()
        elif response in answer_B:
            Apollo_exploration()
        else:
            print("Enter a valid choice")

def Outside_Apollo():
    print("Someone is calling you from afar. A normal guy. He "
          "\nhas a wide-brimmed hat. "
          "\n'Hello there Art... ummm... ups... Sorry, I "
          "\nconfused you with my sister... Oh... you are... "
          "\nwell, anyways...sorry, bye...'"
          "\n"
          "\n What do you do?"
          "\nA. Pressure the man to tell you what is going on. "
          "\nB. Letting his strange behaviour go and talking "
          "\nabout bland things."
          "\nC. You shrugg your shoulders. We all make mistakes.")
    ApolloMet = True
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Apollo_dialogue1()
        elif response in answer_B:
            Apollo_dialogue2()
        elif response in answer_C:
            Apollo_dialogue3()
        else:
            print("Enter a valid choice")

def Apollo_dialogue1():
    print("'Eh... look this is not an appropiate place to talk..."
          "\nsorry, goodbye!'")
    intro()
    #This option send the player to the intro.

def Apollo_dialogue2():
    print("'Yeah, I was looking for my sis because I haven't seen "
          "\nher here for a long time..."
          "\nWell, surely she is ok. She is a very capable person. "
          "\nIsn't this place amazing? Ahh... it is so idylic!"
          "\nBut, tell me. Do you want to know something "
          "\nspecifically?'"
          "\nA. 'Who are you?'"
          "\nB. Look at the lyre of the strange man. 'Could you " 
          "play a song?'"
          "\nC. Where are we?"
          "\nD. What is going on?"
          "\nE. It's been a pleasure to meet you, but I have to "
          "go.")
    response = ""
    while response not in answer_A or answer_B or answer_C or answer_D:
        response = input(">>> ")
        if response in answer_A:
            Apollo_dialogue2_1()
        elif response in answer_B:
            Apollo_dialogue2_2()
        elif response in answer_C:
            Apollo_dialogue2_3()
        elif response in answer_D:
            Apollo_dialogue2_4()
        elif response in answer_E:
            Apollo_dialogue2_5()
        else:
            print("Enter a valid choice")

def Apollo_dialogue2_1():
    print("'Me? I am a traveller, just like you. I travel around "
          "\nthe world as a minstrel. My music is the best in "
          "\nthe world. I don't want to be cocky about it but, "
          "\nyou know, I invented music so it's technically "
          "\ntrue...'"
          "\n'What?? Do you mean that you are the creator of "
          "\nmusic itself???'"
          "\n'Yep. Kinda. Do you want to know something else?' ")
    Apollo_dialogue2()

#ApolloSong = 1
def Apollo_dialogue2_2(): 
    print("'Of course! I'm gonna play a very important song. "
          "\nI want you to remember it well. After all, music "
          "\nis for sharing with others. Specially with an "
          "\nold lady...'"
          "\nThe man plays a song and you put all your efforts "
          "\nto remember it."
          "\n'That's all. Do you want something else?'")
    ApolloSong = True
    Apollo_dialogue2()

def Apollo_dialogue2_3():
    print("'This is a beautiful and magical region. One would "
            "\nthink that time does not run normally here. "
            "\nSee that mountain? Some people say that it's the "
            "\nMount Olympus. Others say that underneath it's the "
            "\nentrance to the Underworld. Who knows. Maybe both "
            "\nversions are true. "
            "\nSee that road over there? That path is the exit "
            "\nfrom this area... Well, more or less...'"
            "\n'More or less?'"
            "\n'Yep, they say that only the chosen ones can pass."
            "\n'Are you a chosen one?'"
            "\n'Well, I live around here so yes, technically I am '"
            "\na chosen one, I guess."
            "\n'And how you...'"
            "\n'That's a story I'd be happy to tell you other time."
            "\n Do you want anything else?'")
    Apollo_dialogue2()

def Apollo_dialogue2_4():
     print("'What do you mean?'"
     "\n'Yeah, you know, I don't know what's going on here, "
     "\nI woke up in a cave, I came out of it, and now I'm "
     "\nhere...'"
     "\nPhew, mate, looks like you took a pretty heavy "
     "\nnap... I'm sorry to tell you that I can't help you "
     "\nthere. Seriously, I am so sorry... Do you want "
     "\nsomething else?'")
     Apollo_dialogue2()
     
#With this option you leave the Apollo Dialogue and enter in 
#the "explore meadow" scenario.
def Apollo_dialogue2_5():
    print("'I feel the same way. Good luck on your journey!'")
    Apollo_exploration()

def Apollo_dialogue3():
    print("You shrugg your shoulders... Everything is so weird...")
    intro()

#Está algo repe pero xa se amañará.
def Apollo_dialogue4_exploration():
    print("You ignore that strange looking man and you decide to "
            "\nexplore this area:"
            "\nA. Explore the surroundings."
            "\nB. Lie under a tree."
            "\nC. Follow the road and go into the grove.")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            if AsclepioFavour == False:
                Apollo_exploration_AsclepioFavour_False()
            elif AsclepioFavour == True:
                Apollo_exploration_AsclepioFavour_True()
        elif response in answer_B:
            Apollo_exploration_tree()
        elif response in answer_C:
            Apollo_exploration_road()
        else:
            print("Enter a valid choice")
            
def Apollo_exploration():
    print("It's really an spectacular landscape."
         "you decide to explore this area:"
         "\nA. Explore the surroundings."
         "\nB. Lie under a tree."
         "\nC. Follow the road and go into the grove.")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            if AsclepioFavour == False:
                Apollo_exploration_AsclepioFavour_False()
            elif AsclepioFavour == True:
                Apollo_exploration_AsclepioFavour_True()
        elif response in answer_B:
            Apollo_exploration_tree()
        elif response in answer_C:
            Apollo_exploration_road()
        else:
            print("Enter a valid choice")
                   
def Apollo_exploration_AsclepioFavour_False():
    print("You walk calmly in the meadow. Although it's a "
          "\nbeautiful place, there is nothing remarkable that "
          "\ncould help you on your journey.")
    Apollo_exploration()
    
#Scroll_piece2 = 1
def Apollo_exploration_AsclepioFavour_True():
    print("After a lot of walking without finding anything "
          "\nremarkable, you look down by chance. In front "
          "\nof you there is a torn piece of paper. It "
          "\nseems to be missing another half. "
          "\nYou pick up the paper."
          "\n"
          "\n(YOU HAVE OBTAIN A SCROLL PIECE)")
    scroll_piece2 = True
    Apollo_exploration()

def Apollo_exploration_tree():
    print("You see a tree under which you could lie "
          "\ndown to rest. It's so nice out here and "
          "\nyou are so tired... ")
    if ArtemisFavour == True:
        Apollo_exploration_tree_ArtemisFavour_True
    elif ArtemisFavour == False:
        Apollo_exploration_tree_ArtemisFavour_False
        
def Apollo_exploration_tree_ArtemisFavour_False():
    print("Everything that happened had to be a "
          "\nnightmare. You are tired... and you "
          "\nfall asleep...")
    intro()

#scroll_piece1 = True
def Apollo_exploration_tree_ArtemisFavour_True():
    print("You follow Artemis' advice. Maybe you "
          "just need to clear your mind... You are "
          "\ntired and you fall asleep quickly..."
          "\nyou wake up for a moment and see a "
          "\ntorn piece of paper on your lap. It "
          "\nseems to be missing the other half."
          "\nYou pick up the paper."
          "\n"
          "\nYOU HAVE OBTAIN A SCROLL PIECE")
    scroll_piece1 = True
    intro()

def Apollo_exploration_road():
    print("As you go into the woods you are overcome "
          "\nby a sense of deja vù. Have you been here "
          "\nbefore?"
          "\nYou see the road fork. And between both "
          "\nof them there is an elderly man. As you approach "
          "\nhe stares at you."
          "\n"
          "\nWhat do you do?"
          "\nA. Come closer and talk to him."
          "\nB. Just ignore him and choose a way.")
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            Road_Asclepio()
        elif response in answer_B:
            Road_Asclepio_ChoosePath()
        else:
            print("Enter a valid choice")
            
def Road_Asclepio():
    print("'Well, well... it's you... I'm curious to know "
          "\nwhat you did to the old man so that he would "
          "\nbe so mad that he condemn you to this. I suppose "
          "\nit's very likely that I will never know. And "
          "\nneither you'."
          "\n"
          "\nA. 'Do you know who I am? What it's going on here?'"
          "\nB. 'Could you tell me which one is the right way?'"
          "\nC. Old man? You are pretty old, mate."
          "\nD. Well, I guess I can manage by myself to find "
          "\nthe right way.")
    response = ""
    while response not in answer_A or answer_B or answer_C or answer_D:
        response = input(">>> ")
        if response in answer_A:
            Road_AsclepioDialogue_1()
        elif response in answer_B:
            Road_AsclepioDialogue_2()
        elif response in answer_C:
            Road_AsclepioDialogue_3()
        elif response in answer_D:
            Road_Asclepio_ChoosePath()
        else:
            print("Enter a valid choice")
            
def Road_AsclepioDialogue_1():
    print("'Of course I know you. Everyone knows. But "
          "\nI am not allowed to tell you anything. It's "
          "\nnone of my bussiness anyway'.")
    Road_Asclepio()
    
def Road_AsclepioDialogue_2():
    print("'Why should I? To make the loop restart?'"
          "\nA. 'Please, help me!'"
          "\nB. 'I don't know what are you talking about "
          "\nbut the sooner you help me the sooner you "
          "\nwill be rid of me'"
          "\nC. 'You're a dick, I can manage without you!'")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Road_AsclepioDialogue_2_1()
        elif response in answer_B:
            Road_AsclepioDialogue_2_2()
        elif response in answer_C:
            Road_Asclepio_ChoosePath()
        else:
            print("Enter a valid choice")

def Road_AsclepioDialogue_2_1():
    print("'Oh, so you beg? Okay, I'll give you a hint, "
          "\nI don't care what the old man thinks."
          "\nThere is no right way'."
          "\n"
          "\n'ONLY THOUGH DARKNESS FREEDOM WILL BE "
          "OBTAIN'")
    intro()

#AsclepioFavour = 1
def Road_AsclepioDialogue_2_2():
    print("'That is a fair point. Look, why don't "
          "\ntake it easy. Take a walk or something. "
          "\nMaybe you will find a way...'")
    AsclepioFavour = True
    intro()

def Road_Asclepio_ChoosePath():
    print("Choose one path: "
          "\nA. Left."
          "\nB. Right.")
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            intro()
        elif response in answer_B:
            intro()
        else:
            print("Enter a valid choice")

def Road_AsclepioDialogue_3():
    print("Ohh... But I'm talking about someone you "
          "\nknew very well. I may be old, but the "
          "\nold man was there before everything else.")
    Road_Asclepio()

def Cave_Explore():
    print("You explore the depths of the cave and enter "
          "\nthe darkness."
          "\nIt's very dark, but your vision adjusts and "
          "\nyou continue. When you walk a bit, a sound "
          "\nrumbles behind you. You can deduce that "
          "\nsome kind of mechanism has been activated and "
          "\nnow you cannot go back."
          "\nYou realize that the path you are taking ascends"
          "\nin the form of a spiral. "
          "\n"
          "\nYou continue. The path is so long that you lose "
          "\ntrack of time... Until you finally find a door. "
          "\nSince it's your only option, you decide to enter."
          "\nSuddenly, a blinding light dazzles you. "
          "\nYou are on the outside, on the top of a mountain."
          "\nThere you can see a person."
          "\nIt's a young woman. She turns towards you."
          "\n"
          "\nWhat do you do?"
          "A. Ask her questions... Everything is so weird..."
          "B. Jump to the abyss.")
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            Artemis_Dialogue()
        elif response in answer_B:
            Artemis_JumpAbyss()
        else:
            print("Enter a valid choice")

def Artemis_Dialogue():
    print("'Oh, hello there. I didn't hear you coming. I'm "
        "\nsorry to tell you this so suddenly, but there's "
        "\nonly one way to leave this area... And I know you "
        "\n are not going to like it...'"
        "\n"
        "\nA. 'How can I leave this area?'"
        "\nB. 'Where are we?'"
        "\nC. 'Who are you?'"
        "\nD. 'Can you help me?'"
        "\nE. 'It's time for me to leave...'")
    response = ""
    while response not in answer_A or answer_B or answer_C or answer_D or answer_E:
        response = input(">>> ")
        if response in answer_A:
            Artemis_dialogue_1()
        elif response in answer_B:
            Artemis_dialogue_2()
        elif response in answer_C:
            if ApolloMet == True:
                Artemis_dialogue_3alt()
            elif ApolloMet == False:
                Artemis_dialogue_3()
        elif response in answer_D:
            Artemis_dialogue_4()
        elif response in answer_E:
            Artemis_dialogue_5()
        else:
            print("Enter a valid choice")
            
def Artemis_dialogue_1():
    print("'You will have to jump. You know, down there. I "
    "\nknow, it sounds crazy and scary but I assure you that "
    "\nyou are not going to feel a thing. Well, the other option "
    "\nis to stay here. For all eternity.")
    Artemis_Dialogue()

def Artemis_dialogue_2():
    print("'This is the Mount Olympus. Why are you making that "
    "\nface? Don't tell me you also expected it to be more "
    "\nimpressive... I guess I can't blame you. The stories "
    "\ntold about the Olympus give rise to imagination. And "
    "\nnothing real can compete with that. Not even something "
    "\nof divine proportions'."
    "\n"
    "\nA. If this is the Mount Olympus... Where are the gods?")
    response = ""
    while response not in answer_A:
        response = input(">>> ")
        if response in answer_A:
            Artemis_dialogue_2_1()
        else:
            print("Enter a valid choice")
    
def Artemis_dialogue_2_1():
    print("'I don't know. Moving around I guess. Doing more "
    "\ninteresting stuff than being here... I mean, the views "
    "\nare certainly impressive but in a couple of hundred "
    "\nyears you end bored of them easily'.")
    Artemis_Dialogue()

def Artemis_dialogue_3():
    print("'Artio, Bendis, Dali, Skade, Banka-Mundi, "
    "\nMielikki... but of all the names I have, Artemis "
    "\nis the one that humans recognize the most'.")
    Artemis_Dialogue()
    
#Alternative dialogue: If you have spoken with Apollo.
def Artemis_dialogue_3alt():
    print("'Artio, Bendis, Dali, Skade, Banka-Mundi, "
    "\nMielikki... but of all the names I have, Artemis "
    "\nis the one that humans recognize the best'."
    "\n"
    "\n'I think that your brother is looking for you'."
    "\n'Yes, surely... he is a sweetheart, he always "
    "\nworries about me. Anyway, in a moment I will go "
    "\nwith him'.")
    Artemis_Dialogue()

#ArtemisFavour = True
def Artemis_dialogue_4():
    print("'I'm afraid I cannot do it. But I recommend you "
     "\nenjoy the meadow below. You know, breath some fresh air "
     "\nand take a nap under a tree or something like that...'.")
    ArtemisFavour = True
    intro()
    
def Artemis_dialogue_5():
    print("You know what you have to do for it... It's a shame "
     "\nthat you have to jump to get out of this area... "
     "\nI have to ask Hefesto to fix the mechanism below. It's "
     "\nnot a problem to gods but for mortals..."
     "\n"
     "\nYou swallow and look down. The height is impressive "
     "\nand you can see the clouds from there... above, of course "
     "\nYou take a deep breath, close your eyes and jump the "
     "\nlongest you can... and suddenly...")
    intro()

def Artemis_JumpAbyss():
    print("\nYou swallow and look down. The height is impressive "
     "\nand you can see the clouds from there... above, of course "
     "\nYou take a deep breath, close your eyes and jump the "
     "\nlongest you can... and suddenly...")
    intro()

#This choices are repeated in "Hermes_dialogue()" because I thought that it could 
#be better to display (just the last text part).
def Cave_Descend():
    print("You descend through the vines, plunging into that "
          "\nbottomless void. It's dark and difficult to hold "
          "\non the vines, but your vision and muscles adapt."
          "\n"
          "\nYou hear a noise above your head. You can't go "
          "\nback. Something or someone has just blocked the "
          "\nthe exit."
          "\n"
          "\nYou continue to descend until you hear something..."
          "\nlike a wisper. Someone is calling you. "
          "\n'Hey... Hey there!'"
          "\n'It's me, Hermes! I'm here to guide you to freedom... "
          "\nYes, I know you're confused and probably don't"
          "\nremember who I am, but you have to believe me when"
          "\nI tell you that you have to defeat Cronos. He is "
          "\nthe one who locked you up here. Believe me. Cronos"
          "\nis watching you and as soon as you arrive to him"
          "\nhe is going to send you back to the begining, again"
          "\nand again'."
          "\n"
          "\n'This is the only place where he can't see you. He"
          "\nknows that you won't be able to escape this loop "
          "\non your own... but whith the help of others..."
          "\nIt's against the rules to interfere in the affairs"
          "\nof other gods openly. Here, I could give you a "
          "\nhand but the rest should do it in a more subtle "
          "\nway. If they help you in a direct way, the loop"
          "\nwill restart again and maybe they will get into"
          "\ntrouble'." 
          "\n'Besides, to face Cronos you must have in your hands "
          "\none of the most powerful artifacts on Olympus: the"
          "\nSCROLL OF AGES'."
          "\n"
          "\n'There is not much I cand do for you, but I can "
          "\nteleport you to the nearest gods':"
          "\n"
          "\nA. CRONOS. 'Send me to Cronos!'"
          "\nB. ASCLEPIO. 'I want to talk with Asplepio'."
          "\nC. ARTEMIS. 'I want to talk with Artemis'."
          "\nD. APOLLO. 'I want to talk with Apollo'."
          "\nE. (KEEP DESCENDING) 'Thanks, but I'm gonna "
          "\nkeep descending'.")
    response = ""
    while response not in answer_A or answer_B or answer_C or answer_D or answer_E:
        response = input(">>> ")
        if response in answer_A:
            Hermes_dialogueCronos()
        elif response in answer_B:
            Hermes_dialogueAsclepio()
        elif response in answer_C:
            Hermes_dialogueArtemis()
        elif response in answer_D:
            Hermes_dialogueApollo()
        elif response in answer_E:
            Hermes_DialogueKeepDescend()
        else:
            print("Enter a valid choice")
            
def Hermes_dialogue():
    print("\n'There is not much I cand do for you, but I can "
        "\nteleport you to the nearest gods':"
          "\n"
          "\nA. CRONOS. 'Send me to Cronos!'"
          "\nB. ASCLEPIO. 'I want to talk with Asplepio'."
          "\nC. ARTEMIS. 'I want to talk with Artemis'."
          "\nD. APOLLO. 'I want to talk with Apollo'."
          "\nE. (KEEP DESCENDING) 'Thanks, but I'm gonna "
          "\nkeep descending'.")
    response = ""
    while response not in answer_A or answer_B or answer_C or answer_D or answer_E:
        response = input(">>> ")
        if response in answer_A:
            Hermes_dialogueCronos()
        elif response in answer_B:
            Hermes_dialogueAsclepio()
        elif response in answer_C:
            Hermes_dialogueArtemis()
        elif response in answer_D:
            Hermes_dialogueApollo()
        elif response in answer_E:
            Hermes_DialogueKeepDescend()
        else:
            print("Enter a valid choice")
            
def Hermes_dialogueCronos():
    print("It would be great if it were that easy, but that "
        "\neasy, but that would give myself away. You'll have to "
        "\nfind another way.")
    Hermes_dialogue()

def Hermes_dialogueAsclepio():
    print("Ok, I'll send you where Asclepio is. He is just a "
        "\nlittle surly but I'm sure he will help you!")
    Road_Asclepio()

def Hermes_dialogueArtemis():
    print("Ok, I'm going to send you where Artemis is. I'm sure"
        "\nthat she will help you!")
    Artemis_Dialogue()

def Hermes_dialogueApollo():
    print("Ok, I'll send you where Apollo is. He is a kind guy. "
        "\nI'm not sure why mortals think that he is an arrogant "
        "\nperson... He will help you without a doubt!")
    Outside_Apollo()

def Hermes_DialogueKeepDescend():
    print("Ok, see you!"
        "\nYou keep descending slowly though the vines until you"
        "\nreach the bottom. It was not that ''bottomless'' after"
        "\nall...")
    if MoiraeHelped == True:
        Moirae_Helped()
    elif MoiraeHelped == False:
        Moirae_NotHelped()
    else:
        print("Enter a valid choice")
        
def Moirae_NotHelped():
    print("You see in the darkeness a inmense metal door. And"
     "\nguarding them a small old lady. "
     "\n"
     "\n'Greetings, traveller. My name is MOIRAE... I know who"
     "\nyou are and both of us know that the only way for you "
     "\nto scape this time prision is reaching Cronos..."
     "\nAnd I can help you with that'."
     "\n"
     "\n'If you cross these doors you will descend to the TARTARO"
     "\nThe place where titans dwell... including Cronos. I have"
     "\nthe key to cross this passage and I'll gladly give it to "
     "\nyou... if you make a little favour. Let me go home'. "
     "\n"
     "\nWhat? Are you surprise? You are not the only one that is"
     "\ntrapped in this dark and cursed code'."
     "\n'I wish I could say that the choice is yours but... There"
     "\nis no other choice I'm afraid'."
     "\nA. ENTER TARTARO.'Nothing personal, but I don't trust"
     "\nyou'."
     "\nB. HELP MOIRAE. 'Ok. A favour for a favour I guess'."
     "\nC. DON'T HELP MOIRAE. 'I'm sorry, but I can even help"
     "\nmyself, how am I supposed to help you?'")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Moirae_NotHelped_1()
        elif response in answer_B:
            if ApolloSong == False:
                Moirae_NotHelped_2_NoSong()
            elif ApolloSong == True:
                Moirae_NotHelped_2_Song()
        elif response in answer_C:
            intro()
        else:
            print("Enter a valid choice")
            
def Moirae_NotHelped_1():
    print("You try to open the Tartaro gates pushing them, "
     "\nbut they don't move at all. The old lady looks at you"
     "\nsmiling. It seems that you have made a fool of yourself...")
    intro()

def Moirae_NotHelped_2_Song():
    print("'This song... It was exactly what I needed to escape."
     "\nthank you stranger... I will fulfil my word'."
     "\n"
     "\nThe Tartaro's gates open while the old lady fade away..."
     "\n'But remember: reach Cronos it's not enough... you will"
     "\nneed something to defeat him... The SCROLL OF AGES...'"
     "\n"
     "\nThe gates are open for you. Do you want to enter the"
     "\nTARTARO?"
     "\nA. ENTER TARTARO. 'Here we go'."
     "\nB. GO BACK. 'No... I'm not ready, maybe I should...'")
    MoiraeHelped = True
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            Tartaro_enter()
        elif response in answer_B:
            intro()
        else:
            print("Enter a valid choice")

def Moirae_NotHelped_2_NoSong():
    print("The old lady sighs. 'It seem that you don't have"
     "\nwhat I need to return home... Please, try again after you"
     "\nexplore the surface'.")
    intro()
    
def Moirae_Helped():
    print("There you are again before the Tartaro's passage."
     "\nMoirae is not here. It seems that she is free for real."
     "\nThe gates are open." 
     "\n"
     "\nA. ENTER TARTARO. 'There we go'."
     "\nB. GO BACK. 'No... I'm not ready, maybe I should...'")
    response = ""
    while response not in answer_A or answer_B:
        response = input(">>> ")
        if response in answer_A:
            Tartaro_enter()
        elif response in answer_B:
            intro()
        else:
            print("Enter a valid choice")


#Esto pode que estea mal. Non sei se podo poñer a segunda opción como que o scroll1 ou o scroll2 sexa True e que non pete porq na terceira opción o scroll1 e o scroll2 teñen que ser true.
def Tartaro_enter():
    print("You cross the dor and enter into the darkness. You"
     "\nare not able to see anything at all. For a long stretch"
     "\nof the road you find your way blindly, with your hands."
     "\n"
     "\nStep by step, you notice a presence in the place. You"
     "\nknow who is there. You know he was waiting you."
     "\n"
     "\nSuddenly, everything was illuminated.")
    if scroll_piece1 and scroll_piece2 == False:
        Cronos_noScroll()
    elif scroll_piece1 or scroll_piece2 == True:
        Cronos_1Scroll()
    elif scroll_piece1 and scroll_piece2 == True:
        Cronos_2Scroll()
    
def Cronos_noScroll():
    print("'Well, well... It seems that you managed to reach me."
     "\nBut I have bad news for you. You are never going to be freed"
     "\nfrom this nightmare. You will stay here forever. Because"
     "\nthis is your punishment. You are never going to escape."
     "\nYou will come back here, again, and again... just to go"
     "\nback to the start'."
     "\n"
     "\nA. 'Why?? Why do you do this to me??'"
     "\nB. 'I don't understand, what I have done to you?!'"
     "\nC. 'Please... forgive me...'")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Cronos_noScrollDialogue_1()
        elif response in answer_B:
            Cronos_noScrollDialogue_2
        elif response in answer_C:
            Cronos_noScrollDialogue_3
        else:
            print("Enter a valid choice")

def Cronos_noScrollDialogue_1():
    print("You know why. Did you think that you could get "
     "\naway with it? You knew exactly what you get when"
     "\nyou defy a god. An agonic and eternal punishment."
     "\nAnd you did it anyways.")
    intro()

def Cronos_noScrollDialogue_2():
    print("You know what you did... or maybe your memory"
     "\nis begging to fickle? I guess it usually happens..."
     "\nNothing could give me more pleasure that seeing "
     "\nyou like this, you know?")
    intro()   

def Cronos_noScrollDialogue_3():
    print("You ask for forgiveness? After what you did"
     "\nwith complete malice and aforethought? C'mon, have"
     "\nsome dignity. There is no forgiveness for you. ")
    intro()

#Return to intro without scrolls. scroll_piece1 = False; scroll_piece2 = False
def Cronos_1Scroll():
    print("The piece of paper you found at some point in "
     "\nthe loop appears out of nowhere in your hands and"
     "\nshines brightly... but nothing happens... for a "
     "\nmoment you see some strange letters."
     "\n"
     "\n*********** eRrOR_sCRol_iNcOMpLEtE *************"
     "\n"
     "\n'Oh... It seems that someone has helped you... that"
     "\nwas unexpected. I guess I will have to find out who "
     "\nhas been. But that can wait. Did you really thought"
     "\nyou where going to scape your punishment? That's funny'."
     "\n"
     "\nThe scroll piece that you hold in your hands burns. "
     "\nBut not only physically. When you see the ashes fade"
     "\naway you know it has just disappeared from the temporal"
     "\nline.")
    scroll_piece1 = False
    scroll_piece2 = False
    intro()
    
#Seguramente haxa algunha mellor forma de chamar a mesma función para as mesmas respostas, pero bueno.
def Cronos_2Scroll():
    print("Before Cronos could say anything, both scroll pieces"
     "\nthat you found at some point in the loop appear out of "
     "\nnothing and shine, creating a unique and complete scroll."
     "\nIt's like it was never split in two."
     "\nSuddenly your memories start to flow and you know exactly"
     "\nwhat you have to do. Your freedom is at hand and you cannot"
     "\nhold tears of joy."
     "\n"
     "\nCronos changes his actitude radically. He starts to" 
     "\ninterrogate you and ask you questions on who helped you,"
     "\nhow you did it... His words are filled with anger," 
     "\nfrustration and... fear? You burst out laughing."
     "\n"
     "\nA. You say nothing. Because nothing matters now"
     "\nB. 'Your tiranny ends here!'"
     "\nC. 'Screw you Cronos! I win again!")
    response = ""
    while response not in answer_A or answer_B or answer_C:
        response = input(">>> ")
        if response in answer_A:
            Cronos_2Scroll_Ending()
        elif response in answer_B:
            Cronos_2Scroll_Ending()
        elif response in answer_C:
            Cronos_2Scroll_Ending()
        else:
            print("Enter a valid choice")

def Cronos_2Scroll_Ending():
    print("You read the Scroll of Ages. Some words appear before"
     "\nyour eyes. You know that reading them you will obtain"
     "\nyour freedom...")
    Scroll_Ending()

def Scroll_Ending():
    response = ""
    print("EXIT GAME? Y/N")
    while response not in answer_Y or answer_N:
        response = input("Would you like to close the game? Y/N: ")
        if response in answer_Y:
            #Algo que cerre a ventana, por agora teñoo como "YOU WIN"
            print("YOU WIN")
        elif response in answer_N:
            Cronos_EndingScrewed()
        else:
            print("Enter a valid choice")
    
#Return to intro with Scroll1 = 0; Scroll2 = 1.
def Cronos_EndingScrewed():
    print("'Ok, now I just have to say Y' you though. But you"
     "\nare so nervous that you just say N. Cronos bursts laughing."
     "\nIf you had any doubt, you have made a fool of yourself."
     "\nBut, hey, everyone make mistakes, I guess. "
     "\n"
     "\nThe scroll burns in your hands. When you see the ashes "
     "\nfade away you know that the scroll have just disappeared"
     "\nfrom the time line...")
    scroll_piece1 = False
    scroll_piece2 = False
    intro()
    
    
    
#The real game begins here :v. Just for now. It is a little cancerous to have all the code in a single file. I will change that.

print("         ##########################")
print("         #                        #")
print("         #      THE TIME LOOP     #")
print("         #                        #")
print("         ##########################")
print("\n")
print("\n")
print("\n")

#This is just for starting the game.
response = ""
while response != answer_Y or answer_N:
    response = input("Would you like to start the game? Y/N: ")
    if response in answer_Y:
         intro()
    elif response in answer_N:
         print("Another time maybe")
         quit()
    else:
         print("Enter a valid choice \n")
