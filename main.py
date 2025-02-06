from imap_tools import MailBox, AND
import imaplib
import email

imap = imaplib.IMAP4_SSL('imap.gmail.com')

username = 'nbence0620@gmail.com'
password = "messenger self"
imap.login(username, password)

for i in imap.list()[1]:
    l = i.decode().split(' "/" ')
    print(l[0] + " = " + l[1])

imap.select('"INBOX"')
status, messages = imap.search(None, 'UNSEEN')

for num in messages[0].split()[::-1]:
    _, msg = imap.fetch(num, "(RFC822)")
    message = email.message_from_bytes(msg[0][1])

    # print the message details
    subject_header = message['Subject']
    decoded_subject = email.header.decode_header(subject_header)
    subject = decoded_subject[0][0]
    print("Subject:", subject)
    print("From:", message["From"])
    print("Date:", message["Date"])