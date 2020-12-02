# -*- coding: utf-8 -*-
"""Telegramm_bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lbxehgZKE3nLH41pH6VCHMr6bsqwRLKu
"""

pip install python-telegram-bot

import telegram

TOKEN = '1453823463:AAGCNd1mLb4aXdc94A_8pP6-qDfbtawuu7g'

bot = telegram.Bot(TOKEN)
print(bot.get_me())

bot = telegram.Bot(TOKEN)

updates = bot.get_updates()  # this line needs to be run everytime u fetch/chat any content
# prints all the text sent to the bot
print([u.message.text for u in updates])
print("\nMessage length is", len(updates))

context = [u.message.text for u in updates]

seed_text = context[-1]

for _ in range(10):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_length - 1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

bot = telegram.Bot(TOKEN)

chat_id = bot.get_updates()[-1].message.chat_id
#Bot's reply text'
txt = seed_text

# send message
bot.send_message(chat_id, txt)

