#SWEN 503
#Mauricio Hernandez
#300412504
#Python program with very basic functionalities to manage a contact list

import json
from Tkinter import *
from distutils import command

#The new contact is a dictionary that is added to the list of contacts
#It opens the contacts.json file and then overwrites with the new information
def addContact():
    try:
        name_i=raw_input("Add name: ")
        phone_i=raw_input("Add phone: ")
        mail_i=raw_input("Add mail: ")
        
        contact_n={"name":name_i,"phone": phone_i, "mail":mail_i}
        
        with open("res/contactslist.json","r+") as f:
            data= json.load(f)
            data["contacts"].insert(len(data["contacts"]),contact_n)
            f.seek(0)
            f.truncate()
            json.dump(data,f,indent=2)
            print("The contact was added successfully")
    except IOError:
        print("Something went wrong with res/contactslist.json")

#It prints every contact-dictionary information from the list                
def displayContacts():
    try:
        with open("res/contactslist.json","r") as f:
            data= json.load(f)
            for contact in data["contacts"]:
                print("Name: " + contact["name"])
                print("Phone: " + contact["phone"])
                print("Email: " + contact["mail"])
                print("...........................")
    except IOError:
        print("Something went wrong with res/contactslist.json")

#Iterates contact list(dict entries) to find a matching name key,
#if found it displays the contact
def searchContact():
    search_c=raw_input("Write the name of contact to search: ")
    try: 
        with open("res/contactslist.json","r") as f:
            data= json.load(f)
            counter=0
            for contact in data["contacts"]:
                if contact["name"]!=search_c:
                    counter+=1
                else:
                    break
            contact= data ["contacts"][counter]
            print("Name: " + contact["name"])
            print("Phone: " + contact["phone"])
            print("Email: " + contact["mail"])
            print("...........................")
    except (IOError,IndexError):
        print("Check the spelling of the contact name or res/contactslist.json")
    

#Iterates contact list(dict entries) to find a matching name key,
#if found it removes the contact      
def removeContact():
    remove_c=raw_input("Write the name of contact to remove: ")
    try:
        with open("res/contactslist.json","r+") as f:
            data= json.load(f)
            counter=0
            for contact in data["contacts"]:
                if contact["name"]!=remove_c:
                    counter+=1
                else:
                    break
            del data["contacts"][counter]
            f.seek(0)
            f.truncate()
            json.dump(data,f,indent=2)    
            print("The contact was removed successfully")
            
    except (IOError,IndexError):
        print("Check the spelling of the contact name or res/contactslist.json ")

#Iterates contact list(dict entries) to find a matching name key,
#if found it updates the phone and mail information
def updateContact():
    search_c=raw_input("Write the name of contact to update: ")
    try:
 
        with open("res/contactslist.json","r+") as f:
            data= json.load(f)
            counter=0
            for contact in data["contacts"]:
                if contact["name"]!=search_c:
                    counter+=1
                else:
                    break
            contact= data ["contacts"][counter]
            phone_i=raw_input("Add new phone: ")
            mail_i=raw_input("Add new mail: ")
            
            contact["phone"]= phone_i
            contact["mail"]= mail_i    
            
            f.seek(0)
            f.truncate()
            json.dump(data,f,indent=2)    
            print("The contact was updated successfully")
            
    except (IOError,IndexError):
        print("Check the spelling of the contact name or res/contactslist.json ")

#GUI
root=Tk()
theLabel_1=Label(root,text="WELCOME TO CONTACT LIST")
theLabel_2=Label(root,text= '''
                            Make sure you have the file res/contactslist.json
                            Use the GUI just to select an option. 
                            Input/Output happens in the console''')

theLabel_1.pack()
theLabel_2.pack()

button_add=Button (root,text="Add", command=addContact)
button_add.pack()
button_display=Button (root,text="Display", command=displayContacts)
button_display.pack()
button_search=Button (root,text="Search", command=searchContact)
button_search.pack()
button_remove=Button (root,text="Remove", command=removeContact)
button_remove.pack()
button_update=Button (root,text="Update", command=updateContact)
button_update.pack()
root.mainloop()





        


