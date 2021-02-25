# --------------------------------------------------------
#        Name: <Lessly Ortiz>
# Course Info: CSC111 - Fall 2020
# Description: Submission for Assignment 5
#        Date: <10-10-2020>
# --------------------------------------------------------

from art import *

def encrypt(msg):
    print("encrypting...\n")#Makes the program run slower but if you throw in entire books or something it may take awhile anyways so this is basically a loading thing without the loading bar module
    ecrypt   = msg.split(' ')# can you do a split on a string?
    ecrypt   = [item + "*" for item in ecrypt]# adds the little * to the end      #https://stackoverflow.com/questions/15738267/add-a-character-to-each-item-in-a-list 
    ecrypted =""
    for ecrypter in ecrypt:
        print("encrypting...\n")#Makes the program run slower but if you throw in entire books or something it may take awhile anyways so this is basically a loading thing without the loading bar module
        spli     = ecrypter
        a        = 0 #Start counter at 0
        first    = ecrypter[0] #selects the first letter 
        first    = str(first) #I WILL MAKE A STRIIIINGG OUT OF YOU!
        first    = first.upper()
        if first in vowel: 
            pig_latin   = spli + way # makes the new word
            ecrypted    = ecrypted + pig_latin + " " # adds it to the new sentence
            
        if first in consonant:
            word     = first
            while word in consonant:
                print("encrypting...\n")#Makes the program run slower but if you throw in entire books or something it may take awhile anyways so this is basically a loading thing without the loading bar module
                listy      = [word for word in spli] #seperates the word into a list by char like appartide
                a          = a + 1 #my counter in the loop-de-loop
                word       = listy[a] #selects the next letter 
                word       = str(word) #I WILL MAKE A STRIIIINGG OUT OF YOU!
                word       = word.upper()#IN CASE UPPERCASE
                if word in consonant:#continues my loop-de-loop if its another stinky consonant
                    continue
                elif word in vowel:#what we looking for sweet sweet vowels
                    break #breaks my weird while loop incase of something I dont understand happens   
            length         = len(spli)# gets the legnth of the word
            remove_letters = spli[a:length] #adds the removed chars into a var
            correction     = remove_letters.replace("", "")#a weird correction for some reason needed to be here because idk 
            word           = spli.replace(correction, "")#yep litteraly needed this else it wouldn't print, iont like python 3.9 except for := because its cute 
            pig_latin      = remove_letters + word + ay # takes the last chars in the word adds them to the front then takes the first letters adds them to the back then adds the fonsie
            ecrypted       = ecrypted + pig_latin + " " # adds it to the sentence
        if first not in consonant and first not in vowel: #Stops the only thing that messes it up king of it still goes through with it but ya know
            print("Sorry 0nly condition is you cannot have a symbol or number before a vowel in a word") #just incase some dumbass tries to throw in a weird char

    return ecrypted  #returns it so i can use it
    
    


def decrypt(ecrypted, msg): #The MSG is used as a fail safe in case something breaks the program
    print("decrypting...\n")
    dcrypt   = ecrypted.split(' ')
    dcrypted = ""
    for dcrypter in dcrypt:
        print("decrypting...\n")#Makes the program run slower but if you throw in entire books or something it may take awhile anyways so this is basically a loading thing without the loading bar module
        spli     = dcrypter
        if way not in spli: #Checks to see if its a consonant
            back , sep , front = spli.partition("*")# essenctially DiskPart or Gparted hint use Linux preferably Debian based
            front              = front.replace(ay, "")# gets rid of Phonsie ;(
            dcrypted          = dcrypted + front + back + " "# Creates the origninal word again
        if way in spli: #Checks to see if it's a vowel word
            spli        = spli.replace(way, "")#Removes ~way
            spli        = spli.replace("*", "")
            dcrypted    = dcrypted + spli + ' '# just adds the word to the string
        
    #FAIL SAFE!!!!!!!!!!!!! # you can comment this out if you'd like should still work
    #if dcrypted == msg: 
        #dcrypted = dcrypted
    #if dcrypted != msg:
        #dcrypted = msg
    return dcrypted

def main():
    print     ("\n\n")
    msg      = str(input("Please enter your message: \n"))
    msg      = msg.upper()
    ecrypted = encrypt(msg)
    print     ("Here is your encrypted text:\n\n")
    print     (ecrypted) # prints the encrypted sentence
    dcrypted = decrypt(ecrypted, msg)#MSG is a failsafe in case something breaks the traditional decrypt function
    print     ("Here is your original entry:\n\n")
    print     (dcrypted) # Prints the origninal message
   
    main()


    

ay = "AY" # ayyyyyyyy phonsie
way = "~WAY" # DO YOU KNOW DA WAY?
consonant = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')# Im not an english major
vowel = ('A','E','I','O','U')#again idk im not an english major



banner = text2art("0ink Latin", font="small")
print(banner, """ 
                        _____  
                    ^..^     \9
                    (oo)_____/ 
                       WW  WW """, "My name is Fredrick") #https://www.asciiart.eu/animals/other-land
print("\n\n\n")
print("By: Lessly Ortiz")
print("_" * 60)
print("Welcome to 0ink Latin where we take your message and user the 0ink Latin Cypher \nto make it nearly unreadable and then decode it into its original form")
 


if __name__ == "__main__":#You dont need this, makes it harder to understand what's going on
  main()



