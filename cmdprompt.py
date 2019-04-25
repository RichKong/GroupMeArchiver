import pyAesCrypt
import zipfile
import os


action = ""
i = 0
while action not in {'1','2','3'}:
    if i == 1:
        print("Sorry, %s is not a valid selection" % action)
    i = 1
    action = input('''Welcome! What would you like to do today? 
        1) Encrypt + Compress file
        3) Archive groupme chat''')

action = int(action)

mappings = {'1': encrypt,
            '2': archive
            }

def archive(): 
    oauth = input('''To continue, please enter your GroupMe authentication token.
    If you need help finding it, please go to https://dev.groupme.com/ and log-in.''')


    test = Archiver(oauth)
    arr = test.group_list()

    print("/nPlease select the chat you'd like to archive/n")

    j = 0
    for i in arr: 
        j += 1
        print("/n%d) %s" % (j, i))
    
    
    chat_selection = input("")


    print("/nYou have selected " + chat_selection)
    chat_selection = int(chat_selection)






    file_name = input("Name your archive file: ")

def encrypt(): 

    file_name = input("What is your archive file: (leave off .txt)")

    archive_name = file_name + ".zip"
    file_name = file_name + ".txt"

    with zipfile.ZipFile(archive_name, 'w') as file:
        print("{} is created.".format(archive_name))
        file.write(file_name)

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    password = "foopassword"
    # encrypt
    pyAesCrypt.encryptFile(file_name, file_name + ".aes", password, bufferSize)

   
 
    


    
    
