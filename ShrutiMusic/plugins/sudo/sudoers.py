from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from ShrutiMusic import app
from ShrutiMusic.misc import SUDOERS
from ShrutiMusic.utils.database import add_sudo, remove_sudo
from ShrutiMusic.utils.decorators.language import language
from ShrutiMusic.utils.extraction import extract_user
from ShrutiMusic.utils.inline import close_markup
from ShrutiMusic.utils.functions import DevID
from config import BANNED_USERS, OWNER_ID


def can_use_owner_commands(user_id):
    return user_id == OWNER_ID or user_id == DevID


@app.on_message(filters.command(["addsudo"]) & filters.user([OWNER_ID, DevID]))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user([OWNER_ID, DevID]))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["deleteallsudo", "clearallsudo", "removeallsudo"]) & filters.user([OWNER_ID, DevID]))
@language
async def delete_all_sudoers(client, message: Message, _):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Yes, Delete All", callback_data="confirm_delete_all_sudo"),
            InlineKeyboardButton("❌ Cancel", callback_data="cancel_delete_all_sudo")
        ]
    ])
    
    sudo_count = len([user_id for user_id in SUDOERS if user_id != OWNER_ID])
    
    if sudo_count == 0:
        return await message.reply_text("❌ <b>No sudoers found to delete!</b>")
    
    await message.reply_text(
        f"⚠️ <b>Warning!</b>\n\n"
        f"Are you sure you want to delete all <code>{sudo_count}</code> sudoers?\n\n"
        f"<i>This action cannot be undone!</i>",
        reply_markup=keyboard
    )


@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    if not can_use_owner_commands(message.from_user.id) and message.from_user.id not in SUDOERS:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔒 View Sudolist", callback_data="view_sudolist_unauthorized")]
        ])
        await message.reply_text(
            "🔒 <b>Access Restricted</b>\n\n"
            "Only Owner and Sudoers can check the sudolist.",
            reply_markup=keyboard
        )
        return
    
    text = _["sudo_5"]
    try:
        user = await app.get_users(OWNER_ID)
        user_mention = user.first_name if not user.mention else user.mention
        text += f"1➤ {user_mention} <code>{OWNER_ID}</code>\n"
    except:
        text += f"1➤ Owner <code>{OWNER_ID}</code>\n"
    
    sudo_count = 0
    sudo_text = ""
    
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user_mention = user.first_name if not user.mention else user.mention
                sudo_count += 1
                sudo_text += f"{sudo_count + 1}➤ {user_mention} <code>{user_id}</code>\n"
            except:
                sudo_count += 1
                sudo_text += f"{sudo_count + 1}➤ Unknown User <code>{user_id}</code>\n"
                continue
    
    if sudo_count > 0:
        text += _["sudo_6"]
        text += sudo_text
    else:
        text += "\n<b>No sudoers found.</b>"
    
    await message.reply_text(text, reply_markup=close_markup(_))


@app.on_callback_query(filters.regex("confirm_delete_all_sudo"))
async def confirm_delete_all_sudoers(client, callback_query: CallbackQuery):
    if not can_use_owner_commands(callback_query.from_user.id):
        return await callback_query.answer("❌ Only owner can do this!", show_alert=True)
    
    deleted_count = 0
    sudoers_to_remove = [user_id for user_id in SUDOERS.copy() if user_id != OWNER_ID]
    
    for user_id in sudoers_to_remove:
        try:
            removed = await remove_sudo(user_id)
            if removed:
                SUDOERS.discard(user_id)
                deleted_count += 1
        except:
            continue
    
    if deleted_count > 0:
        await callback_query.edit_message_text(
            f"✅ <b>Successfully deleted all sudoers!</b>\n\n"
            f"📊 <b>Deleted:</b> <code>{deleted_count}</code> users\n"
            f"🛡️ <b>Protected:</b> Owner remains safe"
        )
    else:
        await callback_query.edit_message_text("❌ <b>Failed to delete sudoers!</b>\n\nTry again later.")


@app.on_callback_query(filters.regex("cancel_delete_all_sudo"))
async def cancel_delete_all_sudoers(client, callback_query: CallbackQuery):
    await callback_query.edit_message_text("❌ <b>Cancelled!</b>\n\nNo sudoers were deleted.")


@app.on_callback_query(filters.regex("view_sudolist_unauthorized"))
async def unauthorized_sudolist_callback(client, callback_query: CallbackQuery):
    await callback_query.answer(
        "🚫 Access Denied!\n\nOnly Owner and Sudoers can check sudolist.", 
        show_alert=True
    )
