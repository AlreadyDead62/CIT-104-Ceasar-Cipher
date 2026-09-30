"""
  Kitsmiller, Jericho
        
  Purpose: Encrypt  / decrypt a text file using a modified Caesar cipher based
  on user input for number distance. 
    """
# Read file contents
file_path = r"C:\Users\jeric\Downloads\CIT-140-A.26.U-Sept. 30-Ceasar Cipher Text.txt"
with open(file_path, 'r', encoding='utf-8') as inputFile:
    data = inputFile.read()

print(data)
print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    user_message = input("Enter message to encrypt (leave blank to use file contents): ")
    try:
        distance = int(input("Enter the distance value:"))
    except ValueError:
        print("Distance must be an integer.")
        raise

    # use user message if provided, otherwise use file contents
    source = user_message if user_message.strip() else data
    code = ""

    # If you want to encrypt file contents, iterate over `source`.
    for ch in source:
        if 'a' <= ch <= 'z':
            ordvalue = ord(ch)
            cipherValue = ordvalue + distance

            # wrap-around for lowercase letters
            if cipherValue > ord('z'):
                cipherValue = ord('a') + (cipherValue - ord('z') - 1)

            code += chr(cipherValue)
        else:
            # leave non-lowercase characters unchanged
            code += ch

    print(code)

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    user_message = input("Enter the encrypted message (leave blank to use file contents): ")
    try:
        distance = int(input("Enter the distance value:"))
    except ValueError:
        print("Distance must be an integer.")
        raise

    source = user_message if user_message.strip() else data
    code = ""

    # data instead of plaintext to match the read file command above
    for ch in source:
        if 'a' <= ch <= 'z':
            ordvalue = ord(ch)
            cipherValue = ordvalue - distance
            if cipherValue < ord('a'):
                # wrap-around for lowercase letters when decrypting
                cipherValue = ord('z') - (ord('a') - cipherValue - 1)
            code += chr(cipherValue)
        else:
            # leave non-lowercase characters unchanged
            code += ch

    print(code)

else:
    print("Invalid selection. Please enter 'e' or 'd'.")
    raise SystemExit(1)

# To write on the file (overwrite with result)
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)
