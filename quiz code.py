print("Good luck!")
answer_ex = input("Good luck! To start type 'start'")
points = 0
if answer_ex == 'start':
  answer_ex = input("Question 1: Which of these SCPS are Keter class?  1. SCP682  2. SCP096") 
  if answer_ex == '1' :
    points = points + 1
  elif answer_ex == '2':
    points = 0
  print(str(points) + "/1")
  answer_ex = input("Type c to continue! Same for the following questions") 
  if answer_ex == 'c' :
    answer_ex = input("Question 2: What SCP commonly is associated with the word 'pestilience'? 1. SCP 049 2. SCP 5000")
    if answer_ex == '1':
      points = points + 1
    elif answer_ex == '2':
      points = points
    print(str(points) + "/2")
    answer_ex = input("Type C to continue!")
    if answer_ex == 'c':
      answer_ex = input("Question 3: Which of these safe-class SCPs is more deadly? 1. SCP 999 2. SCP 131")
      if answer_ex == '1':
        points = points + 1
      elif answer_ex == '2':
        points = points
      print(str(points) + "/3")
      answer_ex = input("Type C to continue!")
      if answer_ex == 'c':
        answer_ex = input("Question 4: Which SCP is 'reported to attack by snapping the neck at the base of the skull'? 1. SCP 173 2. SCP 049")
        if answer_ex == '1':
          points = points + 1
        elif answer_ex == '2':
          points = points
        print(str(points) + "/4")
        answer_ex = input("Press C to continue!")
        if answer_ex == 'c':
          answer_ex = input("Question 4: Which SCP is referred to as 'The Flesh That Hates'? 1. SCP 666 2. SCP 610")
          if answer_ex == '1':
            points = points
          elif answer_ex == '2':
            points = points + 1
          print(str(points) + "/5")
          # End of quiz (Aidan if u have additional questions add it above this line.
          answer_ex = input("Press C to continue!")
          if answer_ex == 'c':
            print("Thank you for playing! You got " + str(points) + " correct! Well done!")
