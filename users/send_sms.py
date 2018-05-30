from twilio.rest import Client

account_sid = "ACec2c50cc9f1876ae8729bf05023c32b7"
auth_token = "ed2ea0f981ecfae2b7d0122c590cbee4"

# if you want to send a group sms, uncomment the my_cell array with the group inside of it and comment out the single number below, and vice versa

# my_cell = ["+19702273514", "+17087384175", "+17205971878", "+16787874272"]
# my_cell = ["+17087384175"]
my_cell = ["+16787874272"]
my_twilio = "+19513092057"

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

# same thing goes for these

# my_msg = "this is a test, hope y'all get it"
my_msg = ["call the cops i'm dead", "you up?", "hey.! can u pick me up am drnuk?", "you should do your half a work and I have a little money to get!!1!", "You're mom says hi", "Sorry about last night, you should probably get tested...", "It looks bigger on an iPad", "The mitochondria is the powerhouse of the cell"]
