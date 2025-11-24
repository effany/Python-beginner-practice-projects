#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as file:
        letter_content = file.read()
        with open("Input/Names/invited_names.txt") as names:
            names_strings = names.readlines()
        for name in names_strings:
            with open(f"Output/ReadyToSend/{name.strip()}.txt", "w") as new_file:
                personalized_letter = letter_content.replace("[name]", name.strip())
                new_file.write(personalized_letter)