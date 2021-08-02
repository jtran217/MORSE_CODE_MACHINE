# DICTIONARY
morse_code = {'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-'}

# SCRIPT FOR MORSE CODE MACHINE
condition = True
while condition:

    # ASK USER WHETHER THEY WANT TO CONVERT TEXT OR TRANSLATE MORSE
    print("Welcome to the morse code machine v1!")
    mode_choice = input('What mode would you like to use? "C": Converter, "T" for translator ')
    mode_choice = mode_choice.capitalize()

    # USER CHOOSE TO CONVERT TEXT --> MORSE

    if mode_choice[0] == 'C':
        user_text = input("Please enter the text you would like to convert to morse: ").upper()
        converted_text = ''
        #Filter through user_text and generate morse code with '/' to separate words, space for letters
        for letter in user_text:
            if letter == ' ':
                converted_text += '/'
            else:
                converted_text = converted_text + morse_code[letter] + ' '

        print(f"Here is your encrypted message: {converted_text} "
              )
        # ASK IF USER WOULD LIKE TO CONTINUE TO USE SCRIPT
        repeat = input(
            "Would you like to continue to use the morse code machine v1? Type 'Y' for Yes or 'N' for No ").capitalize()
        if repeat[0] == 'N':
            condition = False
            print("SHUTTING DOWN MORSE CODE MACHINE ")
        elif repeat[0] == 'Y':
            print("Restarting Machine!")
        else:
            print("Sorry that is not a valid response! Ending Morse Code Machine V1")
            condition = False


    #USER CHOOSE TO TRANSLATE MORSE TO TEXT
    elif mode_choice[0] == 'T':
        code_to_convert = input("Please enter the morse code here, making sure to have appropriate /:  ")
        #SPLIT TEXT BASED ON location
        code_to_convert = code_to_convert.split('/')
        translated_code = ''
        pair = morse_code.items()
        for text in code_to_convert:
            word = text.split(' ')
            for code in word:
                for key,value in pair:
                    if code == value:
                        translated_code += key
            translated_code += ' '
        print(f"The message encoded in the morse code was:  {translated_code}")
        #ASK IF USER WOULD LIKE TO CONTINUE TO USE SCRIPT
        repeat = input(
            "Would you like to continue to use the morse code machine v1? Type 'Y' for Yes or 'N' for No ").capitalize()
        if repeat[0] == 'N':
            condition = False
            print("SHUTTING DOWN MORSE CODE MACHINE ")
        elif repeat[0] == 'Y':
            print("Restarting Machine!")
        else:
            print("Sorry that is not a valid response! Ending Morse Code Machine V1")
            condition = False
    else:
        print("You have not entered a proper response! Please Try Again")












