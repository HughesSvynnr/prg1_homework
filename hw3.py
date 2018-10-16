#prg1_Hw3
while(True):
    print("Welcome to SJNMA!")
    print("This is your Planner that will help you keep track of your homework")
    print("please enter in the numbers 1, 2, or 3.")
    number = 1 or 2 or 3
    number = int(input("number>"))
    
    if(number==1):
        hwtd=str(input("What is homework? "))
    
        hdd=str(input("When's it due? "))
    
        homework = (hwtd + hdd)

    if(number==2):
        qt=str(input("Describe the quiz or test " ))
        
        tqd=str(input("When will the test or quiz happen? "))
    
        tests = (qt + tqd)

        homework_and_tests=[
            homework,
            tests,
    ]
    
    if(number==3):
        print("Here are all the assignments, quizzes and tests you have written down> ")
        print(homework_and_tests)