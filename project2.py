# personal Rule based AI chat bot by python 
import datetime
import time
name = input("welcome , enter your name :")
present_hour = datetime.datetime.now().hour
if present_hour >4 and present_hour<=12:
    print("Good Morning",name)
elif present_hour>12 and present_hour<= 15:
    print("Good Afternoon",name)
elif present_hour>15 and present_hour<=19:
    print("Good evening",name)
else:
    print("Good Night",name)


print("Namaste! , welcome to AI chat bot")
print("you can ask me basic questions ,type 'bye to exit from the bot")
# creation of chat bot meemory [dictionary of responses]
responses = {
    "hello" : "Hi,how I can help you",
    "how are you": "Iam fine,Thank you",
    "who are you" : "Iam rule based AI chat bot",
    "motivate me": "keep going, every bugs in your project helps you to become a better developer",
    "Is AI is intresting ?": "Yes absolutely!",
    "what are string ?" : "string is the sequence of characters",
}
# function to get response of chat bot
def getresponseofbot(user_input):
    user_input = user_input.lower()
    for eachkey in responses:
        if eachkey in user_input:
            return responses[eachkey]
    return "iam not able to answer this question now , i will learn it soon!"
    

# user input
while True:
    user_input = input("Ask your question : ")
    if user_input.lower()== "bye":
        print("Goodbye!")
        break
    reply = getresponseofbot(user_input)
    print(reply)
    
    


    

