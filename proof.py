#W
#Please read the README file before assessing

#Importing Libraries
import pyautogui
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Omar Bakr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf083672641deb03941d505694edca2da"
# Your Auth Token from twilio.com/console
auth_token  = "17149879a1d67538c332f1134bd084fa"

client = Client(account_sid, auth_token)
# from pushbullet import PushBullet

# API_KEY = "o.GoVgB0ldmujStfog709gCjfQNSSq5kFs"

time.sleep(3)

calledName = False
# with open("test.txt", "r+") as file:
textList = []

previous = []
difference = []
total = []

while calledName == False:
    time.sleep(1)
    myScreenshot = pyautogui.screenshot(region=(325,400, 800, 250))
    myScreenshot.save('image3.png')
    userCurrent = " "
    userPast = " "
    # Use OCR to extract text from Image


    img = Image.open("image3.png")
    text = tess.image_to_string(img)
    os.remove("image3.png")
    textList.append(text)
    
    s = text

    current = s.split()

    if len(previous) > 0:
        for i in range(len(current)):
            if current[0:i] in previous:
                continue
            else:
                difference = current[i -1:len(current)]
    else:
        difference = current

    previous = current
    total.append(difference)
    totalLen = len(total)
    # print(totalLen)


        
        
        
    word = "Omar"
    # count = 1

    if word in text:
        # print("found on line", count)
        # pb = PushBullet(API_KEY)
        # push = pb.push_note('Come back to class you fucking donkey',text)
        print("Found")
        calledName = True
        # message = client.messages.create(
        #     to="+16475499325", 
        #     from_="+16463511854",
        #     body="You've been called in your meet")

        # print(message.sid)

        # call = client.calls.create(
        #     twiml='<Response><Say>Hello</Say></Response>',
        #     to="+16475499325", 
        #     from_="+16463511854",
        # )
        break


# print(total)








# lines = filter(lambda x: not x.isspace(), lines)
# file = open("output.txt","w")
# file.write("".join(lines))
# file.close()

# print(userCurrent)



#print(text[0:4])

# print(userCurrent)

asdf = []
for v in range(len(total)):
    totalString = " ".join(total[v])
    asdf.append(totalString)

t = ' '.join(asdf)
f = open('test.txt', 'w')
for i in range(len(t)):
    if t[i] != '.':
        f.write(t[i])
    else:
        f.write('.\n')

f.close()
