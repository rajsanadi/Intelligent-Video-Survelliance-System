
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "svm892073@gmail.com"
APP_PASSWORD = "xjpbqxdhiywmtuqp"


print("Mail Start")
msg = EmailMessage()
msg['Subject'] = "Anomaly Activity Detection"
msg['From'] = SENDER_EMAIL
msg['To'] = "vaishnavi.vst@gmail.com"
msg.set_content('Anomaly Activity Detected')

   


# with open('D:/bitmap/100%-Face Attendance with Excel Sheet/100%-Face Attendance with Excel Sheet/pandas_to_excel.xls', 'rb') as f:
#         file_data = f.read()
# msg.add_attachment(file_data, maintype="application", subtype="vnd.ms-excel", filename='D:/bitmap/100%-Face Attendance with Excel Sheet/100%-Face Attendance with Excel Sheet/pandas_to_excel.xls')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("Mail send successfully")
