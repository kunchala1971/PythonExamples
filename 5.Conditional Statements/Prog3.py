playerName=input("Enter Player Name: ")
score=int(input("Enter Score: "))
result=""
if score==0:
    result="Dock Out"
elif score>0 and score<50:
    result="Below Half Century"
elif score==50:
    result="Half Century"
elif score>50 and score<100:
    result="Above Half Century"
elif score==100:
    result="Century"
elif score>100 and score<150:
    result="Above Century"
elif score==150:
    result="One and Half Century"
elif score>150 and score<200:
    result="Above One and Half Century"
elif score==200:
    result="Double Century"
elif score>200:
    result="Above Double Century"

print("Player Name is {}, he scores {} and got the rank is {}".format(playerName,score ,result))