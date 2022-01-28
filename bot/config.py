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
    APP_ID = config("APP_ID", cast=int, default='14142054')
    API_HASH = config("API_HASH", default='d7d057a6d2f2490204420daf5b91c5fb')
    BOT_TOKEN = config("BOT_TOKEN", default='5004574248:AAFRdfn3R5aAswHpzTPWSfy7bNu5oZ6IyPw')
    DEV = 1322549723
    OWNER = config("OWNER",default='1171770592')
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -b:v 450k -map 0:v -c:a libvorbis -b:a 32k -ac 6 -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
