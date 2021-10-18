from random import randint, choice, shuffle
import pyperclip

# DEFINING GLOBAL VARIABLES

LOWER_CASE_ALPHABETS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER_CASE_ALPHABETS = [char.upper() for char in LOWER_CASE_ALPHABETS]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL_CHARACTERS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# FLAGS FOR INPUT LOGIC
password_type_chosen = False
password_length_config_chosen = False

# INPUT LOGIC FOR PASSWORD LENGTH CONFIGURATION
while not password_type_chosen or not password_length_config_chosen:
    if not password_type_chosen:
        password_type = input("Enter the password type you wish to generate.\nSimple: S\nComplex: C\n")
        if password_type.lower() == 'c' or password_type.lower() == 's':
            password_type_chosen = True
        else:
            print("Please choose a valid type.\nEnter 'C' for Complex or 'S' for Simple.\n")

    if not password_length_config_chosen and password_type_chosen:
        if password_type.lower() == 'c':
            try:
                min_length, max_length = [int(_) for _ in
                                          input("Enter the minimum and maximum length of password "
                                                "respectively(separated by comma and without any space) "
                                                "you wish to generate: ").split(',')]
                if min_length > max_length:
                    raise ValueError

                min_lowercase, max_lowercase = [int(_) for _ in
                                                input("Enter the minimum and maximum number of lowercase alphabets "
                                                      "respectively(separated by comma and without any space) "
                                                      "you wish to include in your password: ").split(',')]
                if min_lowercase > max_lowercase:
                    raise ValueError

                min_uppercase, max_uppercase = [int(_) for _ in
                                                input("Enter the minimum and maximum number of uppercase alphabets "
                                                      "respectively(separated by comma and without any space) "
                                                      "you wish to include in your password: ").split(',')]
                if min_uppercase > max_uppercase:
                    raise ValueError

                min_numeric, max_numeric = [int(_) for _ in
                                            input("Enter the minimum and maximum number of numeric characters "
                                                  "respectively(separated by comma and without any space) "
                                                  "you wish to include in your password: ").split(',')]
                if min_numeric > max_numeric:
                    raise ValueError

                min_special, max_special = [int(_) for _ in
                                            input("Enter the minimum and maximum number of special characters "
                                                  "respectively(separated by comma and without any space) "
                                                  "you wish to include in your password: ").split(',')]
                if min_special > max_special:
                    raise ValueError

                password_length_config_chosen = True


            except ValueError:
                print("WRONG INPUT!! Please enter the minimum and maximum values in proper order and format"
                      " (two integer values separated by comma without any space)\n")

            if password_length_config_chosen:
                sum_individual_min_lengths = min_lowercase + min_uppercase + min_numeric + min_special

                sum_individual_max_lengths = max_lowercase + max_uppercase + max_numeric + max_special

                if sum_individual_min_lengths < min_length \
                        or sum_individual_max_lengths > max_length \
                        or sum_individual_max_lengths < min_length \
                        or sum_individual_min_lengths > max_length \
                        or sum_individual_min_lengths > sum_individual_max_lengths:
                    print("INVALID LENGTHS!! Password lengths don't add up. Please make sure individual "
                          "lengths chosen do not exceed the maximum length and is at least greater than "
                          "the minimum length\n")
                    password_length_config_chosen = False

        elif password_type.lower() == 's':
            try:
                min_length, max_length = [int(_) for _ in
                                          input("Enter the minimum and maximum length of password "
                                                "respectively(separated by comma and without any space) "
                                                "you wish to generate: ").split(',')]
                if min_length > max_length:
                    raise ValueError

                password_length_config_chosen = True

            except ValueError:
                print("WRONG INPUT!! Please enter the minimum and maximum values in proper order and format"
                      " (two integer values separated by comma without any space)\n")


# PASSWORD GENERATION ACCORDING TO THE TYPE CHOSEN

if password_type.lower() == 's':
    password_alphabets = [choice(LOWER_CASE_ALPHABETS) for _ in range(randint(min_length, max_length))]

    shuffle(password_alphabets)

    password = "".join(password_alphabets)
    print(f"Your simple password is {password}")

    pyperclip.copy(password)  # COPIES THE PASSWORD IN CLIPBOARD FOR INSTANT COPY

elif password_type.lower() == 'c':
    password_lower_alphabets = [choice(LOWER_CASE_ALPHABETS) for _ in range(randint(min_lowercase, max_lowercase))]
    password_upper_alphabets = [choice(UPPER_CASE_ALPHABETS) for _ in range(randint(min_uppercase, max_uppercase))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(min_numeric, max_numeric))]
    password_special = [choice(SPECIAL_CHARACTERS) for _ in range(randint(min_special, max_special))]

    password_list = password_lower_alphabets + password_upper_alphabets + password_numbers + password_special

    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your complex password is {password}")

    pyperclip.copy(password)  # COPIES THE PASSWORD IN CLIPBOARD FOR INSTANT COPY
