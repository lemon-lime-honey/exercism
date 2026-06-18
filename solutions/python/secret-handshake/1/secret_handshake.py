handshake = {0b0001: 'wink', 0b0010: 'double blink', 
             0b0100: 'close your eyes', 0b1000: 'jump'}

def commands(binary_str):
    command = []
    number = int(binary_str, 2)
    for value, key in handshake.items():
        if value & number:
            command.append(key)
    if number & 16:
        command = command[::-1]
    return command
