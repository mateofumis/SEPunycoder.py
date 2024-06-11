#!/usr/bin/python3
import time
import os
def translte_to_cyrillic(text):
    punycode_table = {
        'a': 'а', 'b': 'в', 'r': 'г', 'e': 'е',
        'k': 'к', 'o': 'о', 'p': 'р', 'c': 'с',
        'y': 'у', 'x': 'х'
    }
    
    result = ''
    for char in text:
        if char.lower() in punycode_table:
            if char.isupper():
                result += punycode_table[char.lower()].upper()
            else:
                result += punycode_table[char.lower()]
        else:
            result += char
    
    return result

# Colors
green_color = "\033[1;32m"
end_color = "\033[0m"
red_color = "\033[1;31m"
blue_color = "\033[1;34m"
yellow_color = "\033[1;33m"
purple_color = "\033[1;35m"
turquoise_color = "\033[1;36m"
gray_color = "\033[1;37m"

# Print Welcome Banner
banner='''{} 
  ______ _______ ______                                  _             
 / _____|_______|_____ \                                | |            
( (____  _____   _____) )   _ ____  _   _  ____ ___   __| |_____  ____ 
 \____ \|  ___) |  ____/ | | |  _ \| | | |/ ___) _ \ / _  | ___ |/ ___)
 _____) ) |_____| |    | |_| | | | | |_| ( (__| |_| ( (_| | ____| |    
(______/|_______)_|    |____/|_| |_|\__  |\____)___/ \____|_____)_|    
                                   (____/                              Social Engineering Punycoder
                                                                        by @hackermater
{}'''.format(green_color, end_color)
lines = banner.split('\n')
for line in lines:
    print(line)
    time.sleep(0.08)

# Get user Input for Text to Translate
user_input = input("🔓 Enter the text to translate to Cyrillic: ")
user_input_https = input("🔗 Do you want to add \"https://\" protocol? (y/n): ")
output_text = translte_to_cyrillic(user_input)
if user_input_https == "y":
    output_text = "https://" + output_text
    print("👀 Translated text:", output_text)
elif user_input_https == "n":
    print("👀 Translated text:", output_text)
else:
    print("👀 Translated text:", output_text)
