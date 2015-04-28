

def encode_caesar(text, key):
    """Encode string using Caesar shift cipher. Use negative key to decode."""
    encoded = []
    for c in text:
        # Shift each character by the key
        char_value = ord(c) + key
        # Wrap down when character goes beyond ~ to avoid printing issues
        while char_value > ord('~'):
            # Returns the minimum value ( ) plus the amount 'above' the max
            char_value = (char_value % ord('~')) + ord(' ')
        # Wrap up when character goes below ' ' to avoid printing issues
        while char_value < ord(' '):
            # Returns the maximum value (~) minus the amount 'below' the min
            char_value = ord('~') - (ord(' ') - char_value)
        encoded_char = chr(char_value)
        encoded.append(encoded_char)
    # Compile string from each encoded char
    return ''.join(encoded)

to_encode = input('Enter some text: ').strip()
key = int(input('Enter your caesar shift key: '))
print('Encoded: ')
encoded = encode_caesar(to_encode, key)
print(encoded)
print('Decoded: ')
# 'Encode' the decoded string using additive inverse or encoding key to decode
print(encode_caesar(encoded, 0 - key))
