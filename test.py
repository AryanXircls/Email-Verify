import smtplib
import dns.resolver

def is_valid_email(email):
    # Split the email address into local part and domain
    local_part, domain = email.split('@')

    try:
        # Get MX records for the domain
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange.to_text()

        # Connect to the email server
        with smtplib.SMTP() as server:
            server.set_debuglevel(0)
            server.connect(mx_record)
            server.helo(server.local_hostname)
            server.mail('')
            code, _ = server.rcpt(str(email))
            return code == 250

    except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected,
            dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

# Example usage
email = 'crce.9594.ce@gmail.com'
if is_valid_email(email):
    print("Email exists")
else:
    print("Email does not exist")
