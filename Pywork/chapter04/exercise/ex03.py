# [문제3] list 내포를 이용하여 문자열 처리하기

message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = [int('spam' == s) for s in message]
print(dummy)

spam_list = [s for s in message if s == 'spam']
print(spam_list)
