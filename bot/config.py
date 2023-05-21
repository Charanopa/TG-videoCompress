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
    APP_ID = config("12001153", cast=int)
    API_HASH = config("c388da32bc40c14a9d4dc64f8f96f134")
    BOT_TOKEN = config("6278628468:AAGp4FYKM1V73kTbxnU0julBfAxhuVcDiZY")
    DEV = 1287276743
    OWNER = config("6113562037")
    ffmpegcode = [" -c:v libx265 -preset medium -x265-params crf=28 -c:a aac -strict experimental -b:a 128k -map 0:v -map 0:a -map 0:s -c:a copy -c:s copy  -metadata 'title=Never_xy'"]
    THUMB = config("https://telegra.ph/file/e63c07cd04a2255f7c185.jpg")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
