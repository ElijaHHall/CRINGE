from twilio.rest import Client

account_sid = "ACec2c50cc9f1876ae8729bf05023c32b7"
auth_token = "ed2ea0f981ecfae2b7d0122c590cbee4"
my_cell = "+19702273514"
my_twilio = "+19513092057"

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "call the cops i'm dead"
