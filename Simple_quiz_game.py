

from Questions_and_Answers import questions,answers

score =0 
attempt=2


while attempt>0 :
    for question in questions:
        print(question,". ", questions[question]["question"],sep="" )
        inp=input("\nEnter the choice :").lower()
        if (answers[question])==inp:
            score+=1
            print("\nCorrect answer!!!\n")
        else:
            attempt-=1
            print("\nwrong answer :(\n")
    break
print("your score :",score,"/",len(questions))