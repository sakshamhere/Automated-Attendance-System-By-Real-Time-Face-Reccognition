import smtplib


def send_mail_student(sender,reciever,mail_body,mail_subject):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
    server.starttls() #encrypts are connection
    server.ehlo()

    server.login('sam9111doshi@gmail.com','9111204454')

    subject = mail_subject
    body = mail_body

    msg = f"Subject: {subject}\n\n{body}" #new f-string way to format in python like we use ``  and ${} in js
    
    server.sendmail(
        sender, #from
        reciever, #to
        msg
    )
    print('mail sent!')
    server.quit()

def send_mail(line):
    print(line)
    sender = line[3]
    reciever = line[4]
    mail_body = 'Your Attendance has been marked, current attendance 74%'
    mail_subject = 'Attendance notification'
    send_mail_student(sender,reciever,mail_body,mail_subject)