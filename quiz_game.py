print("Welcome ! You will pass a little quiz about Vietnam !")

def ready():
    ready_answer = input("Do you want to start the quiz ? Yes[Y] or [No]N : ")
    
    if ready_answer == "Y" or ready_answer == "y":
        print("Let's start !")
        return true
    elif ready_answer == "N" or ready_answer == "n":
        print("See you next time")
        quit()
    else:
        print("Please, write Yes[Y] or [No]N : ")
        ready()
            
ready()

#Dictionaries with question and answer, idk if it is the best method.
# Have to think about the best method to bank the question, 
def question_function():
    questions_list = {
                    one : "What's the capital ?",
                    one_answer : "Hanoi"
                    two :                 
                    }