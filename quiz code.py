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
          answer_ex = input("Question 5: Which SCP is referred to as 'The Flesh That Hates'? 1. SCP 666 2. SCP 610")
          if answer_ex == '1':
            points = points
          elif answer_ex == '2':
            points = points + 1
          print(str(points) + "/5")
          answer_ex = input("Press C to continue!")
          if answer_ex == 'c':
            answer_ex = input("Question 6: Which class is SCP 096 in? 1. Keter 2. Euclid")
            if answer_ex == '1':
              points = points
            elif answer_ex == '2':
              points = points + 1
            print(str(points) + "/6")
            answer_ex = input("Press C to continue!")
            if answer_ex == 'c':
              answer_ex = input (" Question 7: Where was SCP 049 discovered? 1. Montauban, South of France 2. neighbourhood on outskirts of Paris, France")
              if answer_ex == '1':
                points = points + 1
              elif answer_ex == '2':
                points = points 
              print(str(points) + "/7")
              answer_ex = input("Press C to continue!")
              if answer_ex == 'c':
                answer_ex = input (" Question 8: What is SCP 265? [ good luck man ] 1. Rolls Royce Phantom III Sedanca de Ville 2. Series 1 GAZ M21 Volga")
                if answer_ex == '1':
                  points = points
                elif answer_ex == '2': 
                  points = points + 1
                print(str(points) + "/8")
                answer_ex = input("Press C to continue!")
                if answer_ex == 'c':
                  answer_ex = input(" Question 9: What is SCP 294? 1. An antique doll 2. A vending machine")
                  if answer_ex == '1':
                    points = points + 1
                  elif answer_ex == '2':
                    points = points
                  print(str(points) + "/9")
                  answer_ex = input("Press C to continue!")
                  if answer_ex == 'c':
                    answer_ex = input ("What is SCP 173 commonly likened to in appearance? 1.A statue 2. A peanut")
                    if answer_ex == '1':
                      points = points
                    elif answer_ex == '2':
                      points = points + 1
                    print(str(points) + "/10")
                    answer_ex = input("Press C to continue!")
                    if answer_ex == 'c':
                      answer_ex = input ("Which of the following is a safe class SCP? 1. SCP 999 2. SCP 173")
                      if answer_ex == '1':
                        points = points + 1
                      elif answer_ex == '2':
                        points = points
                      print(str(points) + "/11")
                      answer_ex = input("Press C to continue!")
                      if answer_ex == 'c':
                        answer_ex = input ("What does SCP stand for? 1. Strange Creature Protection 2. Secure Contain Protect")
                        if answer_ex == '1':
                          points = points
                        elif answer_ex == '2':
                          points = points + 1
                        print(str(points) + "/12")
                        answer_ex = input("Press C to continue!")
                        if answer_ex == 'c':
                          answer_ex = input ("Why is SCP 682 dangerous? 1.It has an array of sharp claws and teeth, and a tail which can snap a humans legs in class. 2. It simply cannot die and hates all life")
                          if answer_ex == '1':
                            points = points
                          elif answer_ex == '2':
                            points = points + 1
                          print(str(points) + "/13")
                          answer_ex = input("Press C to continue!")  
                          if answer_ex == 'c':
                            answer_ex = input ("What is SCP 001’s name 1. The Scarlet King 2. Alpha Male")
                            if answer_ex == '1':
                              points = points + 1
                            elif answer_ex == '2':
                              points = points
                            print(str(points) + "/14")
                            answer_ex = input("Press C to continue!")   
                            if answer_ex == 'c':
                              answer_ex = input ("What has been rumoured to have temporarily killed SCP 682? 1. SCP 173 2. SCP 4218")
                              if answer_ex == '1':
                                points = points + 1
                              elif answer_ex == '2':
                                points = points
                              print(str(points) + "/15")                
                           # End of quiz (Aidan if u have additional questions add it above this line.
                              answer_ex = input("Press C to continue!")
                              if answer_ex == 'c':
                                print("Thank you for playing! You got " + str(points) + " correct! Well done!")
