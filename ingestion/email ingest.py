import imaplib
import email

class EmailIngest:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def fetch_latest(self):
        mail = imaplib.IMAP4_SSL(self.host)
        mail.login(self.username, self.password)
        mail.select("inbox")

        _, data = mail.search(None, "ALL")
        mail_ids = data[0].split()

        latest_id = mail_ids[-1]
        _, msg_data = mail.fetch(latest_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        return {
            "subject": msg["subject"],
            "from": msg["from"],
            "body": self._get_body(msg)
        }

    def _get_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode()
        return msg.get_payload(decode=True).decode()