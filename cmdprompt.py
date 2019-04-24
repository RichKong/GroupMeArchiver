action = ""
i = 0
while action not in {'1','2','3'}:
    if i == 1:
        print("Sorry, %s is not a valid selection", action)
    i = 1
    action = input("Welcome! What would you like to do today?\n
    1) Encrypt file\n
    2) Compress file\n
    3) Archive groupme chat\n")

action = int(action)

mappings = {'1': encrypt,
            '2': compress,
            '3' archive
            }

def archive(): 
    oauth = input("/nTo continue, please enter your GroupMe authentication token. \n
    If you need help finding it, please go to https://dev.groupme.com/ and log-in. \n")


    print("/nPlease select the chat you'd like to archive/n")


    
    chat_selection = input("")


    print("/nYou have selected " + chat_selection)
    chat_selection = int(chat_selection)

    file_name = input("Name your archive file: ")

    


    
    
