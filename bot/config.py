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
    APP_ID = config("APP_ID", cast=int, default="1906076")
    API_HASH = config("API_HASH", default="3be910cde04b3f810cd843880b24f737")
    BOT_TOKEN = config(
        "BOT_TOKEN", default="5306377919:AAGxkSjlbHKx1yDdA1lCmHvH5ePXSznv2n4"
    )
    DEV = 682111519
    OWNER = config("OWNER", default="682111519")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -b:v 450k -map 0:v -c:a libvorbis -b:a 32k -ac 6 -map 0:a -c:s copy -map 0:s? "{}"',
    )
    THUMB = config("THUMBNAIL", default="")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
