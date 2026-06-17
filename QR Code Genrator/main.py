import qrcode 

# UPI id ->

UPI = input("Enter Your UPI Id: ")

# Payment for app

PhonePe_url = f"upi://pay?pa={UPI}&pn=Recipient%20Name&mc='1234'"

# Qr code for PhonePe

PhonePe = qrcode.make(PhonePe_url)

# Display Qr code

PhonePe.show()
