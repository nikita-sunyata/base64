'''編碼功能
1. 將用戶輸入的 decode 為數字 (依照一般編碼)
2. 將該數字轉換為二進位碼
3. 檢查該二進位字串是否剛好能被3整除，如果不行，則要補1-2個0，並且記錄補了多少0，就要在最後的base64信息上的最後加上幾個 " = "
4. 建立一個 0-64的字母資料庫，讓所有base64字元能夠對應(用字典)
5. 開始將二進位資料用6個一組的方式進行編碼
6. 最後如果有要補 = 的話，要記得補 = 
'''

# ASCII 轉 base64

def base64_encode(user_input:str):
    #進度1
    binary_message = ""
    add_equal_sign_count = ( 6-(len(user_input)*8)%6 )//2 #進度3
    #print(add_equal_sign_count)
    for word in user_input:
        user_input_ascii = ord(word)
        #進度2
        user_input_binary = "{:>08}".format(bin(user_input_ascii)[2:])
        #print(user_input_ascii)
        #print(user_input_binary)
        binary_message+=user_input_binary
    #print(binary_message)
    binary_message += "{}".format("0"*add_equal_sign_count) #進度3


    #進度4
    base64_words = dict()
    dict_title_number = 0
    for ascii_word_number_set1 in range(65,91):
        base64_words[dict_title_number]=chr(ascii_word_number_set1)
        dict_title_number+=1
    for ascii_word_number_set2 in range(97,123):
        base64_words[dict_title_number]=chr(ascii_word_number_set2)
        dict_title_number+=1
    for ascii_word_number_set3 in range(0,10):
        base64_words[dict_title_number]="{}".format(ascii_word_number_set3)
        dict_title_number+=1
    base64_words[62]='+'
    base64_words[63]='/'

    #進度5
    final_message = ''
    a_6_number_word=''
    a_6_number_count=0
    for w in binary_message:
        a_6_number_word += w
        a_6_number_count += 1
        if a_6_number_count == 6:
            final_message += base64_words[int(a_6_number_word,2)]
            a_6_number_word = ''
            a_6_number_count = 0
    #當跑完之後還有多餘的字母時要保留剩下的字母並加0到滿六位數
    if len(a_6_number_word) > 0:
        a_6_number_word+="0"*(6-len(a_6_number_word))
        final_message += base64_words[int(a_6_number_word,2)]
        #a_6_number_word = ''
        #a_6_number_count = 0
    
    #進度6
    final_message += "{}".format("="*add_equal_sign_count)
    print(final_message)    


#base64_encode("Hello World")

# #UTF-8 萬用編碼

# def base64_encode_from_utf8(user_input:str):
#     #進度1
#     binary_message = ""
#     #add_equal_sign_count = ( 6-(len(user_input)*8)%6 )//2 #進度3
#     #print(add_equal_sign_count)

#     binary_len_count = 0#進度3
#     for word in user_input:
#         user_input_ascii = ord(word)
#         #進度2
#         #user_input_binary = "/+{}{}".format("0"*(8-len(bin(user_input_ascii)[2:])),bin(user_input_ascii)[2:])
#         user_input_binary = "/{}{}".format("0"*(8-(len((bin(user_input_ascii)[2:]))%8)),bin(user_input_ascii)[2:])
#         #print(user_input_ascii)
#         #print(user_input_binary)
#         binary_message+=user_input_binary
#         binary_len_count += len(user_input_binary)-1
#     add_equal_sign_count = (6 - (binary_len_count%6)) // 2
#     #print(binary_message)
#     #binary_message += "{}".format("0"*add_equal_sign_count) #進度3


#     #進度4
#     base64_words = dict()
#     dict_title_number = 0
#     for ascii_word_number_set1 in range(65,91):
#         base64_words[dict_title_number]=chr(ascii_word_number_set1)
#         dict_title_number+=1
#     for ascii_word_number_set2 in range(97,123):
#         base64_words[dict_title_number]=chr(ascii_word_number_set2)
#         dict_title_number+=1
#     for ascii_word_number_set3 in range(0,10):
#         base64_words[dict_title_number]="{}".format(ascii_word_number_set3)
#         dict_title_number+=1
#     base64_words[62]='+'
#     base64_words[63]='/'

#     #進度5
#     final_message = ''
#     binary_message_list = binary_message.split('/')
#     for w in binary_message_list:
#         final_message += "{}".format(base64_words[int(w,2)])
#         print(w)

#     #final_message += "{}".format('='*add_equal_sign_count)

#     print(final_message)



    # final_message = ''
    # a_6_number_word=''
    # a_6_number_count=0
    # for w in binary_message:
    #     a_6_number_word += w
    #     a_6_number_count += 1
    #     if a_6_number_count == 6:
    #         final_message += base64_words[int(a_6_number_word,2)]
    #         a_6_number_word = ''
    #         a_6_number_count = 0
    # #當跑完之後還有多餘的字母時要保留剩下的字母並加0到滿六位數
    # if len(a_6_number_word) > 0:
    #     a_6_number_word+="0"*(6-len(a_6_number_word))
    #     final_message += base64_words[int(a_6_number_word,2)]
    #     #a_6_number_word = ''
    #     #a_6_number_count = 0
    
    # #進度6
    # final_message += "{}".format("="*add_equal_sign_count)
    # print(final_message)   

# print(base64_encode_from_utf8('hello world'))
#print(bin(ord("好")))