from django.shortcuts import render
from .services import *
# Create your views here.
from telegram import ReplyKeyboardMarkup, KeyboardButton


def btns(type=None):
    if type == "ctg":
        ctg = get_ctgs()
        btn = []
        for i in range(1, len(ctg)):
            btn.append([KeyboardButton(ctg[i].get('content', "")),
                        KeyboardButton(ctg[i-1].get('content', "")),
                        ])

        if len(ctg) % 2 == 1:
            btn.append([KeyboardButton(ctg[-1].get('content', ""))])
    else:
        btn = [
            [KeyboardButton("Contact", request_contact=True)]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    tg_user = get_user(user.id)
    try:
        log = get_user(user.id).get('message', {})
    except:
        log = get_log(user.id)

    if not tg_user:
        tg_user = create_user(user.id)

    if not log:
        log = create_log(user.id)['message']
    state = log['state']

    if state == 3:
        log['state'] = 4
        update.message.reply_text("Bosh menyu")
        update.message.reply_text("Categoriyalardan birini tanlang", reply_markup=btns('ctg'))
    else:
        log['state'] = 1
        update.message.reply_text("Assalomu Alaykum 😁 Mebel Botimizga xush kelibsiz 😁 ")

    change_log(user_id=user.id, message=log)


def message_handler(update, context):
    user = update.message.from_user
    tg_user = get_user(user.id)
    log = get_log(user.id)['message']
    state = log['state']
    msg = update.message.text

    if state == 1:
        log["ism"] = msg
        log['state'] = 2
        update.message.reply_text("Familiyangizni kiriting")
    elif state == 2:
        log["familiya"] = msg
        log['state'] = 3
        update.message.reply_text("Telefon raqamingizni kiring", reply_markup=btns)
    elif state == 3:
        log['phone'] = msg
        log['state'] = 4
        update_user(user, log)
        update.message.reply_text("Bosh menyu")
        update.message.reply_text("Categoriyalardan birini tanlang", reply_markup=btns('ctg'))

    change_log(user_id=user.id, message=log)


def recieved_contact(update, context):
    user = update.message.from_user
    tg_user = get_user(user.id)
    log = get_log(user.id)['message']
    state = log['state']
    msg = update.message.contact
    if state == 3:
        log['phone'] = msg.phone_number
        log['state'] = 4
        update_user(user, log)
        update.message.reply_text("Bosh menyu")
        update.message.reply_text("Categoriyalardan birini tanlang", reply_markup=btns('ctg'))

    change_log(user_id=user.id, message=log)


def recieved_photo(update, context):
    pass
