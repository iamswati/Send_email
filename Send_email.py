# Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib as s



# Port 587: This is the default mail submission port. When an email client or outgoing server is submitting an email to be routed by a proper mail server, it should always use SMTP port 587 as the default port.
ob = s.SMTP("smtp.gmail.com",  587)

ob.starttls()

# Two parameters: email, pass
ob.login("sg131019@gmail.com", "")

subject="Send Email Using Python"
body="Hi, The email is sending using python."

message = "Subject:{}\n\n{}".format(subject, body)
# print(message)


listOfAddress = ["swatigulati@outlook.in"]

ob.sendmail("sg131019@gmail.com", listOfAddress, message)
print("send successfully.....")
ob.quit()
