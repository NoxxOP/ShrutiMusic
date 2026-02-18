from typing import List, Optional, Union

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import ChatPrivileges, Message

from ShrutiMusic import app
from ShrutiMusic.core.call import Nand
from ShrutiMusic.utils.database import get_assistant, set_loop
from ShrutiMusic.utils.permissions import adminsOnly

other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.via_bot & ~filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")


@app.on_message(filters.video_chat_started & filters.group)
async def on_vc_start(_, msg):
    chat_id = msg.chat.id
    try:
        await msg.reply("<b>🤍 ᴠɪᴅᴇᴏ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ 🤍\n\n🙄 `ⁱᶠ ᵗʰᵉ ˢᵒⁿᵍ ᵈᵒᵉˢⁿ'ᵗ ᵖˡᵃʸ, ᵖˡᵉᵃˢᵉ ᵃˢᵏ ᶠᵒʳ ʰᵉˡᵖ = @HANTHAR999 { 🇲🇲 }</b>")
        # Remove st_stream call from here - it's causing the error
        await set_loop(chat_id, 0)
    except Exception as e:
        await msg.reply(f"<b>ᴇʀʀᴏʀ:</b> <code>{e}</code>")


async def get_group_call(client: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await assistant.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply(f"<b>No group voice chat found</b> {err_msg}")
    return False


@app.on_message(filters.command(["vcstart", "startvc"], ["/", "!"]))
@adminsOnly("can_manage_video_chats")
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    
    if assistant is None:
        await m.reply("<b>Error:</b> Assistant not found!")
        return
    
    ass = await assistant.get_me()
    assid = ass.id

    msg = await m.reply("<b>Starting the Voice Chat...</b>")
    
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("<b>🎧 Voice Chat Started Successfully 🤍</b>")
        await set_loop(chat_id, 0)

    except ChatAdminRequired:
        try:
            await app.promote_chat_member(
                chat_id,
                assid,
                privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=True,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                ),
            )

            peer = await assistant.resolve_peer(chat_id)
            await assistant.invoke(
                CreateGroupCall(
                    peer=InputPeerChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash,
                    ),
                    random_id=assistant.rnd_id() // 9000000000,
                )
            )

            await app.promote_chat_member(
                chat_id,
                assid,
                privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                ),
            )

            await msg.edit_text("<b>🎧 Voice Chat Started Successfully 🤍</b>")
            await set_loop(chat_id, 0)
            
        except Exception as e:
            await msg.edit_text(f"<b>❌ Give the bot full permissions and try again.</b>\n<code>{e}</code>")


@app.on_message(filters.command(["vcend", "endvc"], ["/", "!"]))
@adminsOnly("can_manage_video_chats")
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    
    if assistant is None:
        await m.reply("<b>Error:</b> Assistant not found!")
        return
    
    ass = await assistant.get_me()
    assid = ass.id

    msg = await m.reply("<b>Closing the Voice Chat...</b>")
    
    try:
        group_call = await get_group_call(assistant, m, err_msg=", Voice Chat Already Ended")
        if not group_call:
            await msg.delete()
            return
            
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("<b>🎧 Voice Chat Closed Successfully 🤍</b>")
        await set_loop(chat_id, 0)

    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            try:
                await app.promote_chat_member(
                    chat_id,
                    assid,
                    privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=True,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ),
                )
                
                group_call = await get_group_call(assistant, m, err_msg=", Voice Chat Already Ended")
                if not group_call:
                    await msg.delete()
                    return
                    
                await assistant.invoke(DiscardGroupCall(call=group_call))
                
                await app.promote_chat_member(
                    chat_id,
                    assid,
                    privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ),
                )
                
                await msg.edit_text("<b>🎧 Voice Chat Closed Successfully 🤍</b>")
                await set_loop(chat_id, 0)
                
            except Exception as ex:
                await msg.edit_text(f"<b>😡 Give the bot full permissions and try again.</b>\n<code>{ex}</code>")
        else:
            await msg.edit_text(f"<b>Error:</b> <code>{e}</code>")
