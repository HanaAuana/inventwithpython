import math


def encode_transposition(text, key):
    """Encode string using transposition cipher. """

    # Find the number of rows we'll need, based on text and key length
    num_rows = len(text) // key
    if len(text) % key != 0:
        num_rows += 1

    encoded_rows = [[] for l in range(num_rows)]
    pointer = 0
    for row in encoded_rows:
        in_row = True
        # We'll add each character to the row
        while in_row and pointer < len(text):
            row.append(text[pointer])
            pointer += 1
            # Until we reach the row length, determined by our key
            if pointer != 0 and pointer % key == 0:
                in_row = False
        # To ensure uniform length, pad with None
        while len(row) < key:
            row.append(None)

    encoded = []
    for i in range(key):
        # Turn the "rows" into column format, for easier joining
        col = [row[i] for row in encoded_rows if row[i] is not None]
        encoded.append(''.join(col))
    return ''.join(encoded)


def decode_transposition(text, key):
    num_cols = math.ceil(len(text) / key)
    num_rows = key
    # Record the cells we won't need in the "table"
    num_unused = (num_cols * num_rows) - len(text)

    decoded_cols = [[] for r in range(num_cols)]
    col = 0
    row = 0
    for c in text:
        decoded_cols[col].append(c)
        col += 1

        last_col = col == num_cols
        in_unused = (col == (num_cols - 1) and row >= num_rows - num_unused)
        # If we reach the last column, or if we're in an unused cell
        if last_col or in_unused:
            # Move to the next row
            col = 0
            row += 1

    decoded = [''.join(c) for c in decoded_cols]
    return ''.join(decoded)


# to_encode = input('Enter some text: ').strip()
# key = int(input('Enter your caesar shift key: '))
to_encode = "Common sense is not so common."
key = 8
encoded = encode_transposition(to_encode, key)
print('Encoded: ')
print(encoded)
print('Decoded: ')
# 'Encode' the decoded string using additive inverse or encoding key to decode
print(decode_transposition(encoded, key))


def encode_transposition_comp(text, key):
    """Alternate version of transpo cipher using a list comprehension."""
    encoded = []
    for n in range(key):
        # Columns are the characters divisible at each step in key range
        col = [c for i, c in enumerate(text) if i % key == n]
        # Now, recombine each column, per the cipher
        encoded.append(''.join(col))
    # Then join each column back into a single string
    return(''.join(encoded))

# print(encode_transposition_comp(to_encode, key))
