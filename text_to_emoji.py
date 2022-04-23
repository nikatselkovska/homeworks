# I understand this task might be performed with using lists, but dictionary is more right to use in this case

#we put "complicated" designations ahead for handling it first and avoiding errors
text_emoji_dict = {'>:)': '😈', '>:(': '😠', ':)': '🙂', 'XD': '😂', ':(': '🙁'}

user_input = input('Please enter some sentence using text emoji symbols: ')

for text_emoji, icon_emoji in text_emoji_dict.items():
    user_input = user_input.replace(text_emoji, icon_emoji)

print(user_input)