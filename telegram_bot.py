import requests
import time
import asyncio
from telegram.ext import ApplicationBuilder
from telegram.error import TimedOut, NetworkError
from datetime import datetime, timedelta

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'

# Replace 'YOUR_TELEGRAM_BOT_USERNAME' with your actual bot username
bot_username = 'YOUR_TELEGRAM_BOT_USERNAME'

# Replace 'YOUR_TELEGRAM_CHAT_ID' with your actual Telegram chat ID
chat_id = 'YOUR_TELEGRAM_CHAT_ID'

# Get the mempool threshold from the user
threshold = float(input("Enter the mempool threshold (in sats/vbyte): "))

# Variable to store the timestamp of the last notification
last_notification_time = None

async def get_bitcoin_fees():
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        hourFee = data['hourFee']
        return hourFee
    else:
        print("Failed to fetch Bitcoin fees from mempool.space")
        return None

async def send_telegram_alert(fee):
    global last_notification_time
    
    current_time = datetime.now()
    
    if last_notification_time is None or (current_time - last_notification_time) >= timedelta(hours=6):
        message = f"Alert: The 1-hour Bitcoin fee is now {fee} sats/vbyte, which is below the threshold of {threshold} sats/vbyte."
        bot = ApplicationBuilder().token(bot_token).build()
        
        max_retries = 3
        retry_delay = 5
        
        for attempt in range(max_retries):
            try:
                await bot.bot.send_message(chat_id=chat_id, text=message)
                print(f"Alert sent successfully. Attempt: {attempt + 1}")
                last_notification_time = current_time
                break
            except (TimedOut, NetworkError) as e:
                print(f"Error sending alert: {str(e)}. Attempt: {attempt + 1}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    await asyncio.sleep(retry_delay)
                else:
                    print("Max retries reached. Alert not sent.")
    else:
        print(f"Skipping notification. Last notification sent: {last_notification_time}")

async def monitor_bitcoin_fees():
    while True:
        hourFee = await get_bitcoin_fees()
        if hourFee is not None:
            print(f"Current 1-hour Bitcoin fee: {hourFee} sats/vbyte")
            
            if hourFee < threshold:
                await send_telegram_alert(hourFee)
        
        await asyncio.sleep(600)  # Wait for 600 seconds(10mins) before checking again

# Run the program
asyncio.run(monitor_bitcoin_fees())
