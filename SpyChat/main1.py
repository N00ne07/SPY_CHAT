from spy_details import spy, Spy, friends, ChatMessage

from steganography.steganography import Steganography

from colorama import init
from termcolor import colored

init()
STATUS_MESSAGES = ['Boost is the secret of my energy!', 'What a drag!', "Live and Let Live",
                   "Diamonds are forever!", "Disappointed, but not surprised.", "What in the w...!"]

print(colored("Hello friend, warm welcomes!", "cyan"))

print ("Let\'s get started, shall we?")

question = "Do you want to continue as the default user-" + spy.salutation + " " + spy.name + " or create a new user? (Y/N): "
existing = input(colored(question, "cyan"))


def add_status():
    updated_status_message = None

    if spy.current_status_message is not None:
        print ('Your current status message is %s \n' % spy.current_status_message)
    else:
        print('You don\'t have any status message currently \n')

    default = input(colored("Do you want to select from the older status (y/n)? ", "magenta"))

    if default.upper() == "N":
        new_status_message = input(colored("What status message do you want to see?: ", "magenta"))

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print ('%d. %s' % (item_position, message))
            item_position = item_position + 1

        message_selection = int(input(colored("\nChoose the index of the status: ", "magenta")))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print ('The option you chose is not valid! Press either Y or N.')

    if updated_status_message:
        print ('Your updated status message is:',)
        print(colored(updated_status_message, "yellow"))

    else:
        print(colored('You did not update your status message','magenta'))

    return updated_status_message


def add_friend():
    new_friend = Spy(" ", " ", 0)
    new_friend.name = input("Please add your friend's name: ")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.age = input("Age?: ")
    new_friend.age = int(new_friend.age)

    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and 12 < new_friend.age < 50 and (new_friend.salutation== "Ms." or new_friend.salutation== "Mr."):

        friends.append(new_friend)
        print(colored('Friend Added!', "cyan"))
    else:
        print(colored("Sorry, the friend cannot be added!!", "blue"))

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print ('%d. %s %s aged %d is online' % (item_number + 1, friend.salutation, friend.name, friend.age))

        item_number = item_number + 1

    friend_choice = input(colored("Choose the index of the friend: ", "magenta"))
    friend_choice_position = int(friend_choice) - 1

    if friend_choice_position> len(friends)-1:
        print(colored("Sorry,This friend is not present.", 'green'))
        exit()

    else:
        return friend_choice_position


def send_a_message():
    friend_choice = select_a_friend()

    original_image = input("What is the name of the image?: ")

    output_path = "out"+original_image
    text = input("What do you want to say? ")

    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print(colored("Your secret message image is ready!", "yellow"))


def send_message_help():
    friend_choice = select_a_friend()
    text = "I am coming to save you. Don't worry "
    new_chat = ChatMessage(text, True)
    friends[friend_choice].chats.append(new_chat)


def read_a_message():
    sender = select_a_friend()
    output_path = input("What is the name of the image file?: ")

    try:
        secret_text = Steganography.decode(output_path)
        print ("The secret message you read is",)
        print (colored(secret_text, 'magenta'))
        words = secret_text.split()
        new = (secret_text.upper()).split()

        friends[sender].count += len(words)

        if "SOS" in new or "SAVE" in new or "HELP" in new or "AID" in new or "ACCIDENT" in new or "RESCUE" in "ALERT" in new or "ALARM" in new or "CRISIS" in new:

            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow'))

            print (colored("The friend that sent this message needs an emergency.", 'green'))
            print (colored("PLease help your friend by sending a helping message.", 'green'))
            print (colored("Select that friend to send him a helping message.", 'red'))

            send_message_help()
            print(colored("You have sent a message to help your friend.", 'magenta'))

            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)

        else:
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print(colored("Your secret message has been saved!", 'yellow'))

        print ("Average words said by",)
        print(colored(friends[sender].name, "blue")),
        print ("is",)
        print(colored(friends[sender].count, "red"))

        if len(words) > 100:
            print(colored(friends[sender].name, 'blue')),
            print(colored("Removed from friends list. What a chatter box!", "yellow"))
            friends.remove(friends[sender])

    except TypeError:
        print(colored("Nothing to decode from the image as it contains no secret message.", 'red'))


def read_chat_history():
    read_for = select_a_friend()

    print ('\n')

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            print(colored("You said:", 'red')),
            print (str(chat.message))
        else:
            print(colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", 'blue')),
            print(colored(str(friends[read_for].name) + " said:", 'red')),
            print (str(chat.message))


def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name
    if 12 < spy.age < 50:

        print("Authentication complete.")
        print(colored("Welcome " + str(spy.name), "magenta"))
        print(colored("Your age:" + str(spy.age), "magenta"))
        print(colored("Bravo!Proud to have you on board.", "yellow"))

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats History \n" \
                           " 6. Close Application \n"
            menu_choice = input(colored(menu_choices, "cyan"))

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print ('You have %d friends' % number_of_friends)

                elif menu_choice == 3:
                    send_a_message()

                elif menu_choice == 4:
                    read_a_message()

                elif menu_choice == 5:
                    read_chat_history()

                elif menu_choice == 6:
                    print(colored("Successfully closed", "green"))
                    show_menu = False

                else:
                    print(colored("That was a wrong choice.", 'green'))
                    exit()

    else:
        if spy.age <= 12:
            print("Sorry, you are too young to become a spy!")
        elif spy.age >= 50:
            print("Sorry, you are too old to be a spy!")


if existing.upper() == "Y":
    start_chat(spy)
elif existing.upper() == "N":
    spy = Spy(" ", " ", 0)

    spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0 and spy.name.isdigit() == False:
        spy.salutation = input("What should we call you? Mr. or Ms.?")
        if len(spy.salutation) > 0:

            spy.age = input("Please enter your age: ")

            if len(spy.age) > 0:
                spy.age = int(spy.age)
                if 12 <= spy.age < 50:
                    print("Welcome to Secret Chat")
                    spy.is_online = True
                    start_chat(spy)

                else:
                    if spy.age <= 12:
                        print(colored("Sorry, you are too young to become a spy!", 'red'))
                    elif spy.age >= 50:
                        print(colored("Sorry, you are too old to be a spy!", 'red'))
                    else:
                        print(colored("Please enter a valid age", 'red'))

            else:
                print("Please enter your age")

        else:
            print("Please enter a valid salutation")

    else:
        print("Please enter a valid name")

else:
    print(colored("You did not reply with a yes(Y) or no(N)!", 'green'))
    print(colored("Need to run the program again.", 'green'))
    exit()
