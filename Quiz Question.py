quiz = {
    'question 1':{
        'question':'Whats your name?',
        'answer':'Jhon',
    },
    'question 2':{
        'question':'Whats your fathers name?',
        'answer':'Smith',
    },
    'qestion 3':{
        'question':'Which game is your favourite?',
        'answer':'Apex Legend',
    },
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input('Answer :')

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print("Your score is "+str(score))

    else:
        print("Incorrect")
        print("Your score is "+str(score))
        print("The correct answer is "+value['answer'])

print("")
print("-----------------------")
print("RESULT")     
print("-----------------------")
print("")

print("The total score is "+str(score)+" Out of 3 questions")
print("The total percentage is "+str(int(score/3*100))+"%")

    























