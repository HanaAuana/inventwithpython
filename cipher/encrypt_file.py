import time
import os
import sys
import transposition


class InvalidInputException(Exception):
    pass


def main():
    mode = input("Enter 'E' to encrypt or 'D' to decrypt ")
    input_filename = input('Enter filename for input text: ')
    if not os.path.exists(input_filename):
        raise InvalidInputException("Input file does not exist")
    output_filename = input('Enter filename for output: ')
    if os.path.exists(output_filename):
        proceed = input("Output filename already exists. Continue? (Y/N)")
        if proceed not in ('Y', 'y', 'yes'):
            sys.exit()
    key = int(input('Enter the key value: '))

    text = ''
    with open(input_filename, encoding='utf-8') as input_file:
        text = input_file.read()
    start_translate_time = time.time()
    if mode in ('E', 'e', 'encrypt'):
        translated = transposition.encode_transposition(text, key)
    elif mode in ('D', 'd', 'decrypt'):
        translated = transposition.decode_transposition(text, key)
    translate_time = round(time.time() - start_translate_time, 2)
    print('Translated in ', translate_time, ' seconds')

    start_write_time = time.time()
    with open(output_filename, mode='w', encoding='utf-8') as output_file:
        output_file.write(translated)
    write_time = round(time.time() - start_write_time, 2)
    total_time = translate_time + write_time
    print('Translated/wrote ', len(text), ' chars in ', total_time, ' seconds')

if __name__ == '__main__':
    main()
