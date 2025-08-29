#step-1 install twilio
from twilio.rest import Client
from datetime import datetime, timedelta
import time

#step-2 twilio credentials
account_sid='ACb620c6ec2a010d6f6d3fd3992505fce9'
auth_token = '66c5f266efab7347d74d3b99b4c31893'

client = Client(account_sid, auth_token)

#step-3 degine send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')

#step-4 user input
name = input('enter the name=')
recipient_number =input('enter the recipient whatsapp number with country code (e.g, +123)')
message_body = input(f'enter the message you want to sent to {name}: ')

#step-5 parse date\time and calculate delay
date_str = input('enter the date to sent the message (YYYY-MM-DD): ')#2024-06-12
time_str = input('enter the time to sent the message (HH:MM in 24hour format): ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime =datetime.now()

#calculate delay
time_difference =schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print('the specified time is in the past. please enter a future date and time:')
else:
    print(f'message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait until the schedule time
    time.sleep(delay_seconds)

    #send the message
    send_whatsapp_message(recipient_number, message_body)