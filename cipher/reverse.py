def reverse_loop(message):
    encoded = ''
    for i in range(len(message) - 1, -1, -1):
        encoded += message[i]
    return encoded


def reverse_func(message):
    encoded = ''
    for c in reversed(message):
        encoded += c
    return encoded


def reverse_slice(message):
    encoded = message[::-1]
    return encoded

message = 'Three can keep a secret, if two of them are dead.'
print(reverse_loop(message))
print(reverse_func(message))
print(reverse_slice(message))
