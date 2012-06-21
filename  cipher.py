phrase = raw_input('Enter sentence to encrypt: ')
shift = input('Enter shift value: ')
encoded_phrase = ''

for c in phrase:
    
            if c >= 'A' and c <= 'Z':
                ascii_code = ord(c) - ord('A')
                ascii_code = (ascii_code + shift) % 26
                ascii_code = ascii_code + ord('A')
                encoded_phrase = encoded_phrase + chr(ascii_code)
            elif c >= 'a' and c <= 'z':
                ascii_code = ord(c) - ord('a')
                ascii_code = (ascii_code + shift) % 26
                ascii_code = ascii_code + ord('a')
                encoded_phrase = encoded_phrase + chr(ascii_code)
            else:
                encoded_phrase = encoded_phrase + c
print 'The encoded phrase is: ', encoded_phrase
