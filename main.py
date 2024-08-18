import art
import random
import game_data

print(art.logo)

used_people = []
user_seikaiisuu = 0
gameover = False
def question():
    people = random.choice(game_data.data)
    compare_follower = people['follower_count']
    compare_name = people['name']
    compare_description = people['description']
    compare_country = people['country']
    game_data.data.remove(people)
    used_people.append(people)
    bunsyou = f"{compare_follower},{compare_name}, {compare_description}, form {compare_country}"
    return compare_follower, bunsyou

def owari():
    print("\n" * 20)
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {user_seikaiisuu}.")

followers1, description1 = question()
print(f"Compare A: {description1}")
print(art.vs)
followers2, description2 = question()
print(f"Compare B: {description2}")
userchoice = input("Who has more followers? Type 'A' or 'B': ")

while not gameover:
    if game_data.data == []:
        gameover = True
        print(art.perfect)

    elif userchoice == "A":
        if followers1 > followers2:
            print("\n"*20)
            print(art.logo)
            user_seikaiisuu += 1
            print(f"You're right! Current score {user_seikaiisuu}")
            followers1, description1 = followers2, description2
            followers2, description2 = question()
            print(f"Compare A: {description1}")
            print(art.vs)
            print(f"Compare B: {description2}")
            userchoice = input("Who has more followers? Type 'A' or 'B': ")
        else:
            gameover = True
            owari()

    else:
        if followers1 < followers2:
            print("\n"*20)
            print(art.logo)
            user_seikaiisuu += 1
            print(f"You're right! Current score {user_seikaiisuu}")
            followers1, description1 = followers2, description2
            followers2, description2 = question()
            print(f"Compare A: {description1}")
            print(art.vs)
            print(f"Compare B: {description2}")
            userchoice = input("Who has more followers? Type 'A' or 'B': ")
        else:
            gameover = True
            owari()


