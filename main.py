# Developer : Pouria Hosseini | Channel: @OmgaDeveloper | Telegram ID: @isPoori #
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, PhoneCodeEmpty, SessionPasswordNeeded
from pyrogram.types import User

# Getting user inputs
api_id = input("Enter your API ID: ")
api_hash = input("Enter your API HASH: ")
phone_number = input("Enter your phone number (with country code, e.g. +98xxx): ")

# Admin and reporter information
admin_user_id = 00000000  # Admin user ID
report_username = '@ispoori'  # Reporter username

# Creating the Telegram client
client = Client("Pouria.session", api_id=api_id, api_hash=api_hash)

# Function to get unique time in the form of special characters
def get_unique_time():
    current_time = time.strftime('%H:%M')
    fonts = ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟖", "𝟖", "𝟗"]
    return ''.join([fonts[int(c)] for c in current_time.replace(":", "")])

# Function to update the profile name with time
async def update_profile():
    time2 = get_unique_time()

    # Get user's profile information
    me = await client.get_me()
    current_first_name = me.first_name

    # New profile name with time
    new_first_name = f"{current_first_name} ({time2})"

    # Update the profile with the new name
    await client.update_profile(first_name=new_first_name)

    # Send message to reporter ensuring UTF-8 encoding
    try:
        await client.send_message(report_username, f"Profile updated with time: {time2}".encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

# New message handler
async def handler(client, message):
    if message.from_user.id == admin_user_id:
        if message.text.lower() in ['ping', '#ping', '/ping', '!ping', '.ping','bot', 'omga', 'Ping']:
            await message.reply('Pong !')

# Function to sign in to Telegram and get the code
async def sign_in():
    try:
        await client.start()
    except PhoneCodeEmpty:
        code = input(f"Enter the code sent to {phone_number}: ")
        await client.sign_in(phone_number, code.encode('utf-8'))  # Convert to UTF-8
    except SessionPasswordNeeded:
        password = input("Enter your 2FA password: ")
        await client.check_password(password.encode('utf-8'))  # Convert to UTF-8

# Error management and retrying in case of failure
async def handle_errors():
    while True:
        try:
            # First, sign in to the account
            await sign_in()
            # Then, update profile and start the bot
            while True:
                await update_profile()
                await asyncio.sleep(60)  # Profile updates every 60 seconds
        except FloodWait as e:
            print(f"Rate limit exceeded. Retrying in {e.x} seconds...")
            await asyncio.sleep(e.x)  # Wait if rate limit exceeded
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(10)  # Retry after 10 seconds if any error occurs

# Adding handler to the client
client.add_handler(filters.text, handler)

# Starting the bot
async def main():
    await handle_errors()

# Starting the client and running the bot
if __name__ == "__main__":
    asyncio.run(main())
