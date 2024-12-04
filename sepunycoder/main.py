import argparse
import json
import os
import time

def translte_to_cyrillic(text, punycode_table):
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

def main():
    green_color = "\033[1;32m"
    end_color = "\033[0m"

    banner = r'''{}
      ______ _______ ______                                  _
     / _____|_______|_____ \                                | |
    ( (____  _____   _____) )   _ ____  _   _  ____ ___   __| |_____  ____
     \____ \|  ___) |  ____/ | | |  _ \| | | |/ ___) _ \ / _  | ___ |/ ___)
     _____) ) |_____| |    | |_| | | | | |_| ( (__| |_| ( (_| | ____| |
    (______/|_______)_|    |____/|_| |_|\__  |\____)___/ \____|_____)_|
                                       (____/                              Social Engineering Punycoder
                                                                            by @hackermater
    {}'''.format(green_color, end_color)
    for line in banner.split('\n'):
        print(line)
        time.sleep(0.08)

    parser = argparse.ArgumentParser(description="Translate text to Cyrillic punycode.")
    parser.add_argument('--file', type=str, help="Input file containing the text to translate")
    parser.add_argument('--output', type=str, help="Output file to save the translated text")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    punycode_table_path = os.path.join(script_dir, "punycode_chars.json")

    with open(punycode_table_path, 'r') as json_file:
        data = json.load(json_file)
        punycode_table = data["punycode_table"]

    if args.file:
        with open(args.file, 'r') as file:
            user_input = file.read()
        output_text = translte_to_cyrillic(user_input, punycode_table)
    else:
        user_input = input("🔓 Enter the text to translate to Cyrillic: ")
        user_input_https = input("🔗 Do you want to add \"https://\" protocol? (y/n): ")
        output_text = translte_to_cyrillic(user_input, punycode_table)
        if user_input_https.lower() == "y":
            output_text = "https://" + output_text

    if args.output:
        with open(args.output, 'w') as file:
            file.write(output_text)
        print(f"👀 Translated text saved to {args.output}")
    else:
        print("👀 Translated text:", output_text)

if __name__ == "__main__":
    main()
