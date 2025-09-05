import threading
import time,os
import pyttsx3
from playsound import playsound
import random

#Vars ---------------------------------------------------

#interaction var
interaction_counter = 0

#library var
books = ["God Don't Like Ugly",
                "Harry Potter and the Chamber of Secrets",
                "1984",
                "Fahrenheit 451",
                "Dune"]

#opening game text var
opening_game_info_1 = ("""You thought it was just another school day as you opened your computer, but the screen flickered. You noticed your terminal is open, reading:

#WARNING: Sean, Brittany, and RJ are not who they seem!
#They are planning to sacrifice Base Camp students to the software god, Kagan.
#There's only one way out: with a code.
#It's up to you to find the code and uncover the secrets of Base Camp.
#Good luck.
    """)

#lobby vars
list_lobby_sean = ["Sean sits in his usual spot, but he looks unnaturally hunched over his computer.", 
"Looking at the dreaded sandwich on your plate, you swear you see something wiggling in it... suddenly you're not hungry anymore.",
"You hear pots and pans in the kitchen, but when you go to look, there's nobody there. You notice roaches in the cereal.",]

list_lobby_sean2 = ["You accidentally step in a strange liquid and look up to see it coming from the ceiling. It smells funny...",
"There's a loud crunching sound coming from Ms. Brittany's office, but you choose to ignore it.",
"You see the janitor walk by the bathrooms cleaning. He looks sick and pale, unnaturally hunched over."]


#class room var
list_find_stuff_rj = ["The light flickers for a moment before going back to normal.",
"Your computer glitches and you see a flash of RJ's face... his teeth look abnormally sharp.",
"The internet goes out and you can't seem to get it working for a few minutes."]

list_find_stuff_rj2 = ["You look up and feel an unknown liquid dripping on your face, gross.",
"You see Sean walking by, a strange red glint in his eyes.", 
"The air around you suddenly gets cold and you swear you can see your breath."]

#slack vars
random_stuff_for_slack = ["You have a new message from your friend Kaden: 'Sean is trying to eat me! HELP!!'",]

#library vars
fahrenheit = """In Montag's world, people are discouraged from reading and engaging in meaningful conversations.
Instead, they are absorbed in mindless entertainment, primarily through large television screens. 
Montag's life takes a turn when he witnesses an elderly woman choosing to die with her books rather than live in a world without them. 
This event sparks a crisis of conscience in Montag, leading him to question the society he lives in and his role within it.

As Montag grapples with his growing dissatisfaction, he begins to secretly collect and read books, seeking knowledge and understanding.
His internal conflict escalates as he confronts his wife, Mildred, who is more interested in her television shows than in their marriage. 
Montag's rebellion against societal norms puts him at odds with his fire chief, Captain Beatty, who represents the oppressive forces of censorship and conformity."""

nineteen = """Set in a future where the world is divided into three superstates, Oceania, Eurasia, and Eastasia, the novel follows Winston Smith, a member of the Outer Party living in Airstrip One (formerly known as Great Britain). 
The Party, led by the figurehead Big Brother, maintains control through constant surveillance, propaganda, and the manipulation of truth. 
The society is characterized by the use of Newspeak, a language designed to limit free thought, and the enforcement of loyalty to the Party through the Thought Police."""

dune = """Dune, the first book in Frank Herbert's series, follows Paul Atreides, the heir of Duke Leto Atreides, as they move to the desert planet Arrakis. 
Arrakis is the only source of the valuable spice melange, which is crucial for space travel and grants psychic abilities. 
As Duke Leto takes on the governorship of Arrakis, he faces a conspiracy led by Emperor Corrino and Baron Vladimir Harkonnen to destroy his family. 
Throughout the story, Paul grapples with his destiny and the prophetic dreams that hint at his significant role in the future of the universe."""

god_dont = """"God Don't Like Ugly" by Mary Monroe is a poignant coming-of-age novel set in civil rights-era Ohio. 
The story follows Annette Goode, a shy and insecure thirteen-year-old girl burdened by a dark secret. 
She finds solace in her books and food until she is chosen as a friend by Rhoda Nelson, a radiant and confident girl. 
Annette is drawn into Rhoda's vibrant and eccentric family, which includes a handsome father, a fragile "Muh'Dear," a brooding brother, and colorful white relatives. 
The friendship takes a dramatic turn when Rhoda reveals a shocking truth about her past, forcing Annette to confront the complexities of loyalty and resilience. 
The novel is rich with humor and depth, exploring the transformative power of friendship in the face of adversity."""

chamber_secrets = """Harry Potter and the Chamber of Secrets is the second novel in the Harry Potter series, written by J.K. Rowling. 
It was first published in the UK on July 2, 1998, and in the US on June 2, 1999. 
The story follows Harry's second year at Hogwarts School of Witchcraft and Wizardry, where he faces new challenges, including a mysterious chamber and a spirit named Moaning Myrtle."""

#random var
the_random_lobby = random.choice(list_lobby_sean)
the_random_lobby_1 = random.choice(list_lobby_sean2)
the_random_lobby_2 = random.choice(list_lobby_sean)
random_lobby_game = random.randint(1,3)
ping_pong_opponent = ["Walker", "Jesse", "Jack", "Kaden", "Bryson", "Dani", "Ayla", "Aleah"]
#rj
random_classwrok_rj = random.randint(1,2)
chance_of_rj_bench_mark = random.randint(1,3)
chanceoffaillingbench_mark_rj = random.randint(1,2)
# if fall 3 times you die
random_classwrok_rj_pick = random.randint(1,2)
#print(RED + list_find_stuff_rj[find_stuff_rj_2] + RESET)
find_stuff_rj = random.randint(0,2)
find_stuff_rj_2 = random.randint(0,2)
find_stuff_rj_3 = random.randint(0,2)
find_stuff_rj_4 = random.randint(0,4)
#Slack
slack_message_rj = random.randint(1,3)
slack_message_sean = random.randint(1,3)
slack_message_brittany = random.randint(1,3)
random_glitch_slack = random.randint(1,4)
random_message_slack = random.randint(1,3)
random_message_slack_1= random.randint(1,3)
#lobby
random_glitch_lobby = random.randint(1,3)

# Colors and Reset var
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
GREY = '\033[90m'
RESET = '\033[0m'

#terminal pictures----------------------------------
king_von = """┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   ██ ▄█▀ ██▓ ███▄    █   ▄████     ██▒   █▓ ▒█████   ███▄    █   │
│   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓██░   █▒▒██▒  ██▒ ██ ▀█   █   │
│  ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░    ▓██  █▒░▒██░  ██▒▓██  ▀█ ██▒  │
│  ▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓     ▒██ █░░▒██   ██░▓██▒  ▐▌██▒  │
│  ▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒      ▒▀█░  ░ ████▓▒░▒██░   ▓██░  │
│  ▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒       ░ ▐░  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒   │
│  ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░       ░ ░░    ░ ▒ ▒░ ░ ░░   ░ ▒░  │
│  ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░         ░░  ░ ░ ░ ▒     ░   ░ ░   │
│  ░  ░    ░           ░       ░          ░      ░ ░           ░   │
│                                        ░                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘"""

the_name_logo = """███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗          
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝          
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝           
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝            
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║             
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝             
                                                                  
██████╗ ██████╗ ██╗   ██╗███████╗ ██████╗ ███╗   ██╗              
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗████╗  ██║              
██████╔╝██████╔╝ ╚████╔╝ ███████╗██║   ██║██╔██╗ ██║              
██╔══██╗██╔══██╗  ╚██╔╝  ╚════██║██║   ██║██║╚██╗██║              
██████╔╝██║  ██║   ██║   ███████║╚██████╔╝██║ ╚████║▄█╗           
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝           
                                                                  
"""

the_logo = """ _____                                                                                       _____ 
( ___ )-------------------------------------------------------------------------------------( ___ )
 |   |                                                                                       |   | 
 |   |                                                                                       |   | 
 |   |  ████████╗██╗  ██╗███████╗    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗      |   | 
 |   |  ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝      |   | 
 |   |     ██║   ███████║█████╗      ██████╔╝███████║   ██║      ██║   ██║     █████╗        |   | 
 |   |     ██║   ██╔══██║██╔══╝      ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝        |   | 
 |   |     ██║   ██║  ██║███████╗    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗      |   | 
 |   |     ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝      |   | 
 |   |                                                                                       |   | 
 |   |   ██████╗ ███████╗                                                                    |   | 
 |   |  ██╔═══██╗██╔════╝                                                                    |   | 
 |   |  ██║   ██║█████╗                                                                      |   | 
 |   |  ██║   ██║██╔══╝                                                                      |   | 
 |   |  ╚██████╔╝██║                                                                         |   | 
 |   |   ╚═════╝ ╚═╝                                                                         |   | 
 |   |                                                                                       |   | 
 |   |  ██████╗  █████╗ ███████╗███████╗         ██████╗ █████╗ ███╗   ███╗██████╗  ██╗██╗   |   | 
 |   |  ██╔══██╗██╔══██╗██╔════╝██╔════╝        ██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔╝╚██╗  |   | 
 |   |  ██████╔╝███████║███████╗█████╗          ██║     ███████║██╔████╔██║██████╔╝██║  ██║  |   | 
 |   |  ██╔══██╗██╔══██║╚════██║██╔══╝          ██║     ██╔══██║██║╚██╔╝██║██╔═══╝ ██║  ██║  |   | 
 |   |  ██████╔╝██║  ██║███████║███████╗███████╗╚██████╗██║  ██║██║ ╚═╝ ██║██║     ╚██╗██╔╝  |   | 
 |   |  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝      ╚═╝╚═╝   |   | 
 |   |                                                                                       |   | 
 |___|                                                                                       |___| 
(_____)-------------------------------------------------------------------------------------(_____)"""


#import functions ----------------------------------------

#clear screen function
def clear_screen():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux and macOS
        _ = os.system('clear')

#sound muisc functions

#the muisic in the background
def play_music_background():
    while True:
        playsound('music/scary-horror-trailer-150087.mp3')
        time.sleep(2)  # Sleep to prevent rapid looping
        playsound('music/dark-horror-background-252905.mp3')

#the muisc during the boss fight
def play_music_background_boss_fight():
    while True:
        playsound('music/evil_boss.mp3')

#text to speech functions
def text_to_speech():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1) # Volume (0.0 to 1.0)
    engine.say(opening_game_info_1)
    engine.runAndWait()

def text_to_speech_main(stuff):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.5) # Volume (0.0 to 1.0)
    engine.say(stuff)
    engine.runAndWait()

#functions for boss fight
def user_attack_func(random_user_attack,user_number_attac_4,mrs_brittany_health,user_number_attac_6,user_number_attac_5):
    if random_user_attack == "Failed Assignment":
        print(GREEN  + f"You attacked with {random_user_attack}!" + RESET)
        print(GREEN  +f"It did {user_number_attac_4} damage." + RESET)
        mrs_brittany_health -= user_number_attac_4
        user_number_attac_4 += 1
        random_user_attack = "AI Code"
    elif random_user_attack == "AI Code":
        print(GREEN  +f"You attacked with {random_user_attack}!")
        print(GREEN  +f"It did {user_number_attac_5} damage." + RESET)
        mrs_brittany_health -= user_number_attac_5
        user_number_attac_4 += 1
        random_user_attack = "Tic-Tac-Toe Project"
    elif random_user_attack == "Tic-Tac-Toe Project":
        print(GREEN  +f"You attacked with {random_user_attack}!" + RESET)
        print(GREEN  +f"It did {user_number_attac_6} damage." + RESET)
        mrs_brittany_health -= user_number_attac_6
        user_number_attac_4 += 1
        random_user_attack = "Failed Assignment"
    return mrs_brittany_health

#For Black Jack ---------------------------------------
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Face cards = 10, Ace = 11
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

def display(player_cards, dealer_cards, reveal_dealer=False):
    print(f"\nYour cards: {player_cards} | Total: {calculate_score(player_cards)}")
    if reveal_dealer:
        print(f"Dealer's cards: {dealer_cards} | Total: {calculate_score(dealer_cards)}")
    else:
        print(f"Dealer's cards: [{dealer_cards[0]}, '?']")

def blackjack():
    print(BLUE + "🂡 Welcome to Blackjack!\n" + RESET)
    player = [deal_card(), deal_card()]
    sean = [deal_card(), deal_card()]
    game_over = False
    while not game_over:
        display(player, sean)
        player_score = calculate_score(player)
        dealer_score = calculate_score(sean)
        if player_score == 21:
            print("\nBlackjack! You win!\n")
        elif player_score > 21:
            display(player, sean, reveal_dealer=True)
            print("\nYou busted! Sean wins.\n")
        action = input("\nType [h] to hit or [s] to stand: ").lower()
        if action == 'h':
            player.append(deal_card())
        elif action == 's':
            game_over = True
        else:
            print(RED + "Invalid input. Please type 'h' or 's'." + RESET)
    # Dealer's turn
    while calculate_score(sean) < 17:
        sean.append(deal_card())
    display(player, sean, reveal_dealer=True)
    player_score = calculate_score(player)
    dealer_score = calculate_score(sean)
    if dealer_score > 21:
        print("\nSean busts! You win!\n")
        time.sleep(3)
        return
    elif dealer_score > player_score:
        print("\nSean wins! He laughs evil-y.\n")
        time.sleep(3)
        return
    elif dealer_score < player_score:
        print("\nYou win! Sean clenches his fist and a vein bulges from his forehead.\n")
        time.sleep(3)
        return
    else:
        print("\nIt's a tie! Sean slams the laptop closed, his face red and angry.\n")
        time.sleep(3)
        return

#For the boss----------------------------------------

health_bar = 5
mrs_brittany_health = 5

#the boss atacks list
list_boss_attacks = ["Long, boring lesson", "Write Up", "a Benchmark"]
list_user_attacks = ["Failed Assignment", "AI Code", "Tic-Tac-Toe Project"]
random_atack = random.choice(list_boss_attacks)
random_user_attack = random.choice(list_user_attacks)

#the random attack they can do
boss_number_attac_1 = random.randint(1,2)
boss_number_attac_2 = random.randint(1,2)
boss_number_attac_3 = random.randint(1,2)
user_number_attac_4 = random.randint(1,3)
user_number_attac_5 = random.randint(1,3)
user_number_attac_6 = random.randint(1,3)

#the user choice functions
def exit_func():
    clear_screen()
    print("You walk out the front door and think about how you're going to be a jobless loser without this program.")
    text_to_speech_main("You walk out the front door and think about how you're going to be a jobless loser without this program.")#here
    time.sleep(2)
    print()
    print("Are you sure you want to leave?")
    text_to_speech_main("Are you sure you want to leave?")
    time.sleep(2)
    print(WHITE + "[yes]\n[no]" + RESET)

def exit_func_2():
    while True:
        user_input = input(GREEN + "=> " + RESET).lower()
        if user_input == 'yes':
            print()
            print(GREEN + "You walk out the front door and never look back." + RESET)
            text_to_speech_main("You walk out the front door and never look back.")
            time.sleep(2)
            print(GREEN + "Congratulations, you have escaped Base Camp!" + RESET)
            text_to_speech_main("Congratulations, you have escaped Base Camp!")
            time.sleep(2)
            print(RED + "Just kidding! You get hit by a bus on the way home. You get a glimpse of Brittany driving just before impact." + RESET)
            time.sleep(2)
            print(RED + "Game Over, the Bad Ending 1/4." + RESET)
            exit()
        elif user_input == 'no':
            print()
            print(GREEN + "You chose to continue your adventure." + RESET)
            time.sleep(2)
            clear_screen()
            break
        else:
            print()
            print("Invalid input. Try again.")

#the class one
def classroom_func_for_choice(random_classwrok_rj,find_stuff_rj,find_stuff_rj_2,chance_of_rj_bench_mark,find_stuff_rj_3):
    print(GREEN + "You are currently in the classroom. RJ sits in the corner desk, deeply involved in his laptop. The rest of the students are gathered around their tables.\n" + RESET)
    while True:
        print("You're doing your work...\n")
        time.sleep(2)
        if random_classwrok_rj == 1:
            while True:
                print(BLUE + "\nTask: Print 'Hello World'" + RESET)
                user_input = input(BLUE + "=> " + RESET)
                if user_input == 'print("Hello World")':
                    print(BLUE + "Congratulations, you have passed the assignment.\n")
                    break
                else:
                    print("False. Try again.\n")
        else:
            print(RED + (list_find_stuff_rj[find_stuff_rj]) + RESET)                    
            list_find_stuff_rj[find_stuff_rj] = "You feel a tap on your shoulder, but when you turn around there's nothing there..."
            time.sleep(4)
            print()
        if random_classwrok_rj == 2:
            while True:
                print(BLUE + "Assignment: Ask the user for their name. (ie. What's your name? )" + RESET)
                user_input = input(BLUE + "=> " + RESET)
                if user_input == """input("What's your name?")""":
                    print(BLUE + "Congratulations, you have passed the assignment.\n")
                    break
                else:
                    print("False. Try again.\n")
        else:
            print(RED + f"{list_find_stuff_rj[find_stuff_rj_2]}\n" + RESET)
            time.sleep(4)
            list_find_stuff_rj[find_stuff_rj] = "You feel a tap on your shoulder, but when you turn around there's nothing there..."
            if chance_of_rj_bench_mark == 3:
                print(BLUE + 'RJ: "Hello student, I hope you are ready for your Benchmark. Go to the benchmark room and we will test your skills... You have two seconds for both lines.' + RESET)
                time.sleep(1)
                print("Type 'RJ'")
                time.sleep(2)
                ben_input_test = input("=> ")
                if ben_input_test != "RJ":
                    print(RED + "RJ laughs evil-y, ", '"You have failed the test, you will be the first sacrifice!"',  + RESET)
                    time.sleep(2)
                    print("Game Over, the Bad Ending 2/4.")
                    exit()
                else:
                    print("You have passed the first test.\n")
                print("Type 'RJ'")    
                ben_input_test = input("=> ")
                if ben_input_test != "RJ":
                    print(RED + "RJ laughs evil-y, ", '"You have failed the test, you will be the first sacrifice!"' + RESET)
                    time.sleep(2)
                    print("Game Over, the Bad Ending 2/4.")
                    exit()
                else:
                    print("Congratulations, you have passed both tests.")
            else:
                print(RED + f"{list_find_stuff_rj[find_stuff_rj_3]}\n" + RESET)
                time.sleep(4)
                list_find_stuff_rj[find_stuff_rj] = "You feel a tap on your shoulder, but when you turn around there's nothing there..."
        clear_screen()
        if interaction_counter < 3:
            print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
            print(WHITE + "[library]\n[check slack]\n[lobby]\n[exit]" + RESET)
            break
        elif interaction_counter >= 3:
            print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
            print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]" + RESET)
            break


#the slack choice function
def slack_func_for_choice(random_glitch_slack,random_message_slack_1,random_message_slack,slack_message_sean,slack_message_rj,slack_message_brittany):
    if random_glitch_slack == 1:
        print(GREEN + "You open Slack and see a message" + RESET)
        time.sleep(1)
        clear_screen()
        print(RED + "You'll never escape..." + RESET) 
        time.sleep(1)
        clear_screen()
        print(GREEN + "You open Slack and see a message:" + RESET)
    if random_message_slack_1 == 2:
        print("You have a new message from your friend Kaden: 'Sean is trying to eat me! HELP!!'")
        print(WHITE + "[respond]\n[ignore]\n[exit]" + RESET)
        user_input = input("=> ")
        if user_input.lower() == 'respond':
            print(GREEN + "You respond: 'Where are you?'" + RESET)
            time.sleep(1)
            print("Kaden: 'I'm in the library, hurry!'\n")
            time.sleep(3)
            print(GREEN + "You rush to the library." + RESET)
            time.sleep(3)
            print(GREEN + "You find Kaden hiding behind a bookshelf, looking terrified." + RESET)
            time.sleep(3)
            print(GREEN + "You help Kaden escape and he thanks you for saving him." + RESET)
            time.sleep(3)
            print(GREEN + "You both decide to leave Base Camp and never come back." + RESET)
            time.sleep(3)
            print(GREEN + "Congratulations, you have escaped Base Camp!" + RESET)
            time.sleep(3)
            print(GREEN + "Just Kidding! Sean eats you both." + RESET)
            time.sleep(1)
            print(RED + "Game Over, the Bad Ending 3/4." + RESET)
            exit()
        else:
            print(GREEN + "You ignore the message and continue with your day." + RESET)
            time.sleep(1)
            print(GREEN + "You hear a scream from the library, but you pretend not to hear it.\n" + RESET)
            time.sleep(1)
    if random_message_slack == 3:
        print("There's a new message from Aiden: 'Wanna go bowling later?'")
        time.sleep(2)
        print("You ignore the message.\n")
        time.sleep(3)
    if random_message_slack == 4:
        print("You see a message in the procurement leadership team channel.")
        print("Dani: 'Sean, there's maggots in the food again!!'")
        time.sleep(2)
        print("Sean: 'It's all part of the plan...'")
        time.sleep(2)
        print("You pretend like you didn't just read that.\n")
        time.sleep(2)            
    if slack_message_rj == 2:
        print(GREEN + "You open Slack and see a message from RJ in the #year10 channel:" + RESET)      
        print("@Channel don't forget to study for the benchmark... you don't wanna know what happens if you fail 3 times!\n")
        time.sleep(2)                
    if slack_message_brittany == 2:
        print(GREEN + "You see a message from Ms. Brittany in the #year10:" + RESET)
        print("@Channel be preparred for today's lesson!\n")
        time.sleep(2)            
    if slack_message_sean == 2:        
        print(GREEN + "Opening up Slack, you see a message from Sean in the #year10 channel:" + RESET)
        print("@Channel the chores today is to sweep! Don't forget or else...\n")
        time.sleep(2)
    print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
    if interaction_counter < 3:
        print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]" + RESET) 
        return           
    elif interaction_counter >= 3:
        print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[Mrs. Brittany's Office]\n[exit]" + RESET)
        return
    

#the lobby choice function
def lobby_func_for_choice(random_glitch_lobby,random_message_slack_1,random_lobby_game):
    print(GREEN + "You are now in the lobby. It's mostly empty and you notice a strange smell coming from the kitchen.\n" + RESET)
    while True:
        print("\nYou look around the lobby...\n")
        time.sleep(2)     
        print(f"{the_random_lobby_1}\n")
        time.sleep(2)
        print(f"{the_random_lobby_2}\n")
        time.sleep(2)        
        if random_lobby_game == 1:#bug fix
            while True:
                print(GREEN + "\nYou see Sean playing a game on his computer." + RESET)
                time.sleep(2)
                print(GREEN + "He looks up and says, 'Hey, wanna play Black Jack?' With an evil smile." + RESET)
                time.sleep(2)
                print(WHITE + "Do you want to play Black Jack with Sean?" + RESET)
                print(WHITE + "[yes]\n[no]" + RESET)
                user_input = input(GREEN + "=> " +  RESET)
                if user_input == 'yes' or user_input == 'y':
                    blackjack()
                    break
                elif user_input == 'no':
                    print(RED + "\nYou reject his offer. Sean looks like he's angry with you, but you walk away before he can say anything.\n" + RESET)
                    time.sleep(3)
                else:
                    print(RED + "Invalid Input." + RESET)
        time.sleep(3)
        clear_screen()
        print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
        if interaction_counter < 3:
            print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]" + RESET)
            break
        elif interaction_counter >= 3:
            print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[Mrs. Brittany's Office]\n[exit]" + RESET)
            break
        if random_lobby_game == 2 or random_lobby_game == 3:
            while True:
                print(GREEN + "You see some of your classmates going to play ping pong. They ask if you want to play." + RESET)
                time.sleep(2)
                print(WHITE + "Join them?" + RESET)
                print(WHITE + "[yes]\n[no]" + RESET)
                user_input = input(GREEN + "=> " + RESET).lower()
                if user_input == 'yes' or user_input == 'y':
                    random.choice(ping_pong_opponent)
                    the_random_person_game = random.choice(ping_pong_opponent)
                    print(f"\nYour opponent is {the_random_person_game}!\n")
                    time.sleep(2)
                    if the_random_person_game == 'Walker':
                        print(GREEN + "\nWalker puts you in a washing machine with his technical shots." + RESET)
                    elif the_random_person_game == 'Jesse':
                        print(GREEN + "\nYou get caffeine patched on the first serve!" + RESET)
                    elif the_random_person_game == 'Jack':
                        print(GREEN + "\nYou skunk him in both matches." + RESET)
                        time.sleep(2)
                        print(GREEN + "He puts you in an arm bar until you tap." + RESET)
                    elif the_random_person_game == 'Kaden':
                        print(GREEN + "\nKaden only has one arm (you swear there's bite marks), and you get up 9-0 early." + RESET)
                        time.sleep(2)
                        print(GREEN + "He says 'I'll start trying,' and you end up losing." + RESET)    
                    elif the_random_person_game == 'Bryson':
                        print(GREEN + "\nHe jumps up and slams the ball so hard it breaks the table." + RESET)
                        time.sleep(2)
                        print(GREEN + "He is so cool!!!" + RESET)
                        time.sleep(2)
                        print(GREEN + "You wish you were like Bryson." + RESET)
                    elif the_random_person_game == 'Dani':
                        print(GREEN + "\nDani hits the ball so hard it puts a hole in the wall behind your head." + RESET)
                        time.sleep(2)
                        print(GREEN + "You decide to quit playing early." + RESET)
                    elif the_random_person_game == 'Ayla':
                        print(GREEN + "\nShe misses every shot, swearing: 'It's just a warm-up!'" + RESET)
                    elif the_random_person_game == 'Aleah':
                        print(GREEN + "\nAleah makes fun of every shot you make. It makes you sad." + RESET)
                    time.sleep(3)
                    print("\nSean walks in and shushes everybody, yelling, 'There's people trying to work! Get back to the classrooms.'\n")
                    break  
                elif user_input == 'no' or user_input == 'n':
                    time.sleep(2)
                    print(GREEN + "\nYou tell them no and go back to the lobby." + RESET)
                    break
                else:
                    print(RED + "\nInvalid input." + RESET)
            clear_screen()
            print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
            if interaction_counter < 3:
                print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]" + RESET)
                break
            elif interaction_counter >= 3:
                print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[Mrs. Brittany's Office]\n[exit]" + RESET)
                break
        if random_glitch_lobby == 1:
            print(RED + "\nYou see a strange figure in the corner of your eye, but when you turn to look, it's gone.\n" + RESET)
            time.sleep(2)
            return#bug fix
        if random_message_slack_1 == 2:
            print(GREEN + "" + RESET)
            print("\nSean: 'Don't forget to clean the kitchen!'\n")
            time.sleep(2)
            return
        if random_glitch_lobby == 3:
            print(RED + "\nThe lights flicker and you hear a strange noise coming from the kitchen.\n" + RESET)
            time.sleep(2)
            return
        if random_glitch_lobby == 4:
            print(RED + "\nYou feel a cold breeze pass through you, but there's no open windows.\n" + RESET)
            time.sleep(2)
            return
#the library choice function
def library_func_for_choice():
    print(GREEN + "Walking into the library, you notice nothing out of the ordinary." + RESET)
    time.sleep(2)
    print(GREEN + "You see a few books stacked on the shelves." + RESET)
    time.sleep(2)

    while True:
        print(WHITE + "\nView the Books?" + RESET)
        print(WHITE + "[yes]\n[no]\n" + RESET)
        choice = input(GREEN + "=> " + RESET).lower()
        if choice == 'yes':
            time.sleep(2)
            print(GREEN + "\nYou can choose from the following books:" + RESET)
            for b in books:
                print(f"{b}")
            choice = input(GREEN + "=> " + RESET).lower()
            time.sleep(2)
            print("\nPicking up the book, you turn it over and read the back.\n")
            if choice == "god don't like ugly":
                time.sleep(2)
                print("When you turn the book on it's side you catch a slip of paper falling out of the pages.")
                print(WHITE + "\nView the note?" + RESET)
                print(WHITE + "[yes]\n[no]" + RESET)
                user_note = input(GREEN + "=> " + RESET).lower()
                if user_note == 'yes':
                    print("You open up the note, seeing five numbers scrawled in messy handwriting: " \
                    "\n51469")
                    time.sleep(2)
                    print("Flipping the note over you see a quickly written signature.")
                    time.sleep(3)
                    clear_screen()
                    print(RED + king_von + RESET)
                    time.sleep(4)
                    clear_screen()
                    return
                elif user_note == 'no':
                    print("You slip the paper back into place.")
                    return
            elif choice == 'harry potter and the chamber of secrets':
                print(chamber_secrets)
            elif choice == '1984':
                print(nineteen)
            elif choice == 'fahrenheit 451':
                print(fahrenheit)
            elif choice == 'dune':
                print(dune)
            time.sleep(2)
        elif choice == 'no':
            print(GREEN + "You decide to leave the library, finding nothing of interest.\n" + RESET)
            print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
            if interaction_counter < 3:
                print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]" + RESET)
                return
            elif interaction_counter >= 3:
                print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[Ms. Brittany's Office]\n[exit]" + RESET)
                return
        else:
            print(RED + "Invalid input." + RESET)

def boss_fight_func_for_choice(user_name,random_user_attack,mrs_brittany_health,random_atack,boss_number_attac_1,boss_number_attac_2,boss_number_attac_3,user_number_attac_4,user_number_attac_6,user_number_attac_5):
    print(GREEN + "Theres a key pad next to the door. You need a passcode." + RESET)
    user_code = int(input(GREEN + "=> " + RESET))
    if user_code == 51469 or 1:#1 if you just want to skip to it
        time.sleep(3)
        my_thread_boss = threading.Thread(target=play_music_background_boss_fight, args=())
        clear_screen()
        my_thread_boss.start()
        text_to_speech_main("Brittany suddenly appears, frightening and imposing in her stance.")
        print(RED + "Brittany suddenly appears, frightening and imposing in her stance!" + RESET)
        health_bar = 5
        time.sleep(3)
        print(RED + f"\nYOU WILL NEVER ESCAPE {user_name}!!" + RESET)
        time.sleep(3)
        clear_screen()
        while True:
            if health_bar == 5:
                print(BLUE + f"Your health ❤️ ❤️ ❤️ ❤️ ❤️" + RESET)
            elif health_bar == 4:
                print(BLUE + f"{user_name} health ❤️ ❤️ ❤️ ❤️ 💔" + RESET)
            elif health_bar == 3:
                print(BLUE + f"{user_name} health ❤️ ❤️ ❤️ 💔 💔" + RESET)
            elif health_bar == 2:
                print(BLUE + f"{user_name} health ❤️ ❤️ 💔 💔 💔" + RESET)
            elif health_bar == 1:
                print(BLUE + f"{user_name} health ❤️ 💔 💔 💔 💔" + RESET)
            elif health_bar <= 0:
                time.sleep(2)
                clear_screen()
                print(RED + f"{user_name} was defeated by Brittany." + RESET)
                print(RED + "\nThe last thing you see is Sean, RJ, and Brittany sacrificing you to the Software God, Kagan." + RESET)
                time.sleep(10)
                clear_screen()
                exit()
            print()#spacing
            time.sleep(2)
            if mrs_brittany_health == 5:
                print(MAGENTA + "Mrs Brittany 🖤 🖤 🖤 🖤 🖤" + RESET)
            elif mrs_brittany_health == 4:
                print(MAGENTA + "Mrs Brittany 🖤 🖤 🖤 🖤 💔" + RESET)
            elif mrs_brittany_health == 3:
                print(MAGENTA + "Mrs Brittany 🖤 🖤 🖤 💔 💔" + RESET)
            elif mrs_brittany_health == 2:
                print(MAGENTA + "Mrs Brittany 🖤 🖤 💔 💔 💔" + RESET)
            elif mrs_brittany_health == 1:
                print(MAGENTA + "Mrs Brittany 🖤 💔 💔 💔 💔" + RESET)
            elif mrs_brittany_health <= 0:
                time.sleep(2)
                clear_screen()
                print("You win!")
                time.sleep(3)
                print(GREEN +"\nWalking out of the office, you see Sean and RJ looking distrought and confused." + RESET)
                time.sleep(2)
                print(GREEN + "They don't stop you as you pass by them..." + RESET)
                print(GREEN + "Walking out of the front door, you bask in the sunshine as you walk home, finally free from Base Camp." + RESET)
                print(GREEN + "\nGame Over, the Good Ending." + RESET)
                return
            time.sleep(2)
            #boss
            if random_atack == "Long, boring lesson":
                print(RED + f"Mrs. Brittany attacked with {random_atack}!" + RESET)
                print(RED + f"It did {boss_number_attac_1} damage.\n" + RESET)
                health_bar -= boss_number_attac_1
                boss_number_attac_1 += 1
                random_atack = "Write Up"
                mrs_brittany_health = user_attack_func(random_user_attack,user_number_attac_4,mrs_brittany_health,user_number_attac_6,user_number_attac_5)
                time.sleep(2)
            elif random_atack == "Write Up":
                print(RED + f"Mrs. Brittany attacked with {random_atack}!" + RESET)
                print(RED + f"It did {boss_number_attac_2} damage." + RESET)
                print()
                health_bar -= boss_number_attac_2
                boss_number_attac_1 += 1
                random_atack = "A benchmark"
                mrs_brittany_health = user_attack_func(random_user_attack,user_number_attac_4,mrs_brittany_health,user_number_attac_6,user_number_attac_5)
                time.sleep(2)
            elif random_atack == "A benchmark":
                print(RED + f"Mrs. Brittany attacked with {random_atack}!" + RESET)
                print(RED + f"It did {boss_number_attac_3} damage." + RESET)
                print()
                health_bar -= boss_number_attac_3
                boss_number_attac_1 += 1
                random_atack = "Long, boring lesson"
                time.sleep(2)
                mrs_brittany_health = user_attack_func(random_user_attack,user_number_attac_4,mrs_brittany_health,user_number_attac_6,user_number_attac_5)            
            #User attacks
            time.sleep(3)#4
            clear_screen()
            print(RED + "KEEP FIGHTING?" + RESET)
            print(GREEN + "[yes]\n[no]" + RESET)
            user_boss_fight_input = input(GREEN + "=> " + RESET).lower()
            if user_boss_fight_input == 'no':
                print(RED +"You run out of the office..."+ RESET)
                time.sleep(2)
                print()
                print(RED + "You're met by Sean and Rj." + RESET)
                time.sleep(2)
                print()
                print(RED + f"{user_name} is taken away and never seen again." + RESET)
                print(RED + "\nGame Over, the Bad Ending 4/4." + RESET)
                time.sleep(10)
                exit()
            elif user_boss_fight_input == 'yes':
                continue
    else:
        print(RED + "Wrong passcode" + RESET)

#The main loop---------------------------------------------------------

#clears the clear so there is not junk in the start of the game
clear_screen()

#Making the threads run and play the muisc
my_thread = threading.Thread(target=play_music_background, args=())
my_thread.start()

#Making the logo for the game
print(GREY + the_name_logo + RESET)
time.sleep(5)

#Make the title for the game
clear_screen()#clearing to get rid of the logo
print(BLUE + the_logo + RESET)
time.sleep(3)
clear_screen()#clearing to effect
print(RED + the_logo + RESET)
time.sleep(0.5)
clear_screen()#clearing to effect
print(BLUE + the_logo + RESET)
time.sleep(1)
clear_screen()#clearing to it go away
print(RED + the_logo + RESET)
time.sleep(3)

#Get the user input for the game settings
print("\n")#for spacing
user_name = input(GREY + "Enter your name: " + RESET)
time.sleep(0.5)
print("\n")

#starting the 2nd thread for the reading of the intro
my_thread_2 = threading.Thread(target=text_to_speech, args=())
my_thread_2.start()

#printing off the intro letter by letter for the effect
for char_1 in opening_game_info_1:
    print(RED + char_1 + RESET, end='', flush=True)
    time.sleep(0.05)

#Making the button that checks if the user wants to continue
print()
time.sleep(1.5)
user_input_zero = input("Press enter to continue> ")
print()

#clear the screen for start of the play through and wait a little
clear_screen()
time.sleep(2)

#scary warining
print(RED + "You have been warned..." + RESET)
text_to_speech_main("you have been warned")
time.sleep(2)
clear_screen()

#starting choices for the user
print(GREEN + "You sit at your desk, dreading what's to come." + RESET)
print()
print(GREEN + "Where do you want to go? (type 'exit' to quit): " + RESET)
print(WHITE + "[classroom]\n[lobby]\n[library]\n[check slack]\n[exit]\n" + RESET)

#the while loop for the game main loop
while True:
    #the user input choice
    choice = input(GREEN + "=> " + RESET).lower()
    clear_screen()
    if choice == 'exit':
        exit_func()
        #the while loop for the user exit func
        exit_func_2()
    elif choice == 'classroom':
        interaction_counter += 1
        classroom_func_for_choice(random_classwrok_rj,find_stuff_rj,find_stuff_rj_2,chance_of_rj_bench_mark,find_stuff_rj_3)
    elif choice == 'check slack':
        interaction_counter += 1
        slack_func_for_choice(random_glitch_slack,random_message_slack_1,random_message_slack,slack_message_sean,slack_message_rj,slack_message_brittany)
    elif choice == 'lobby':
        interaction_counter += 1
        lobby_func_for_choice(random_glitch_lobby,random_message_slack_1,random_lobby_game)
    elif choice == 'library':
        interaction_counter +=1
        library_func_for_choice()
    elif choice == "Ms. Brittany's Office" or choice == 'boss':
        boss_fight_func_for_choice(user_name,random_user_attack,mrs_brittany_health,random_atack,boss_number_attac_1,boss_number_attac_2,boss_number_attac_3,user_number_attac_4,user_number_attac_6,user_number_attac_5)
    else:
        print(RED + "Invalid location, please try again." + RESET)