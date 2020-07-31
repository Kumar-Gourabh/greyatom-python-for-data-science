# --------------
#Step 1: The first thing you have to do is to write a function that reads the contents of the files that we have

def read_file(path):
    file = open(path,'r')
    sentence=file.readline()
    file.close()
    return(sentence)

sample_message = read_file(file_path)
print(sample_message)

#Step 2: In this task, you have to make use of messages of two different files. In the two files, we have one number each. You have to apply a certain operation to extract our message.

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)
def fuse_msg(message_a,message_b):
    quotient = str(int(message_b)//int(message_a))
    return(quotient)
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)

#Step 3: In this task, you have to substitute the message of the file for a secret message.

message_3 = read_file(file_path_3)
print(message_3)
def substitute_msg(message_c):
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Marine Biologist'
    return(sub)
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)

#Step 4: In this task, you have to make use of messages from two different files. You have to compare the two messages and take only those words that appear in first message but not in second message.

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)
def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list=[]
    for i in a_list:
        if i not in b_list:
            c_list.append(i)
    final_msg = " ".join(c_list)
    return(final_msg)
secret_msg_3 = compare_msg(message_4,message_5)
print (secret_msg_3)

#Step 5: In this task, you have to extract only those words from the message in the file that are of even length.

message_6=read_file(file_path_6)
print(message_6)
def extract_msg(message_f):
    a_list=message_f.split()
    even_word = lambda x: len(x)%2==0
    b_list=filter(even_word,a_list)
    final_msg=" ".join(b_list)
    return(final_msg)
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

#Step 6: Congrats lieutenant, you have successfully deciphered all the message bits that we received. In this final task, we will combine all the message bits into a single message and write it in a file.

message_parts = [secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
print(message_parts)
secret_msg = " ".join(message_parts)
final_path= user_data_dir + '/secret_message.txt'
def write_file(secret_msg,path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close()
write_file(secret_msg,final_path)
print(secret_msg)


