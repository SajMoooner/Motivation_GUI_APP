import Twilio
import tkinter


#wdokyrgfyklguqnv

account_sid = 'TWILIO_SSID'
auth_token = 'TWILIO_TOKEN'
from_number = 'TWILIO_NUMBER'

send_object = Twilio.Twilio(account_sid, auth_token, from_number)
motivation = Twilio.Motivation()
send_mail = Twilio.SendToEmail('MAIL_TO', 'PASSWORD_TO_EMAIL')
send_sp = Twilio.CreateSharePointItem('SP_ACCOUNT', 'SP_HESLO')


window =  tkinter.Tk()
window.title("Motivational Quotes")

#open app in full screen
window.attributes('-fullscreen', False)

# create a label to display the quote pretty
label = tkinter.Label(window, text=motivation.get_random_quote(), font=("Arial", 20), wraplength=800)
# change dynamically the height of the label to fit the text inside
label.grid(row=0, column=0, columnspan=3, sticky="nsew")
label.pack(pady=20)

list_of_qoutes = motivation.get_all_quotes()
actual_quote = 0


def next_quote():
    global actual_quote
    actual_quote += 1
    label.config(text=list_of_qoutes[actual_quote].text.rstrip())

def previous_quote():
    global actual_quote
    actual_quote -= 1
    label.config(text=list_of_qoutes[actual_quote].text.rstrip())

def send_quote():
    send_object.send_sms('SEND_TO', list_of_qoutes[actual_quote].text.rstrip())
    label.config(text="Quote sent to your phone!")

def send_quote_email():
    send_mail.send_email('SEND_TO_MAIL', list_of_qoutes[actual_quote].text.rstrip())
    label.config(text="Quote sent to your email!")

def send_quote_sharepoint():
    send_sp.create_item('SP_TENANT', list_of_qoutes[actual_quote].text.rstrip())
    label.config(text="Quote sent to SharePoint!")

#make buttons pretty

# create a button to show the next quote
next_button = tkinter.Button(window, text="Next Quote", command=next_quote, bg="green", fg="white", font=("Arial", 20), width=20)
next_button.pack(pady=20)

# create a button to show the previous quote
previous_button = tkinter.Button(window, text="Previous Quote", command=previous_quote, bg="green", fg="white",font=("Arial", 20), width=20)
previous_button.pack(pady=20)

# create a button to send the quote to your phone
send_button = tkinter.Button(window, text="Send Quote SMS", command=send_quote, bg="green", fg="white",font=("Arial", 20), width=20)
send_button.pack(pady=20)

# create a button to send the quote to your email
send_email_button = tkinter.Button(window, text="Send Quote Email", command=send_quote_email, bg="green", fg="white",font=("Arial", 20), width=20)
send_email_button.pack(pady=20)

# create a button to send the quote to your sharepoint
send_sharepoint_button = tkinter.Button(window, text="Send Quote to SharePoint", command=send_quote_sharepoint, bg="green", fg="white",font=("Arial", 20), width=20)
send_sharepoint_button.pack(pady=20)

window.mainloop()