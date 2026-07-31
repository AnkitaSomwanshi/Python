import smtplib
from email.message import EmailMessage
import sys

def Send_Email(sender,password,receiver,subject,body):
    try:

        msg = EmailMessage()

        msg["From"] = sender

        msg["To"] = receiver

        msg["subject"] = subject

        msg.set_content(body)

        #with smtp = smtplib.SMTP_SSL("smcom",465)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception as e:
        print("Error:", e)


    #smtp.quit()
    

def main():

    
    Sender_Email = "ankitasumitaher@gmail.com"
    
    Sender_password = "jqkrsivjeizetzih" #Ankitasomwanshi1999"
    
    Receiver_Email = "anitasomwanshi1999@gmail.com"
    
    Subject = "TestFromPython"
    
    Body = """Hi Ankita,
    
    This Mail is for testing purpose.
    
    Thanks & Regards,
    Ankita Patil """


    Send_Email(Sender_Email,Sender_password,Receiver_Email,Subject,Body)

    print("Mail sent Sucessfully")


if __name__ == "__main__":
    main()

