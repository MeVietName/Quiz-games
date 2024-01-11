print("Welcome ! You will pass a little quiz about Vietnam !")

def ready():
    ready_answer = input("Do you want to start the quiz ? Y or N : ")
    
    if ready_answer == "Y":
        print("Let's start !")
        return true
    elif ready_answer == "N":
        quit()
    else:
        ready()
            
ready()