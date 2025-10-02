import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# ==============================
# CONFIG
# ==============================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "stembyrysera@gmail.com"
SENDER_PASSWORD = "hpdk wcvq wfmt pnsk"  # Use App Password, not your real password

SUBJECT_TEMPLATE = "🎓 Congratulations, {Name}! Here’s Your AI Course Participation E-Certificate – RYSERA STEM"
BODY_TEMPLATE = """Dear {Name},

Congratulations! 🎉

You have successfully completed the AI Innovation Course conducted by RYSERA STEM.
As a token of recognition for your dedication and effort, we are pleased to present your Course Completion E-Certificate.

📎 Attached: Your official e-certificate (PDF)

Best regards,
Rysera Stem
"""

# ==============================
# LOAD STUDENT DATA
# ==============================
df = pd.read_excel("Student completion list.xlsx")  # or pd.read_csv("students.csv")

# ==============================
# SEND EMAILS
# ==============================
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

for _, row in df.iterrows():
    name = row["Name"]
    email = row["Email"]
    cert_file = row["Certificate_File"]

    # Create email
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = email
    msg["Subject"] = SUBJECT_TEMPLATE.format(Name=name)

    # Add body
    body = BODY_TEMPLATE.format(Name=name)
    msg.attach(MIMEText(body, "plain"))

    # Attach certificate
    with open(cert_file, "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header("Content-Disposition", "attachment", filename=cert_file.split("/")[-1])
        msg.attach(attach)

    # Send
    server.send_message(msg)
    print(f"✅ Sent to {name} ({email})")

server.quit()
print("🎉 All certificates sent successfully!")
