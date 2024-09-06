unencrypted_message = input()
encrypted_message = ''
for character in unencrypted_message:
    encrypted_chr = chr(ord(character) + 3)
    encrypted_message += encrypted_chr
print(encrypted_message)

