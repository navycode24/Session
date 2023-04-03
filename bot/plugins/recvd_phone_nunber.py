
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AKTIFPERINTAH,
    ALREADY_REGISTERED_PHONE,
    CONFIRM_SENT_VIA,
    RECVD_PHONE_NUMBER_DBP,
    app
)
from bot.user import User


@app.on_message(
    filters.text & filters.private, group=1
)
async def recvd_ph_no_message(client, message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    status_message = w_s_dict.get("START")
    if not status_message:
        return
    del w_s_dict["START"]
    status_message = await message.reply_text(
        "Mohon periksa pesan masuk anda, dan masukkan kode yang ada dengan menggunakan spasi setiap kode\n Contoh : 1 2 3 4 5"
    )
    loical_ci = User()
    w_s_dict["PHONE_NUMBER"] = message.text
    await loical_ci.connect()
    w_s_dict["SENT_CODE_R"] = await loical_ci.send_code(
        w_s_dict["PHONE_NUMBER"]
    )
    w_s_dict["USER_CLIENT"] = loical_ci

    status_message = await status_message.edit_text(
        ALREADY_REGISTERED_PHONE
        + "\n\n"
        + CONFIRM_SENT_VIA.format(w_s_dict["SENT_CODE_R"].type.value)
    )
    w_s_dict["MESSAGE"] = status_message
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()