from twilio.rest import Client

account_sid = "ACec2c50cc9f1876ae8729bf05023c32b7"

auth_token = "ed2ea0f981ecfae2b7d0122c590cbee4"

# my_cell = ["+19702273514", "+17087384175", "+17205971878", "+16787874272"]
my_cell = ["+19702273514"]
my_twilio = "+19513092057"

client = Client(account_sid, auth_token)

# my_msg = "this is a test, hope y'all get it"
my_msg = ["call the cops i'm dead", "you up?", "hey.! can u pick me up am drnuk?", "You're mom says hi", "Sorry about last night, you should probably get tested...", "It looks bigger on an iPad", "The mitochondria is the powerhouse of the cell", "I'm an INDEPENDENT women and I don't need no man", "let’s talk about abortion and planned parenthood", "TRUMP 2020", "1st of May", "Knock, knock. Who’s there? To. To who? To whom.", "What’s green and has wheels? Grass, I lied about the wheels", "You see that bush over there? I'm behind it", 'Sex is not the answer. Sex is the question. “Yes” is the answer.', "How come there isn’t white chocolate milk?", "I didn’t fight my way to the top of the food chain to be a vegetarian", "Jesus loves you, but everyone else thinks you’re an asshole.", "It costs me $15k to make this app", "This is a very special message from the engineers of CRINGE: We love you, please fund version 2", "Bears, Beats, Battlestar Galactica", "I’m not superstitious but I am a little stitious", "Have you heard about the new graveyard up the hill? People are dying to get in.", "They're making a movie about clocks. It's about time", "Can you make me a sandwich? Poof, you're a sandwich.", "Why do birds fly south for the winter? Because it's too far to walk.", "Do I enjoy making courthouse puns? Guilty", "Is your spirit animal a beaver? Because dam...", "Bye Felicia", "If I had to rate you from 1-10, I would rate you as a 9 because I am the one that you are missing."]
