class Translation(object):
    START_TEXT = "Hi."
    INPUT_PHONE_NUMBER = "Kirim nomormu untuk mendapatkannya"
    ALREADY_REGISTERED_PHONE = "Nomor ini terdaftar di Telegram. Harap masukkan kode verifikasi yang Anda terima [Telegram](tg://user?id=777000) dipisahkan oleh spasi, jika tidak, PhoneCodeInvalidError akan dimunculkan."
    NOT_REGISTERED_PHONE = "This number is not registered on Telegram. Please check your #karma by reading https://t.me/c/1220993104/28753"
    PHONE_CODE_IN_VALID_ERR_TEXT = "Invalid Code Received. Please re /start"
    ACC_PROK_WITH_TFA = "The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__"
    LOG_MESSAGE_FOR_DBGING = """@UniBorg
**ID**: {APP_ID}
**HASH**: {API_HASH}
[Current User ID](tg://user?id={C}): {C}
[Logged In User ID](tg://user?id={L}): {L}"""
