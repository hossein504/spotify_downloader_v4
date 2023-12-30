from pyrogram import Client, filters 
from pyrogram.types import (Message)
from time import sleep

#+++++++++++
admins = {"owner": "5406865643"}
#+++++++++++

api_hash = "" #your hash
api_id = 11111111


app = Client("acc_spotify", api_id, api_hash)

@app.on_message()
async def main(c:Client, m:Message):

    txt = m.text
    if txt != None:
        if txt.find("This track isn't available for download") != -1:
            await app.send_message("@ho3_jrbot","برای دانلود در دسترس نیست.\n (لینک آلبوم ارسال نکنید)🥸")
        if txt.find("I couldn't find anything") != -1:
            await app.send_message("@ho3_jrbot","چیزی پیدا نکردم🥸")
        if txt.find("Currently i support only") != -1:
            await app.send_message("@ho3_jrbot","لینک اشتباهه دادا🥸")
        if txt.find("Seems like this song is unavailable for bot") != -1:
            await app.send_message("@ho3_jrbot","نمیتونم دانلودش کنم")
    if m.chat.id == 5696025729: # دریافت از بات
        link = m.text
        spotify_link = "https://open.spotify.com/"
        soundcl_link = "https://soundcloud.com/"
        soundcl2_link = "https://on.soundcloud.com/"


        find = link.find(spotify_link)
        if find != -1:
            await app.copy_message("@RegaSpotify_Bot", 5696025729, m.id) # ارسال به ربات اسپاتیفای
            find = -1
        if link.find(soundcl_link) != -1 or link.find(soundcl2_link) != -1:
            await app.copy_message("@scload_bot", 5696025729, m.id) # ارسال به ربات ساند
            find = -1
            
    if m.chat.id == 5360488345:
        try:
            type = m.audio.mime_type
            if type.find("audio") != -1:
                await app.copy_message("@ho3_jrbot", m.chat.id, m.id, caption="@Send_Music_Please \n from spotify") #ارسال به بات از ربات ها
        except:
            pass
    if m.chat.id == 1561498184:
        try:
            type = m.audio.mime_type
            if type.find("audio") != -1:                              
                await app.copy_message("@ho3_jrbot", m.chat.id, m.id, caption="@Send_Music_Please \n from soundcloud" )
        except:
            pass
app.run()


# Client.connect(self= client)
# sent_code_info = client.send_code(phone_number)
# phone_code = input("Please enter your phone code: ")  # Sent phone code using last function
# client.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)
