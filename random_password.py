import random

mix_character = ["A", "C", "a" , "d" , "@", "#", "D" , "1", "3", "5", "H", "!", "&", "F", "K"]

random.shuffle(mix_character)

random_password = mix_character[1] + mix_character[3] + mix_character[5] + mix_character[2] + mix_character[8] + mix_character[9] + mix_character[4] + mix_character[13] + mix_character [14]


print(f"Random Password is : {random_password}")