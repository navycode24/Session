import os
from os import getenv
from dotenv import load_dotenv

AKTIFPERINTAH = {}

load_dotenv(".env")


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")
TG_BOT_WORKERS = int(getenv("TG_BOT_WORKERS", "4"))
COMMM_AND_PRE_FIX = getenv("COMMM_AND_PRE_FIX", "/")
START_COMMAND = getenv("START_COMMAND", "start")
LOG_FILE_ZZGEVC = getenv("LOG_FILE_ZZGEVC", "kynan.log")



START_OTHER_USERS_TEXT = getenv(
    "START_OTHER_USERS_TEXT",
    (
        """
        Selamat Datang Di Naya Session
        """
    )
)
INPUT_PHONE_NUMBER = getenv("INPUT_PHONE_NUMBER", (
    "Masukkan Nomor Akun Telegram"
))
RECVD_PHONE_NUMBER_DBP = getenv("RECVD_PHONE_NUMBER_DBP", (
    "Mencoba mengirim otp, silahkan cek otp"
))
ALREADY_REGISTERED_PHONE = getenv("ALREADY_REGISTERED_PHONE", (
    "Periksa Pesan Masuk"
))
CONFIRM_SENT_VIA = getenv("CONFIRM_SENT_VIA", (
    "kode otp dikirim dari {}"
))
RECVD_PHONE_CODE = getenv("RECVD_PHONE_CODE", (
    "Mencoba mengirim otp, silahkan cek otp"
))
NOT_REGISTERED_PHONE = getenv("NOT_REGISTERED_PHONE", (
    "Nomor terverifikasi belum terdaftar tele gan"
))
PHONE_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode otp salah su. ketik atau tekan ini /start"
)
TFA_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode verif salah su. ketik atau tekan ini /start"
)
ACC_PROK_WITH_TFA = getenv("ACC_PROK_WITH_TFA", (
    "Diverif 2 langkah nih, paste dibawah cuy"
))
SESSION_GENERATED_USING = getenv("SESSION_GENERATED_USING", (
    "Terima kasih telah menggunakan bot ini ..."
))