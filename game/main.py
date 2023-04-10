import random
#Variables
options = ("piedra", "papel", "tijera")
rounds = 1
wins_user1 = 0
wins_user2 = 0

while True:
        print ('-'*10)
        print ('ROUND', rounds)
        print ('-'*10)
        


        user_1 = input("usuario 1 elige: piedra, papel, tijera? => ".title())
        user_1 = user_1.lower()
        user_2 = random.choice(options)
        user_2 = user_2.lower()
        print (f"user_1=> {user_1}")
        print (f"user_2=> {user_2}")
        rounds += 1

        if not user_1 in options: 
                print ("no es una opcion valida")
                continue



        if user_1 == user_2:
                        user_1 = user_1.lower()
                        user_2 = user_2.lower()
                        print(f"{user_2} y {user_1} EMPATE")
        elif user_1 == "papel":
                if user_2 == 'tijera':
                                user_1 = user_1.lower()
                                user_2 = user_2.lower()
                                print ("{} le gana a {}, PERDISTE user_1, GANASTE user_2".format(user_2, user_1))
                                wins_user2 += 1
                else:
                        print ("{} le gana a {}, PERDISTE user_2, GANASTE user_1".format(user_1, user_2))
                        wins_user1 += 1
        elif user_1 == "piedra":
                if user_2 == 'tijera':
                        user_1 = user_1.lower()
                        print (f"{user_1} le gana a {user_2}, PERDISTE user_2, GANASTE user_1")
                        wins_user1 += 1
                else:
                        print (f"{user_2} le gana a {user_1}, PERDISTE user_1, GANASTE user_2")
                        wins_user2 += 1
        else:
                if user_2 == 'papel':
                        print (f"{user_1} le gana a {user_2}, PERDISTE user_2, GANASTE user_1")
                        wins_user1 += 1
                else:
                        print (f"{user_2} le gana a {user_1}, PERDISTE user_1, GANASTE user_2")
                        wins_user2 += 1
        if wins_user1 == 5:
                print ( 'user_1 Eres el GANADOR')
                break
        if wins_user2 == 5:
                print('user_2 Eres el GANADOR')
                break
        