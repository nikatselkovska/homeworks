# I understand this task might be performed with using lists, but dictionary is more right to use in this case

#we put "complicated" designations ahead for handling them first and avoiding errors
text_emoji_dict = {'>:)': '😈', '>:(': '😠', ':)': '🙂', 'XD': '😂', ':(': '🙁'}

user_input = input('Please enter some sentence using text emoji symbols: ')

for text_emoji_key in text_emoji_dict:
    index_key = user_input.find(text_emoji_key)
    if index_key != -1:
        user_input = user_input.replace(text_emoji_key, text_emoji_dict[text_emoji_key])

print(user_input)