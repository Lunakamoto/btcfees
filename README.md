Bitcoin Fee Alert Bot
This Python script monitors the 1-hour Bitcoin fee using the Mempool API and sends a Telegram notification when the fee drops below a specified threshold defined by the user. The bot avoids sending duplicate notifications within a 6-hour interval.

Prerequisites
Before using this script, make sure you have the following:

Python 3.x installed on your system
A Telegram bot created using BotFather
The required Python packages installed (requests, python-telegram-bot)
Setup
Create a new Telegram bot using BotFather:

Start a chat with BotFather on Telegram.
Send the /newbot command and follow the prompts to set a name and username for your bot.
Take note of the API token provided by BotFather.
Obtain your Telegram chat ID:

Start a chat with your newly created bot on Telegram.
Send a message to the bot.
Visit the following URL in your web browser, replacing <YOUR_BOT_TOKEN> with your actual bot token:


    https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
Look for the chat_id field in the response and take note of its value.
Clone the repository or download the script file.

Open the script file in a text editor.

Replace the following placeholders in the script with your actual values:

'YOUR_TELEGRAM_BOT_TOKEN': Replace with your Telegram bot token obtained from BotFather.
'YOUR_TELEGRAM_BOT_USERNAME': Replace with your Telegram bot username (without the @ symbol).
'YOUR_TELEGRAM_CHAT_ID': Replace with your Telegram chat ID obtained in step 2.
Save the modified script file.

Usage
Open a terminal or command prompt.

Navigate to the directory where the script file is located.

Run the following command to install the required packages:

    pip3 install requests python-telegram-bot
    Run the script using the following command:



    python script_name.py
    Replace script_name.py with the actual name of your script file.

The script will start monitoring the 1-hour Bitcoin fee every 600 seconds(10 minutes) and print the current fee in the console.

If the fee drops below the specified threshold(set by the user), the bot will notify your Telegram chat.

The bot will avoid sending duplicate notifications within a 6-hour interval.

Press Ctrl + C in the terminal or command prompt to stop the script.

Customization
You can customize the script according to your needs:

Adjust the fee threshold by modifying the condition if hourFee < threshold in the monitor_bitcoin_fees() function.
Change the notification interval by modifying the condition.


    (current_time - last_notification_time) >= timedelta(hours=6)
in the send_telegram_alert() function.
Modify the notification message by updating the message variable in the send_telegram_alert() function.
Troubleshooting
If you encounter any issues while running the script, consider the following:

Make sure you have installed the required packages (requests, python-telegram-bot).
Double-check that you have correctly replaced the placeholders with your actual bot token, bot username, and chat ID.
Ensure your bot has permission to send messages in the specified chat.
If you encounter any errors, check the console output for error messages and refer to the documentation of the respective packages for troubleshooting.

License
This script is open-source and available under the MIT License.

Feel free to modify and distribute the script as you need.

