from pyrogram import Client, filters , enums, raw
from pyrogram.types import (Message)
import sqlite3
from datetime import datetime

db = sqlite3.connect("DataBase_v4_spotify.db")
cur = db.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    userid INTEGER,
    name VARCHAR(30),
    lastname VARCHAR(30),
    usernames VARCHAR(30),
    chatid INTEGER
    gr INTEGER
    )"""
)
db.commit

#+++++++++++
admins = [] #id admin
accepted_gr = [] #id group
#+++++++++++

bot_token ="" #your bot token
api_hash = "" #your hash
api_id = 11111111

app = Client(
    "my_bot_v2",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


#+++++++++++
ids = [] #be empyt
selected_gr = [] #be empyt
#+++++++++++

async def send_to_acc(m):
    link = m.text
    spotify_link = "https://open.spotify.com/"
    soundcl_link = "https://soundcloud.com/"
    soundcl2_link = "https://on.soundcloud.com/"

    try:
        if link.find(spotify_link) != -1:

            a1 =m.id
            ids.append(a1)
            a1 =m.chat.id
            ids.append(a1)
            a1 = m.from_user.first_name
            ids.append(a1)
            a1 = m.from_user.id
            ids.append(a1)

            await app.copy_message(1525556102, m.chat.id , m.id, caption="sp")
            await app.delete_messages(m.chat.id, m.id)
            await app.send_message(m.chat.id, "لینک اسپاتیفای دریافت شد (لینک آلبوم ارسال نکنید). \n لطفا صبر کنید💋... ")
            await app.send_chat_action(m.chat.id, enums.ChatAction.UPLOAD_AUDIO)
    except:
        pass

    try:
        if link.find(soundcl_link) != -1 or link.find(soundcl2_link) != -1:

            a1 =m.id
            ids.append(a1)
            a1 =m.chat.id
            ids.append(a1)
            a1 = m.from_user.first_name
            ids.append(a1)
            a1 = m.from_user.id
            ids.append(a1)

            await app.copy_message(1525556102, m.chat.id , m.id, caption="sc")
            await app.delete_messages(m.chat.id, m.id)
            await app.send_message(m.chat.id, " لینک ساوندکلاد دریافت شد (لینک آلبوم ارسال نکنید). \n لطفا صبر کنید💋... ")
            await app.send_chat_action(m.chat.id, enums.ChatAction.UPLOAD_AUDIO)

    except:
        pass
    # else:
    #     await app.send_message(m.chat.id, "این ربات فقط در گروه زیر اجرا میشود: \n https://t.me/+6F9-WsT2zB85Nzdk")


@app.on_message(filters.group)
async def main(c:Client, m:Message):
    try:
        if m.chat.id == -1001707603062:
            if m.from_user.id != 5696025729:
                type = m.audio.mime_type
                if type.find("audio") != -1:
                    name_NumberSign = ""
                    for i in m.from_user.first_name:
                        if i ==" ":
                            name_NumberSign += "_"
                        else:
                            name_NumberSign += i

                    await app.copy_message(-1002011650311, -1001707603062 , m.id, caption="**from: **{} \n @io_music".format(name_NumberSign))
                    name_NumberSign=""

                
    except:
        pass
    
    for i in accepted_gr:
        if m.chat.id == i: 
            selected_gr.append(i)
            await send_to_acc(m)

@app.on_message()
async def main(c:Client, m:Message):
    def check_id(id):
        cur.execute("SELECT userid FROM users WHERE userid=?", (m.from_user.id,))
        result = cur.fetchone()
        if result:
            return True
        else:
            return False
    
    def insertdata(userId ,userfirst ,userlast ,userusername,usetchatid, gr):
        if check_id(userId):
            pass
        else:
                
            db.execute(
                """INSERT INTO users(userid,name,lastname,usernames,chatid) VALUES(?,?,?,?,?)""",(userId, userfirst, userlast, userusername,usetchatid)
            )
            db.commit()

    async def joinednum(userid):
        try:
            fr = await app.get_chat_member(-1002011650311, userid)
            return(True)
        except:
            return(False)
            # if m.from_user.id == i.user.id:
            #     return(True)

    insertdata(m.from_user.id, m.from_user.first_name, m.from_user.last_name, m.from_user.username, m.chat.id, joinednum)


    if m.chat.id == 1525556102:
        name_NumberSign = ""
        for i in ids[2]:
            if i ==" ":
                name_NumberSign += "_"
            else:
                name_NumberSign += i

        await app.copy_message(selected_gr[-1], 1525556102, m.id, caption="[Send Music Please](https://t.me/+6F9-WsT2zB85Nzdk) \n لینک از: [{0}](tg://openmessage?user_id={1})\n#{2}".format(ids[2], ids[3], name_NumberSign))
        if str(selected_gr).find("-") != -1:
            await app.copy_message(-1002011650311, 1525556102, m.id, caption= "**from: **#{} \n @io_music".format(name_NumberSign))

        else:
            await app.copy_message(-1001954160501, 1525556102, m.id, caption= "**from: **#{} \n @io_music".format(name_NumberSign))
        name_NumberSign = ""
        selected_gr.pop(0)
        await app.delete_messages(ids[1], ids[0]+1)
        ids.pop(0)
        ids.pop(0)
        ids.pop(0)
        ids.pop(0)
    ok=False
    for i in admins:
        if m.from_user.id == i:
            ok = True
            if m.text == "/check":
                await app.send_message(i,"**online!**")
                
            if m.text == "/ping" or m.text == "Ping":
                start_t = datetime.now()
                await app.send_message(m.chat.id,"Pong!")
                end_t = datetime.now()
                time_taken_s = (end_t - start_t).microseconds / 1000
                await app.send_message(m.chat.id,f"Ping Pong Speed\n{time_taken_s} milli-seconds")

    joined = await joinednum(m.from_user.id)
    if ok == False and m.chat.id != 1525556102 and joined !=True:
        await app.send_message(m.chat.id, "لطفا لینک را در [گروه](http://t.me/+6F9-WsT2zB85Nzdk) ارسال کنید. \n یا در [چنل](https://t.me/+_nUo_Er35CE2NDQ0) عضو شوید تا در همینجا بتوانید از ربات استفاده کنید. \n بعد از عضویت در چنل لینک را ارسال نمایید", disable_web_page_preview=True)


    if joined == True:
        selected_gr.append(m.chat.id)
        await send_to_acc(m)


app.run()
