print("Good luck!")
answer_ex = input("Good luck! To start type 'start'")
points = 0
if answer_ex == 'start':
  answer_ex = input("Question 1: Which of these SCPS are Keter class?  1. SCP682  2. SCP096") 
  if answer_ex == '1' :
    points += 1
  elif answer_ex == '2':
    points = 0
  answer_ex = input("Type c to continue! Same for the following questions") 
  if answer_ex == 'c' :
    answer_ex = input("Question 2: What SCP commonly is associated with the word 'pestilience'? 1. SCP 049 2. SCP 5000")
    if answer_ex == 1:
      points += 2
    elif answer_ex == 2:
      points += 0
    print(str(points))
