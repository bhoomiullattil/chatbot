from chatterbot import ChatBot

bot = ChatBot('Buddy',
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )


# run and get response from user.
#name = input('Enter Your Name: ')

print ('Welcome to Chatbot Service! Let me know how can I help you')

while True:

    request = input()

    if request=="Bye" or request=='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print(response)