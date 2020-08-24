import os
import os.path # Necessary for me to work with file structures
cls = lambda: os.system("cls") #This allows me to clear the console
#This is a modified program that I made for CS Circles, this program will output every possible version of the decoded message and
# show you the most likely message along with the shift value and give you the option to save the data to a txt file.

def ProgramCloser():
    cls()
    exit(0)

def inputChecker(possibleText):
    tester = possibleText.replace(" ","")#Removes all spaces
    tester=tester.isalpha()#Tests to see if the string contains all letters
    return tester

# This is a method that when called upon will clear the console then close the program
# Not 100% necessary but it saves my typing the 2 liners a couple times, so it is actually a little more efficient

letterGoodness= [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
#This was given to me from CS Circles, it is the most common occurring letters in sentences
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True: #Keeps the program running unless the user decides to exit program 
    while True:#Keeps the users in a lop until they enter a valid string
        cls()
        print("Welcome to Jacob’s Caesar cypher cracking program, type the following then hit enter to perform the action\n")
        print("1)Manually input the encrypted text (or copy and paste)\n2)Exit the program")
        print("\nPlease Note: This is a Caesar Cipher decryption program, due to the nature of the cypher no non letter characters can be used except for spaces. So, no numbers, symbols, etc.")
        print("")
    
        userC=input()
        if userC=="2": ProgramCloser() 
        #If the user types 3 then the program will close 
        possibleText=""#This text will have to be checked to make sure that it does not contain any non letter characters
        attemptStorage=[] # This is a list that will keep track of every attempt of decoding the message
        if userC=="1":
            cls()
            print("Type in you encrypted text then hit enter\nPlease Note: This is a Caesar Cipher decryption program, due to the nature of the cypher no non letter characters can be used except for spaces. So, no numbers, symbols, etc.")
            print("")
            possibleText=input()
            if inputChecker(possibleText) == True: break # If the text that the user inputted is valid then the user can move on
            else:
                cls()
                print(possibleText,"is not valid, press enter to be taken back to the start")
                input()
                 
 
    highestLetterGoodness=0
    tempString =""
    decryptedMessage=""# The actual or final decrypted message
    testMessage=possibleText.upper() # Now that the text is a possible word the program will be able to use it.
    # I originally coded the program for all caps so the string will be converted to caps. Also, this removes any letter case errors.
    bestS=0
    S=0# Shift Value
    for t in range(26):
        letterGoodnessCounter=0 # current value of the word
        decodedMessage="" #stores the potentially correct message
        for i in range(len(testMessage)):
         if testMessage[i] in letters:
           # print(letters.find(testMessage[i]))
              x=letters.find(testMessage[i])
              #print(26-(x-S)) 
               #print("x is:",x,"S is",S,"and x-S is:",x-S)
              if x-S<0:
                  x=x+26
             # print(lettergoodness[x-S])
              letterGoodnessCounter= letterGoodnessCounter+letterGoodness[x-S]
              decodedMessage= decodedMessage+ letters[x-S]
         else: decodedMessage= decodedMessage+" "
        tempString="Shift value: "+str(S)+" Potentially decoded message:\n"+decodedMessage+"\n" # Converts the data into a string, allowing for it to be stores in a list
        attemptStorage.append(tempString)
        if letterGoodnessCounter>highestLetterGoodness:
             bestS=S
             highestLetterGoodness=letterGoodnessCounter
             decryptedMessage = decodedMessage
             #print(S)
             #print(letterGoodnessCounter,decryptedMessage)
        
        S=S+1
    cls()
    print("Your encrypted message was:", possibleText.lower())                           
    print("The likely decrypted message is:",decryptedMessage.lower()," With a shift value of:",bestS,"\n")
    print("Press enter to be taken back to the start, press 1 to archive you data and press 2 to exit\n")
    #print(decryptedMessage) # Final message
    c=input()
    if c=="1":
        while True:# Keeps the user in a loop until they enter a valid file name or decide to close the program
            cls()
            print("Type in your custom file name below then press enter. Only letters and spaces allowed, or type e and press enter to exit")
            print("\nNote: If a file already has that name then it will be replaced. Also don’t put the file extension, it is automatically saved as a .txt.")
            print("Also, you will be able to see more data if you choose to export it")
            name=input()
            if name=="e": ProgramCloser()# Closes the program 
            if inputChecker(name) == True: break # If the text that the user inputted is valid then the user can move on
        name=name+".txt"# This makes the file a text file     
        file=open(name,"w+")# This opens the file and allows me to write to it, if the file does not exits then it will cerate one
        temp="Your encrypted message was:"+ possibleText.lower()
        file.write(temp) # Note: All previous in the file is overwritten
        temp="\nThe likely decrypted message is:"+decryptedMessage.lower()+" With a shift value of:"+str(bestS)+"\n"
        file.write(temp) 
        file.writelines(attemptStorage) # This command writes every string from the list into the text file
        file.close()
        cls()
        print("File was successfully created!")
        print("The file name is:",file.name.replace(".txt","")) #Prints out the file name and the removes the extension so the user can see the file name
        print("The file name with its extension is:",file.name) # Shows the file name with its extension
        print("The file is located in:", os.path.realpath(file.name).replace(file.name,"")) # Shows the files path by finding the files exact location then removing the file name
        print("The exact file path is:",os.path.realpath(file.name)) # Shows the files exact location ( The file path )
        print("Press enter to be taken back to the start or type e then hit enter to exit")
        i=input()
        if i=="e": ProgramCloser()# Closes the program 
    if c=="2": ProgramCloser()# Closes the program 
   


#print(highestLetterGoodness) # based off the most likely number (the number printed below)
#print(bestS)# The most likely S value

#For Testing:
#testMessage="LQKP OG CV GKIJV DA VJG BQQ"
#testMessage="JAZZ"#0.0846
#testMessage="TKJJ"#OFEE with 0.3514
#testMessage="HUD"
#testMessage="BZS"                                
#testMessage="ECV"# Should be cat when S=28


