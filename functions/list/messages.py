def show_messages(messages):
    for message in messages:
        print(message)

messages = ['hello', 'hi', 'good day', 'how are you?']
# show_messages(messages)

def send_messages(messages):
    sent_messages = []
    while messages:
        sent = messages.pop()
        print(f'sending {sent} ...')
        sent_messages.append(sent)
    for message in sent_messages:
        print(f'{message} sent')
'''
send_messages(messages)
print(messages)
'''
send_messages(messages[:])
print(messages)
