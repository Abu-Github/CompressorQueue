#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int, default='1906076')
    API_HASH = config("API_HASH", default='3be910cde04b3f810cd843880b24f737')
    BOT_TOKEN = config("BOT_TOKEN", default='5306377919:AAGxkSjlbHKx1yDdA1lCmHvH5ePXSznv2n4')
    DEV = 682111519
    OWNER = config("OWNER",default='682111519')
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i '''{}''' -c:v libx265  -s 1920x1080  -preset fast  -crf 18 -c:a aac -b:a 192k -metadata title="Sonic Otakus"  -pix_fmt yuv420p -metadata:s:a title="Sonic Otakus" -metadata:s:s title="Sonic Otakus" -map 0 '''{}''' -y',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/c5a7e41b5f23b8ec69f4d.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
