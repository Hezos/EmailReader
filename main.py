from imap_tools import MailBox, AND
import imaplib


with MailBox('imap.gmail.com').login("nbence0620@gmail.com", "********") as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject)

