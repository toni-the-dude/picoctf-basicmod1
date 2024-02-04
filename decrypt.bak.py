message_obj =  open("message.txt", "r")
    
message_text = message_obj.read()

# print(message_text)

message_text = message_text.split(" ")

# print(message_text)

while message_text[-1] == '':
    message_text.pop()

# print(message_text)

decrypted_message_str = ""

for number in message_text:
    # print(int(number))
    mod37 = int(number) % 37
    # print(mod37)
    # print(str(chr(mod37 + 65)))
    # print(str(mod37 - 26))
    # input()
    if mod37 <= 25: decrypted_message_str += str(chr(mod37 + 65))
    elif mod37 <= 35: decrypted_message_str += str(mod37 - 26)
    elif mod37 == 36: decrypted_message_str += "_"
    else: print("Something is wrong.")

print("picoCTF{" + decrypted_message_str + "}")