import time


answer = input("Would you like to play (yes/no)?  ").lower ()

if answer == "yes":    
        print("coolio")
        potatoes = int(input("How many potatoes do you have? = "))
        if (potatoes < 10):
                print("very good you may move on")
                print()
                time.sleep(1)
                print("You come across an angry mother what do you do?")
                print()
                time.sleep(1)
                print("A: Make aloo sabji, B: Dab on her, C: Ignore her")
                print()
                time.sleep(1)
                answer2 = input("Which option do you choose? = ").lower ()

                if answer2 == 'a':
                        print(" you walk towards the kitchen and prepare your culinary skills ")
                        print()
                        time.sleep(1)
                        amt1 = int(input("How many potatoes do you want to use = "))
                        if(amt1 < potatoes):
                                print("Not enough potatoes")
                                print()
                                time.sleep(1)
                                print("get good at mafs, Game over")
                        else:
                                print("You put the potatoes in the pan. ")
                        amt2 = potatoes - amt1
                        time.sleep(1)
                        print("You go to turn on the gas.")
                        print()
                        time.sleep(1)
                        print("A: low, B: Meduim, C: high")
                        flame = input("What flame do you use?[a, b, c] = ").lower ()
                        
                        if flame == 'a':
                                        print("You turn the gas to low")
                                        print()
                                        time.sleep(1)
                                        print("You take too long and your mother takes over")
                                        print()
                                        time.sleep(1)
                                        print("Game over")
                        
                        elif flame == 'b':
                                        print("You turn the gas on meduim")
                                        print()
                                        time.sleep(1)
                                        print("Your potatoes are done cooking")
                                        print()
                                        time.sleep(1)
                                        print("You win!!")
                                
                        else:
                                        print("You burnt the potatoes, slow and steady wins the race")
                                        print()
                                        time.sleep(1)
                                        print("Game over")
                        
                if answer2 == 'b':
                        print("you proceed to dab on her")
                        print()
                        time.sleep(1)
                        print("She pulls out an uno reverse card what do you do?")
                        print()
                        time.sleep(1)
                
                        print("A: Ratio her, B: Challenge her to a fight, C: Use a counter ratio card")
                        print()
                        time.sleep(1)
                        mom = input("Which option do you choose? = ")
                        
                        if mom == 'a':
                                print("You ratio your mother")
                                print()
                                time.sleep(2)
                                print("She doesnt understand it and takes it for 'an urban slur'")
                                print()
                                time.sleep(1)
                                print("She gives you 1 option to explain yourself.")
                                time.sleep(1)
                                print()
                                print("A: It was a joke, B: You arent understanding it properly, C: *bali noises*")
                                mom_a = input("Which option do you choose? = ")
                                
                                if mom_a == 'a':
                                        print("unfunny joke")
                                        print()
                                        time.sleep(1)
                                        print("you lose due to emotional damage")
                                        print()
                                        time.sleep(1)
                                        print("GAME OVER")
                                
                                if mom_a == 'b': 
                                        print("You try and explain yourself, but it comes out making your mother think you are saying she is stupid")
                                        print()
                                        time.sleep(1)
                                        print("You are instantly slapped and break down into tears")
                                        print()
                                        time.sleep(1)
                                        print("Game over")
                                        
                                if mom_a == 'c':
                                        print("You start making random bali noises")
                                        print()
                                        time.sleep(1)
                                        print("Your mother assumes its a gang song")
                                        print()
                                        time.sleep(1)
                                        print("You are instantly thrown into your room")
                                        print()
                                        time.sleep(1)
                                        print("Game over, blame bali for this one..")        
                        
                        elif mom == 'b':
                                print("where do you go for a critical hit?")
                                print()
                                time.sleep(1)
                                print("A: Toes, B: Face, C: Fingers")
                                print()
                                time.sleep(1)
                                mom_b = input("Where do you hit? = ")
                       
                                if mom_b == 'a':
                                        print("You forgot she was a toe ninja and instantly critical hit you back")      
                                print()
                                time.sleep(1)
                                print("You take 40 damage and are at 60 hp.")
                                time.sleep(1)
                                print()
                                print("A: Try again for a crit. B: Attack face, C: Run away")
                                print()
                                time.sleep(1)
                                mom_b1 =input("What do you choose? = ").lower ()
                                
                                if mom_b1 == 'a':
                                        print("You go for a risky crit on the pinky toe")
                                        print()
                                        time.sleep(2)
                                        print("You crit her! -50 damage")
                                        print()
                                        time.sleep(2)
                                        print("Mother: Its my house, hitting me is not allowed, you are banished")
                                        print()
                                        time.sleep(1)
                                        print("You get thrown out of the house and start a new life working for raju tea stall and live a very long life")
                                        print()
                                        print("GAME OVER!")
                                        
                                if mom_b1 == 'b':
                                        print("you attack the face")
                                        print()
                                        time.sleep(2)
                                        print("Before you can attack, you hear the aromatic smell of aloo sabji")
                                        print()
                                        time.sleep(2)
                                        print("you instantly lower your hand and eat all the aloo sabji")
                                        print()
                                        time.sleep(2)
                                        print("You ate the aloo sabji!!")
                                        print()
                                        time.sleep(1)
                                        print(" YOU WIN !!! ")
                                        print()
                                        time.sleep(2)
                                        print("(although the rest of the familly hated you because you ate all the sabji")
                
                                if mom_b1 == 'c':
                                        print("You start running away in fear")
                                        print()
                                        time.sleep(1)
                                        print("You come to a decision left or right?")
                                        print()
                                        time.sleep(1)
                                        lr = input("Where do you go [left/right] = ").lower ()

                                        if lr == 'left':
                                                print("You turn left in the hope of solitude")
                                                print()
                                                time.sleep(1)
                                                print("But you are legally blind and run into a wall")
                                                print()
                                                time.sleep(1)
                                                print("You get knocked out cold and your mother wins")
                                                print()
                                                time.sleep(1)
                                                print(" Game over, you lost to a wall..")
                                        
                                        if lr == 'left':
                                                print("You turn left in the hope of shelter")
                                                print()
                                                time.sleep(1)
                                                print("but you forget you are dyslexic and end up going left")  
                                                time.sleep(1)
                                                print("But you are legally blind and run into a wall")
                                                print()
                                                time.sleep(1)
                                                print("You get knocked out cold and your mother wins")
                                                print(" Game over, you lost to a wall..")             
                        
                        if mom == 'c':
                                print("You use your counter ratio card")
                                print()
                                time.sleep(1)
                                print("You realize you used a couter ratio card without getting ratio-ed")
                                print()
                                time.sleep(1)
                                print("You start regretting you life choices and start thinking you are stupid")
                                print()
                                time.sleep(1)
                                print("Your mother capitlizing on the situation brings up your grades")
                                print()
                                time.sleep(1)
                                print("A: Grades dont matter, B: You never got good grades, C: Start doing tik tok dances")
                                momc_1 = input("What do you choose? = ").lower ()
                                
                              
                                if momc_1 == 'a':
                                        print("Your mother is shocked hearing this and makes you follow her to the basment")
                                        print()
                                        time.sleep(1)
                                        print("You get in your car and visit raju tea stall")
                                        print()
                                        time.sleep(1)
                                        print("She points at them and says 'this is what happens when you dont study'(LEGIT EVERY PARENT DOES THAT) ")
                                        print()
                                        time.sleep(1)
                                        print("You feel embarssed for no reason and accept defeat")
                                        print()
                                        time.sleep(1)
                                        print("Game over")
                                
                                if momc_1 == 'b': 
                                        print("Her face starts to turn angrier by the second")
                                        print()
                                        time.sleep(1)
                                        print("She slaps you so hard that your teeth fall out")
                                        print()
                                        time.sleep(1)
                                        print("You both run to the doctor, and to get your jaw re-alligned it cost 40k")
                                        print()
                                        time.sleep(1)
                                        print("She feels extremly guilty and makes you a bowl of aloo sabji")
                                        print()
                                        time.sleep(1)
                                        print("Not only did she lose money, she had to accept defeat")
                                        print()
                                        time.sleep(1)
                                        print("OMEGA WIN!")
                
                                if momc_1 == 'c':
                                        print("For the first few seconds she is confused by your movments")
                                        print()
                                        time.sleep(1)
                                        print("after a while she deems you mentally crazy and takes away all your gadgets")
                                        print()
                                        time.sleep(1)
                                        print("Game over, you lost due to tik tok dances")
                                                        
                if answer2 == 'c':
                        print("She got mad at you and grounded you, game over")
                                                       
        
        elif (potatoes > 10):
                        print("Way too many potatoes, what is this the irish famine?")
         
        else:
                print("Invalid wtf u doing noob")
    
elif answer == 'no':
                print("damn alright")

