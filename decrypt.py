message_obj =  open("message.txt", "r")
message_text = message_obj.read()
message_text = message_text.split(" ")

while message_text[-1] == '':
    message_text.pop()

decrypted_message_str = ""

for number in message_text:
    mod37 = int(number) % 37
    if mod37 <= 25: decrypted_message_str += str(chr(mod37 + 65))
    elif mod37 <= 35: decrypted_message_str += str(mod37 - 26)
    elif mod37 == 36: decrypted_message_str += "_"
    else: print("Something is wrong.")

print("picoCTF{" + decrypted_message_str + "}")