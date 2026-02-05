# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


HELP_1 = """<b><u>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs :</b></u>

ᴊᴜsᴛ ᴀᴅᴅ <b>ᴄ</b> ɪɴ ᴛʜᴇ sᴛᴀʀᴛɪɴɢ ᴏғ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜsᴇ ᴛʜᴇᴍ ғᴏʀ ᴄʜᴀɴɴᴇʟ.


/pause : ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

/resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

/skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.

/end ᴏʀ /stop : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

/player : ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ.

/queue : sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.
"""

HELP_2 = """
<b><u>ᴀᴜᴛʜ ᴜsᴇʀs :</b></u>

ᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

/auth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] : ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.
/unauth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴀᴜᴛʜ ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ.
/authusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.
"""

HELP_3 = """
<u><b>ʙʀᴏᴀᴅᴄᴀsᴛ ғᴇᴀᴛᴜʀᴇ</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :
/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs :</u>
<b>-pin</b> : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.
<b>-pinloud</b> : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs.
<b>-user</b> : ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.
<b>-assistant</b> : ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.
<b>-nobot</b> : ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ.
<b>-forward</b> : ғᴏʀᴡᴀʀᴅs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴏʀɪɢɪɴᴀʟ ᴄʜᴀɴɴᴇʟ/ᴜsᴇʀ ᴀᴛᴛʀɪʙᴜᴛɪᴏɴ.
<b>-wfchat</b> : sᴘᴇᴄɪᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴏᴅᴇ ғᴏʀ ᴄʜᴀᴛs (ᴡᴏʀᴋs ᴡɪᴛʜ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs).
<b>-wfuser</b> : sᴘᴇᴄɪᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴏᴅᴇ ғᴏʀ ᴜsᴇʀs (ᴡᴏʀᴋs ᴡɪᴛʜ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs).

<b>ɴᴏᴛᴇ:</b> -wfchat and -wfuser modes require replying to a message.
"""

HELP_4 = """<u><b>ᴄʜᴀᴛ ʙʟᴀᴄᴋʟɪsᴛ ғᴇᴀᴛᴜʀᴇ :</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

ʀᴇsᴛʀɪᴄᴛ sʜɪᴛ ᴄʜᴀᴛs ᴛᴏ ᴜsᴇ ᴏᴜʀ ᴘʀᴇᴄɪᴏᴜs ʙᴏᴛ.

/blacklistchat [ᴄʜᴀᴛ ɪᴅ] : ʙʟᴀᴄᴋʟɪsᴛ ᴀ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ.
/whitelistchat [ᴄʜᴀᴛ ɪᴅ] : ᴡʜɪᴛᴇʟɪsᴛ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ.
/blacklistedchat : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs.
"""

HELP_5 = """
<u><b>ʙʟᴏᴄᴋ ᴜsᴇʀs:</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

sᴛᴀʀᴛs ɪɢɴᴏʀɪɴɢ ᴛʜᴇ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴜsᴇʀ, sᴏ ᴛʜᴀᴛ ʜᴇ ᴄᴀɴ'ᴛ ᴜsᴇ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.

/block [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʙʟᴏᴄᴋ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴏᴜʀ ʙᴏᴛ.
/unblock [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴜɴʙʟᴏᴄᴋs ᴛʜᴇ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀ.
/blockedusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs.
"""

HELP_6 = """
<u><b>ᴄʜᴀɴɴᴇʟ ᴩʟᴀʏ ᴄᴏᴍᴍᴀɴᴅs:</b></u>

ʏᴏᴜ ᴄᴀɴ sᴛʀᴇᴀᴍ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ɪɴ ᴄʜᴀɴɴᴇʟ.

/cplay : sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋ ᴏɴ ᴄʜᴀɴɴᴇʟ's ᴠɪᴅᴇᴏᴄʜᴀᴛ.
/cvplay : sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋ ᴏɴ ᴄʜᴀɴɴᴇʟ's ᴠɪᴅᴇᴏᴄʜᴀᴛ.
/cplayforce or /cvplayforce : sᴛᴏᴩs ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ.

/channelplay [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] ᴏʀ [ᴅɪsᴀʙʟᴇ] : ᴄᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀ ɢʀᴏᴜᴩ ᴀɴᴅ sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʀᴀᴄᴋs ʙʏ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴄᴏᴍᴍᴀɴᴅs sᴇɴᴛ ɪɴ ɢʀᴏᴜᴩ.
"""

HELP_7 = """
<u><b>ɢʟᴏʙᴀʟ ʙᴀɴ ғᴇᴀᴛᴜʀᴇ</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/gban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ɢʟᴏʙᴀʟʟʏ ʙᴀɴs ᴛʜᴇ ᴄʜᴜᴛɪʏᴀ ғʀᴏᴍ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ ʙʟᴀᴄᴋʟɪsᴛ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ.
/ungban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ɢʟᴏʙᴀʟʟʏ ᴜɴʙᴀɴs ᴛʜᴇ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀ.
/gbannedusers : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs.
"""

HELP_8 = """
<b><u>ʟᴏᴏᴘ sᴛʀᴇᴀᴍ :</b></u>

<b>sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ɪɴ ʟᴏᴏᴘ</b>

/loop [enable/disable] : ᴇɴᴀʙʟᴇs/ᴅɪsᴀʙʟᴇs ʟᴏᴏᴘ ғᴏʀ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ
/loop [1, 2, 3, ...] : ᴇɴᴀʙʟᴇs ᴛʜᴇ ʟᴏᴏᴘ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴠᴀʟᴜᴇ.
"""

HELP_9 = """
<u><b>ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/logs : ɢᴇᴛ ʟᴏɢs ᴏғ ᴛʜᴇ ʙᴏᴛ.

/logger [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] : ʙᴏᴛ ᴡɪʟʟ sᴛᴀʀᴛ ʟᴏɢɢɪɴɢ ᴛʜᴇ ᴀᴄᴛɪᴠɪᴛɪᴇs ʜᴀᴩᴩᴇɴ ᴏɴ ʙᴏᴛ.

/maintenance [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] : ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ʏᴏᴜʀ ʙᴏᴛ.
"""

HELP_10 = """
<b><u>ᴘɪɴɢ & sᴛᴀᴛs :</b></u>

/start : sᴛᴀʀᴛs ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ.
/help : ɢᴇᴛ ʜᴇʟᴩ ᴍᴇɴᴜ ᴡɪᴛʜ ᴇxᴩʟᴀɴᴀᴛɪᴏɴ ᴏғ ᴄᴏᴍᴍᴀɴᴅs.

/ping : sʜᴏᴡs ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

/stats : sʜᴏᴡs ᴛʜᴇ ᴏᴠᴇʀᴀʟʟ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
"""

HELP_11 = """
<u><b>ᴩʟᴀʏ ᴄᴏᴍᴍᴀɴᴅs :</b></u>

<b>v :</b> sᴛᴀɴᴅs ғᴏʀ ᴠɪᴅᴇᴏ ᴩʟᴀʏ.
<b>force :</b> sᴛᴀɴᴅs ғᴏʀ ғᴏʀᴄᴇ ᴩʟᴀʏ.

/play ᴏʀ /vplay : sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.

/playforce ᴏʀ /vplayforce : sᴛᴏᴩs ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ.
"""

HELP_12 = """
<b><u>sʜᴜғғʟᴇ ᴏ̨ᴜᴇᴜᴇ :</b></u>

/shuffle : sʜᴜғғʟᴇ's ᴛʜᴇ ᴏ̨ᴜᴇᴜᴇ.
/queue : sʜᴏᴡs ᴛʜᴇ sʜᴜғғʟᴇᴅ ᴏ̨ᴜᴇᴜᴇ.
"""

HELP_13 = """
<b><u>sᴇᴇᴋ sᴛʀᴇᴀᴍ :</b></u>

/seek [ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs] : sᴇᴇᴋ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴛᴏ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴜʀᴀᴛɪᴏɴ.
/seekback [ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs] : ʙᴀᴄᴋᴡᴀʀᴅ sᴇᴇᴋ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴛᴏ ᴛʜᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴜʀᴀᴛɪᴏɴ.
"""

HELP_14 = """
<b><u>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ</b></u>

/song [sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ] : ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ɪɴ ᴍᴘ3 ᴏʀ ᴍᴘ4 ғᴏʀᴍᴀᴛs.
"""

HELP_15 = """
<b><u>sᴘᴇᴇᴅ ᴄᴏᴍᴍᴀɴᴅs :</b></u>

ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛʀᴏʟ ᴛʜᴇ ᴘʟᴀʏʙᴀᴄᴋ sᴘᴇᴇᴅ ᴏғ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ. [ᴀᴅᴍɪɴs ᴏɴʟʏ]

/speed or /playback : ғᴏʀ ᴀᴅᴊᴜsᴛɪɴɢ ᴛʜᴇ ᴀᴜᴅɪᴏ ᴘʟᴀʏʙᴀᴄᴋ sᴘᴇᴇᴅ ɪɴ ɢʀᴏᴜᴘ.
/cspeed or /cplayback : ғᴏʀ ᴀᴅᴊᴜsᴛɪɴɢ ᴛʜᴇ ᴀᴜᴅɪᴏ ᴘʟᴀʏʙᴀᴄᴋ sᴘᴇᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟ.
"""

HELP_16 = """
<b><u>ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ:</b></u>

/Privacy : Display the privacy statement for Sarcastic Bot 
"""

HELP_17 = """
<b><u>ɢᴀᴍᴇs</b></u>

/dice : Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
/ludo : Pʟᴀʏ Lᴜᴅᴏ.
/dart : Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
/basket ᴏʀ /basketball : Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
/football : Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
/slot ᴏʀ /jackpot : Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
/bowling : Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
"""

HELP_18 = """
<b><u>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs</b></u>
/ban - Ban A User
/banall - Ban All Users
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message
/unpinall - unpinall messages
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins.
"""

HELP_19 = """
<b><u>ɪᴍᴀɢᴇ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ:</b></u>

/tgm : ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀɴʏ ɪᴍᴀɢᴇ,ᴠɪᴅᴇᴏ ᴏʀ ɢɪғ
"""

HELP_20 = """
<b><u>ᴛᴀɢ ᴄᴏᴍᴍᴀɴᴅs:</b></u>

/tagall [ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴏɴ ᴀɴʏ ᴄʜᴀᴛ] : ᴛᴀɢ ᴀʟʟ ᴜsᴇʀs.
/admins [ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴏɴ ᴀɴʏ ᴄʜᴀᴛ] : ᴛᴀɢ ᴀʟʟ ᴀᴅᴍɪɴs.
"""

HELP_21 = """
<b><u>ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏs:</b></u>

/vid : ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ɪɴsᴛᴀ ᴛᴡɪᴛᴛᴇʀ ᴀɴᴅ ᴍᴏʀᴇ ᴘʟᴀᴛғᴏʀᴍs ᴠɪᴅᴇᴏ.
"""

# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>

# 🎯 TEXT TO SPEECH COMMANDS
HELP_22 = """ 🔊 <b>TEXT TO SPEECH</b> 🎤

• /tts &lt;text&gt;: Converts the given text to speech in myanmar 🇲🇲
<b>Example:</b>
• /tts မဂ်လာပါ 🙏

<b>Note:</b> Make sure to provide some text after the /tts command ✨ """

# 🔗 INVITE LINK COMMANDS  
HELP_23 = """ 🔗 <b>INVITE LINK COMMANDS</b> 💫

• /givelink: Get the invite link for the current chat 📱
• /link group_id: Get information and generate an invite link for the specified group ID 🆔 """

# 🔒 FORCE SUBSCRIPTION COMMANDS
HELP_24 = """ 🔒 <b>FORCE SUBSCRIPTION COMMANDS</b> 🎯

• /fsub &lt;channel username or id&gt; - Set force subscription for this group 📢
• /fsub off - Disable force subscription for this group ❌ """

# 🧟 ZOMBIE ACCOUNTS
HELP_25 = """ 🧟 <b>ZOMBIE ACCOUNTS</b> 💀

• /zombies - Ban Deleted Accounts 🚫 """

# 👤 USER INFORMATION
HELP_26 = """ 👤 <b>USER INFORMATION</b> 📊

• /info [user_id]: Get detailed information about a user 🔍
• /userinfo [user_id]: Alias for /info 👥 """

# 📁 GITHUB REPOSITORY DOWNLOADER
HELP_27 = """ 📁 <b>GITHUB REPOSITORY DOWNLOADER</b> 🐙

<b>Commands Help:</b> 💻
1. /downloadrepo 📥

<b>Description:</b> Download and retrieve files from a GitHub repository 🗂️
<b>Usage:</b> /downloadrepo [Repo_URL] 🔗
<b>Details:</b>
• Clones the specified GitHub repository 📋
• Creates a zip file of the repository 📦
• Sends the zip file back as a document 📄
• If the download fails, an error message will be displayed ⚠️

<b>Examples:</b>
• /downloadrepo https://github.com/username/repository 🌟 """

# 🎲 TRUTH OR DARE BOT COMMANDS
HELP_28 = """ 🎲 <b>TRUTH OR DARE BOT COMMANDS</b> 🎯

Use these commands to play truth or dare: 🎮
• /truth: Get a random truth question. Answer honestly! 💭
• /dare: Get a random dare challenge. Complete it if you dare! 🔥

<b>Examples:</b>
• /truth: "What is your most embarrassing moment?" 😅
• /dare: "Do 10 push-ups." 💪

<b>Note:</b> If you encounter any issues with fetching questions, please try again later ⏰ """

# 🍃 MONGODB CHECKER
HELP_29 = """ 🍃 <b>MONGODB CHECKER</b> 🔍

• /mongochk [mongo_url]: Checks the validity of a MongoDB URL and connection to the MongoDB instance 🗄️ """

# 🔤 FONT CONVERTER
HELP_30 = """ 🔤 <b>FONT CONVERTER</b> ✨

• /font [text] - Converts simple text to beautiful text by changing its font 🎨 """

# 🤬 GALI COMMANDS
HELP_31 = """ 🤬 <b>GALI COMMANDS</b> 😤

<b>Commands:</b>
• /gali - Send random gali (works in DM) 💢
• .gali - Alternative command format 🔥 """

# 🤖 BOT LIST
HELP_32 = """ 🤖 <b>BOT LIST</b> 🎯

• /bots - Get a list of bots in the group 📋 """

# 📝 MARKDOWN HELP
HELP_33 = """ 📝 <b>MARKDOWN HELP</b> 📖

• /markdownhelp - Help about Markdown 🔧 """

# 🏷️ WISH TAG HELP
HELP_34 = """ 🏷️ <b>WISH TAG HELP</b> 🌟

<b>Good Morning:</b> 🌅
• /gmtag - Start Good Morning tagging ☀️
• /gmstop - Stop Good Morning tagging 🛑

<b>Good Afternoon:</b> 🌞
• /gatag - Start Good Afternoon tagging 🌤️
• /gastop - Stop Good Afternoon tagging 🛑

<b>Good Night:</b> 🌙
• /gntag - Start Good Night tagging 🌜
• /gnstop - Stop Good Night tagging 🛑

<b>Utility:</b> ⚙️
• /stopall - Stop all active tagging 🚫
• /taghelp - Show this help message 📖

<b>Note:</b> Only one tagging session can run per chat at a time 📌 """

HELP_35 = """ <b>Welcome Message</b>
• /welcome on/off: Enable or Disable welcome message .
• /awelcome on/off: Enable or Disable Assistant welcome message ."""

HELP_36 = """ 💑 <b>COUPLE OF THE DAY</b> 💖

• /couple - Selects two random members in the group as today's couple ❤️  
• /couples - Same as /couple, shows today's selected couple 💏

📸 Beautiful framed photo with both DPs will be generated 🖼️  
📅 Next couple will be selected automatically tomorrow ⏳ """

HELP_37 = """🤖 <b>ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇsᴇ ʙᴏᴛs</b> 🤖

🔹 <b>ғᴜɴᴄᴛɪᴏɴ:</b>  
• <b>ʀᴛᴍᴘs sᴛʀᴇᴀᴍɪɴɢ</b> 🎥

🔹 <b>ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ɪs sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ:</b>  

• @SHWEMM_Music2bot – <b>ShweMM music bot</b>  
• @SHWEMM_MUSIC2bot – <b>SHWEMM Mᴜsɪᴄ Bᴏᴛ</b>  

✨ <b>ᴜsᴇ ᴛʜᴇsᴇ ʙᴏᴛs ᴛᴏ ᴇɴᴊᴏʏ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ғᴜʟʟʏ.</b>"""

HELP_38 = """💝 <b>LOVE BIRDS TOOLS</b> 🕊️

🎁 <b>Virtual Gifts:</b>  
• /gifts - <b>ꜱʜᴏᴡ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ɢɪꜰᴛꜱ</b> 🎀  
• /sendgift @user 🌹 - <b>ꜱᴇɴᴅ ᴀ ɢɪꜰᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ</b> 💌  
• /mygifts - <b>ᴠɪᴇᴡ ʏᴏᴜʀ ʀᴇᴄᴇɪᴠᴇᴅ ɢɪꜰᴛꜱ</b> 📥  

💰 <b>Balance & Coins:</b>  
• /balance (or /bal) - <b>ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏɪɴꜱ, ɢɪꜰᴛꜱ ꜱᴇɴᴛ & ʀᴇᴄᴇɪᴠᴇᴅ</b> 💸  
• (auto) - <b>ᴇᴀʀɴ ᴄᴏɪɴꜱ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙʏ ᴄʜᴀᴛᴛɪɴɢ & ᴄʟᴀɪᴍɪɴɢ ɢɪꜰᴛꜱ</b> ✨  

📖 <b>Love Stories:</b>  
• /story Name1 Name2 - <b>ɢᴇɴᴇʀᴀᴛᴇ ᴀ ʀᴀɴᴅᴏᴍ ʀᴏᴍᴀɴᴛɪᴄ ꜱᴛᴏʀʏ</b> 💞  

🏆 <b>Leaderboard:</b>  
• /top (or /leaderboard) - <b>ꜱʜᴏᴡ ʀɪᴄʜᴇꜱᴛ ᴜꜱᴇʀꜱ ᴡɪᴛʜ ᴍᴏꜱᴛ ᴄᴏɪɴꜱ</b> 🏅  

💡 <b>Tips:</b>  
- <b>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ᴇᴀʀɴ ᴄᴏɪɴꜱ</b> 📩  
- <b>ᴄʟᴀɪᴍ ᴘᴇɴᴅɪɴɢ ɢɪꜰᴛꜱ ᴡʜᴇɴ ʏᴏᴜ ᴄʜᴀᴛ</b> 🎁  
- <b>ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ & ᴄʟɪᴍʙ ᴛʜᴇ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ</b> ❤️
"""

HELP_39 = """🎤 <b>VC LOGGER</b> 📢

🔔 <b>Voice Chat Notifications:</b>  
- /vclogger - <b>ᴄʜᴇᴄᴋ ᴠᴄ ʟᴏɢɢᴇʀ ꜱᴛᴀᴛᴜꜱ</b> 📊  
- /vclogger on - <b>ᴇɴᴀʙʟᴇ ᴠᴄ ʟᴏɢɢɪɴɢ</b> ✅  
- /vclogger off - <b>ᴅɪꜱᴀʙʟᴇ ᴠᴄ ʟᴏɢɢɪɴɢ</b> 🚫  

📝 <b>Alternative Commands:</b>  
- /vclogger enable - <b>ᴛᴜʀɴ ᴏɴ ɴᴏᴛɪꜰɪᴄᴀᴛɪᴏɴꜱ</b> 🔊  
- /vclogger disable - <b>ᴛᴜʀɴ ᴏꜰꜰ ɴᴏᴛɪꜰɪᴄᴀᴛɪᴏɴꜱ</b> 🔇  
- /vclogger yes/no - <b>ǫᴜɪᴄᴋ ᴛᴏɢɢʟᴇ</b> ⚡  

✨ <b>Features:</b>  
- <b>ʀᴇᴀʟ-ᴛɪᴍᴇ ᴊᴏɪɴ/ʟᴇᴀᴠᴇ ɴᴏᴛɪꜰɪᴄᴀᴛɪᴏɴꜱ</b> 🎵  
- <b>ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ (10 ꜱᴇᴄ)</b> ⏱️  
- <b>ʀᴀɴᴅᴏᴍ ᴡᴇʟᴄᴏᴍᴇ/ɢᴏᴏᴅʙʏᴇ ᴍᴇꜱꜱᴀɢᴇꜱ</b> 💬  
- <b>ᴘᴇʀꜱɪꜱᴛᴇɴᴛ ꜱᴇᴛᴛɪɴɢꜱ (ꜱᴀᴠᴇᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ)</b> 💾  

💡 <b>Tips:</b>  
- <b>ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴛᴏɢɢʟᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ</b> 👑  
- <b>ᴋᴇᴇᴘꜱ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʟɪᴠᴇʟʏ & ɪɴꜰᴏʀᴍᴇᴅ</b> 🎉  
- <b>ᴡᴏʀᴋꜱ ᴡɪᴛʜ ᴀʟʟ ᴘʀᴇꜰɪxᴇꜱ (., !, /, @, ?, ')</b> 🔧
"""

# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
