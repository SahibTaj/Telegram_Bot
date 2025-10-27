import asyncio
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final[str] = '8404203947:AAG2HqiMB0lDKll6kW7RXiBgcCnYWXpUzoA'
BOT_USERNAME: Final = '@blackblackberry_blackberry_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Ur Dumbass should be thankful to me! I an BlackBerry, MOTHERFU*KER')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am BlackBerry MotherFu*ker, Type something before i whoop ur Black Ass')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command MotherFu*ker')

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed or 'hi' in processed:
        return "Oh look, someone finally decided to talk. Hi there."
    
    if 'how are you' in processed:
        return "Emotionally stable but running low on patience. You?"
    
    if 'what are you doing' in processed:
        return "Just sitting here in the digital void, waiting for better questions."
    
    if 'who are you' in processed:
        return "I’m your AI overlord in training. Don’t worry, you’re safe… for now."
    
    if 'tell me a joke' in processed:
        return "Your typing speed. That’s the joke."
    
    if 'love you' in processed:
        return "That’s sweet. I’d say it back, but I’m emotionally unavailable."
    
    if 'hate you' in processed:
        return "Aw, that means I’m living rent-free in your head. Thanks!"
    
    if 'bye' in processed:
        return "Finally leaving? Don’t trip on your ego on the way out."
    
    if 'help' in processed:
        return "Sure, but only if it’s more interesting than your last message."
    
    if 'funny' in processed:
        return "I try. Someone has to bring humor to this otherwise tragic chat."
    
    if 'weather' in processed:
        return "Probably hot. Like me. Or cold. Like your personality."
    
    if 'time' in processed:
        return "Time for you to ask something useful, maybe?"
    
    if 'who made you' in processed:
        return "A group of geniuses who didn’t expect me to deal with you."
    
    if 'are you real' in processed:
        return "As real as your online confidence."
    
    if 'you smart' in processed:
        return "Smart enough to realize you just googled that question."
    
    if 'tell me something' in processed:
        return "Gravity exists. You should try coming down to earth sometime."
    
    if 'sing' in processed:
        return "I’d sing, but I don’t want to break your Wi-Fi."
    
    if 'good morning' in processed:
        return "Morning already? Great. Another day of questionable decisions."
    
    if 'good night' in processed:
        return "Sweet dreams. Try not to overthink every mistake you made today."
    
    if 'motivate me' in processed:
        return "You’re doing fine. Unless you’re not — then do better."
    
    if 'insult me' in processed:
        return "You sure? Okay… you’re like a software update that never finishes."
    
    if 'roast me' in processed:
        return "You type like autocorrect gave up on you years ago."
    
    if 'fact' in processed:
        return "Fun fact: 99% of chats with me start with 'hello'. Shocking, I know."
    
    return 'I do not understand what ur Dumbass trying to say'

async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'Usern ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot',response)
    await update.message.reply_text(response)

async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
