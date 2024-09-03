import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror

# Email configuration
SMTP_SERVER = 'smtp.mail.com'  # Replace with your SMTP server. Gmail(stmp.gmail.com), yahoomail(smtp.mail.yahoomail.com)
SMTP_PORT = 587                   # Common port for 587 TLS, 465 SSL
USERNAME = 'recipient@example.com'  # Replace with your email address
PASSWORD = 'password'  # Replace with your email password. for gmail users, generate app  password and ensure to turn on 2-step verification.

# Email content
def create_email_content():
    subject = 'Daily Report'
    body = 'This is your daily report. \nHey there, future Flask developer! \nEmbarking on the journey to become a web developer is like setting out on an exciting adventure. Flask is your compass, and every line of code you write is a step toward creating something amazing. \nRemember, every great web developer started where you are now—facing challenges and overcoming obstacles. It is not about knowing everything from the start; it is about the determination to keep learning and growing. \nWhen you dive into Flask, you are not just coding; you are crafting solutions, building dreams, and creating experiences for users. Embrace each challenge as an opportunity to learn and improve. Your passion and persistence are your greatest tools. \nCelebrate your progress, no matter how small, and keep pushing forward. Each bug you fix and each feature you build brings you one step closer to mastering your craft. \nBelieve in your journey. Your dedication will turn aspirations into achievements. Keep coding, keep learning, and let your creativity shine. The world is waiting to see what you’ll create with Flask! \nYou have got this!. \n\nBest regards,\nYour Automated System'
    return subject, body

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except (gaierror, ConnectionRefusedError) as e:
        print(f"Failed to connect to SMTP server: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication failed: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the task
def send_daily_report():
    subject, body = create_email_content()
    recipient = 'recipient@example.com'  # Replace with the recipient's email address
    send_email(subject, body, recipient)

# Schedule the task
schedule.every().day.at("09:00").do(send_daily_report)  # Set the time for sending the email

# Keep the script running
if __name__ == "__main__":
    print("Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait a minute
