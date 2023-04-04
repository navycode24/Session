

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    SessionPasswordNeeded,
    BadRequest
)
from bot import (
    ACC_PROK_WITH_TFA,
    AKTIFPERINTAH,
    PHONE_CODE_IN_VALID_ERR_TEXT,
    RECVD_PHONE_CODE,
    SESSION_GENERATED_USING,
    app
)


@app.on_message(
    filters.text &
    filters.private,
    group=2
)
async def recv_tg_code_message(_, message: Message):

    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    sent_code = w_s_dict.get("SENT_CODE_R")
    phone_number = w_s_dict.get("PHONE_NUMBER")
    loical_ci = w_s_dict.get("USER_CLIENT")
    if not sent_code or not phone_number:
        return
    status_message = w_s_dict.get("MESSAGE")
    if not status_message:
        return
    # await status_message.delete()
    del w_s_dict["MESSAGE"]
    status_message = await message.reply_text(
        RECVD_PHONE_CODE
    )
    phone_code = "".join(message.text.split(" "))
    try:
        w_s_dict["SIGNED_IN"] = await loical_ci.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            phone_code
        )
    except BadRequest as e:
        await status_message.reply_text(
          f"{e} \n\nKode yang anda masukkan salah, coba masukan kembali atau mulai dari awal"
        )
        del AKTIFPERINTAH[message.chat.id]
    except SessionPasswordNeeded:
        await status_message.reply_text(
          "Verifikasi 2 Langkah Diaktifkan, Mohon Masukkan Verifikasi 2 Langkah Anda."
        )
        w_s_dict["IS_NEEDED_TFA"] = True
    else:
        await status_message.edit_text(
            "<code>" + str(await loical_ci.export_session_string()) + "</code>"
        )
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()
