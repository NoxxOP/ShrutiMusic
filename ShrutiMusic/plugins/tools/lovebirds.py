import random
from pyrogram import filters
from ShrutiMusic import app
from ShrutiMusic.core.mongo import mongodb
from config import MONGO_DB_URI

lovebirds_db = mongodb.lovebirds
users_collection = lovebirds_db.users
gifts_collection = lovebirds_db.gifts

GIFTS = {
    "🌹": {"name": "Rose", "cost": 10, "emoji": "🌹"},
    "🍫": {"name": "Chocolate", "cost": 20, "emoji": "🍫"},
    "🧸": {"name": "Teddy Bear", "cost": 30, "emoji": "🧸"},
    "💍": {"name": "Ring", "cost": 50, "emoji": "💍"},
    "❤️": {"name": "Heart", "cost": 5, "emoji": "❤️"},
    "🌺": {"name": "Flower Bouquet", "cost": 25, "emoji": "🌺"},
    "💎": {"name": "Diamond", "cost": 100, "emoji": "💎"},
    "🎀": {"name": "Gift Box", "cost": 40, "emoji": "🎀"},
    "🌙": {"name": "Moon", "cost": 35, "emoji": "🌙"},
    "⭐": {"name": "Star", "cost": 15, "emoji": "⭐"},
    "🦋": {"name": "Butterfly", "cost": 18, "emoji": "🦋"},
    "🕊️": {"name": "Dove", "cost": 22, "emoji": "🕊️"},
    "🏰": {"name": "Castle", "cost": 80, "emoji": "🏰"},
    "🎂": {"name": "Cake", "cost": 28, "emoji": "🎂"},
    "🍓": {"name": "Strawberry", "cost": 12, "emoji": "🍓"}
}

async def get_user_data(user_id):
    try:
        user_data = await users_collection.find_one({"user_id": user_id})
        if not user_data:
            new_user = {
                "user_id": user_id,
                "coins": 50,
                "total_gifts_received": 0,
                "total_gifts_sent": 0,
                "created_at": "2025"
            }
            await users_collection.insert_one(new_user)
            return new_user
        return user_data
    except:
        return {"user_id": user_id, "coins": 0, "total_gifts_received": 0, "total_gifts_sent": 0}

async def update_user_coins(user_id, amount):
    try:
        await users_collection.update_one(
            {"user_id": user_id},
            {"$inc": {"coins": amount}},
            upsert=True
        )
    except:
        pass

async def get_user_gifts(user_id, gift_type="received"):
    try:
        if gift_type == "received":
            gifts = await gifts_collection.find({"receiver_id": user_id}).to_list(length=None)
        else:
            gifts = await gifts_collection.find({"sender_id": user_id}).to_list(length=None)
        return gifts
    except:
        return []

def get_user_info(message):
    try:
        if not message.from_user:
            return None, None
        user_id = message.from_user.id
        username = message.from_user.username or message.from_user.first_name
        return user_id, username
    except:
        return None, None

@app.on_message(filters.command(["balance", "bal"], prefixes=["/", "!", "."]))
async def balance(_, message):
    try:
        uid, username = get_user_info(message)
        if not uid:
            return
        
        user_data = await get_user_data(uid)
        
        coins = user_data["coins"]
        gifts_received = await gifts_collection.count_documents({"receiver_id": uid})
        gifts_sent = await gifts_collection.count_documents({"sender_id": uid})
        
        balance_text = f"""
💰 <b>{username}'s Account</b>
💸 <b>Balance:</b> {coins} coins
🎁 <b>Gifts Received:</b> {gifts_received}
📤 <b>Gifts Sent:</b> {gifts_sent}

💡 <b>Tip:</b> Send messages to earn coins!
        """
        await message.reply_text(balance_text)
    except:
        pass

@app.on_message(filters.command("gifts", prefixes=["/", "!", "."]))
async def gift_list(_, message):
    try:
        text = "🎁 <b>Available Gifts:</b>\n\n"
        sorted_gifts = sorted(GIFTS.items(), key=lambda x: x[1]["cost"])
        
        for emoji, gift_info in sorted_gifts:
            text += f"{emoji} <b>{gift_info['name']}</b> - {gift_info['cost']} coins\n"
        
        text += "\n📝 <b>Usage:</b> /sendgift @username GiftEmoji"
        text += "\n💡 <b>Example:</b> /sendgift @john 🌹"
        
        await message.reply_text(text)
    except:
        pass

@app.on_message(filters.command("sendgift", prefixes=["/", "!", "."]))
async def send_gift(_, message):
    try:
        parts = message.text.split(" ")
        if len(parts) < 3:
            return await message.reply_text("❌ <b>Usage:</b> /sendgift @username GiftEmoji\n💡 <b>Example:</b> /sendgift @john 🌹")
        
        target = parts[1].replace("@", "")
        gift_emoji = parts[2]
        
        sender_id, sender_name = get_user_info(message)
        if not sender_id:
            return
        
        sender_data = await get_user_data(sender_id)
        
        if gift_emoji not in GIFTS:
            return await message.reply_text("❌ <b>Invalid gift!</b> Use /gifts to see available gifts.")
        
        gift_info = GIFTS[gift_emoji]
        cost = gift_info["cost"]
        
        if sender_data["coins"] < cost:
            return await message.reply_text(f"😢 <b>Insufficient coins!</b>\n💰 You need {cost} coins but have {sender_data['coins']} coins.")
        
        await users_collection.update_one(
            {"user_id": sender_id},
            {"$inc": {"coins": -cost, "total_gifts_sent": 1}}
        )
        
        gift_record = {
            "sender_id": sender_id,
            "sender_name": sender_name,
            "receiver_name": target,
            "receiver_id": None,
            "gift_name": gift_info["name"],
            "gift_emoji": gift_emoji,
            "cost": cost,
            "timestamp": "2025",
            "claimed": False
        }
        
        await gifts_collection.insert_one(gift_record)
        updated_sender = await get_user_data(sender_id)
        
        success_msg = f"""
🎉 <b>Gift Sent Successfully!</b>

{gift_emoji} <b>{sender_name}</b> sent <b>{gift_info['name']}</b> to <b>@{target}</b>!

💝 <b>Gift Details:</b>
• <b>Gift:</b> {gift_emoji} {gift_info['name']}
• <b>Cost:</b> {cost} coins
• <b>From:</b> {sender_name}
• <b>To:</b> @{target}

💰 <b>{sender_name}'s remaining coins:</b> {updated_sender['coins']}

💕 <i>Love is in the air!</i>
        """
        
        await message.reply_text(success_msg)
    except:
        pass

async def claim_pending_gifts(user_id, username):
    try:
        pending_gifts = await gifts_collection.find({
            "receiver_name": username,
            "claimed": False
        }).to_list(length=None)
        
        if pending_gifts:
            total_bonus = 0
            gift_count = len(pending_gifts)
            
            for gift in pending_gifts:
                await gifts_collection.update_one(
                    {"_id": gift["_id"]},
                    {
                        "$set": {
                            "receiver_id": user_id,
                            "claimed": True
                        }
                    }
                )
                total_bonus += 5
            
            await users_collection.update_one(
                {"user_id": user_id},
                {"$inc": {"coins": total_bonus, "total_gifts_received": gift_count}}
            )
            
            return gift_count, total_bonus
        
        return 0, 0
    except:
        return 0, 0

@app.on_message(filters.command("story", prefixes=["/", "!", "."]))
async def love_story(_, message):
    try:
        parts = message.text.split(" ", 2)
        if len(parts) < 3:
            return await message.reply_text("❌ <b>Usage:</b> /story Name1 Name2\n💡 <b>Example:</b> /story Raj Priya")
        
        name1, name2 = parts[1], parts[2]
        
        stories = [
            f"Once upon a time, <b>{name1}</b> met <b>{name2}</b> at a coffee shop ☕. Their eyes met over steaming cups, and destiny wrote their love story ❤️✨",
            f"In a crowded library 📚, <b>{name1}</b> and <b>{name2}</b> reached for the same book. Their fingers touched, and sparks flew like magic 💫💕",
            f"<b>{name1}</b> was walking in the rain 🌧️ when <b>{name2}</b> offered an umbrella ☂️. Under that shared shelter, love bloomed like flowers after rain 🌸",
            f"At a music concert 🎵, <b>{name1}</b> and <b>{name2}</b> found themselves singing the same song. Their voices harmonized, and so did their hearts 🎶❤️",
            f"<b>{name1}</b> was lost in a new city 🏙️ when <b>{name2}</b> offered directions. They walked together and found not just the way, but each other 💝",
            f"In a beautiful garden 🌺, <b>{name1}</b> was admiring roses when <b>{name2}</b> appeared like a dream. Together they made the garden even more beautiful 🌹✨",
            f"<b>{name1}</b> dropped their books 📖, and <b>{name2}</b> helped pick them up. In that simple moment, they discovered they were reading the same love story 💘",
            f"At the beach during sunset 🌅, <b>{name1}</b> and <b>{name2}</b> built sandcastles 🏰. Their hearts built something even stronger - eternal love 💞",
            f"<b>{name1}</b> was feeding birds in the park 🐦 when <b>{name2}</b> joined with more breadcrumbs. Together they created a symphony of chirping and laughter 🎭💕",
            f"During a power outage 🕯️, <b>{name1}</b> and <b>{name2}</b> shared stories by candlelight. In that darkness, they found their brightest light - each other ✨❤️",
            f"<b>{name1}</b> was painting a sunset 🎨 when <b>{name2}</b> said it was beautiful. But <b>{name1}</b> replied, 'Not as beautiful as you' 😍💝",
            f"At a dance class 💃, <b>{name1}</b> had two left feet, but <b>{name2}</b> was a patient teacher. They danced into each other's hearts 🕺❤️",
            f"<b>{name1}</b> rescued a kitten 🐱, and <b>{name2}</b> helped find it a home. In saving the kitten, they found their own forever home - in each other's arms 🏠💕",
            f"During a cooking class 👨‍🍳, <b>{name1}</b> burned the food, but <b>{name2}</b> said it tasted like love. Sometimes the best recipes come from the heart 💝🍳",
            f"<b>{name1}</b> and <b>{name2}</b> were both reaching for the last piece of chocolate 🍫. They decided to share it, and ended up sharing their whole lives 💍✨",
            f"At the train station 🚂, <b>{name1}</b> was about to board when <b>{name2}</b> ran through the crowd shouting 'Wait!' That's when they knew - love conquers all ❤️🏃‍♂️",
            f"<b>{name1}</b> was star-gazing alone 🌟 when <b>{name2}</b> appeared with a telescope. Together they discovered that the most beautiful constellation was their intertwined fingers 👫✨",
            f"During a baking disaster 🧁, <b>{name1}</b> covered the kitchen in flour. <b>{name2}</b> laughed and joined the mess. Sometimes love is messy, but it's always sweet 💕👫",
            f"<b>{name1}</b> wrote a letter to the universe 📝 asking for true love. <b>{name2}</b> found that letter and became the answer to every prayer 🙏💝",
            f"At a farmers market 🍎, <b>{name1}</b> and <b>{name2}</b> both reached for the last apple. They decided to share it, and ended up sharing a lifetime of sweetness 🍯❤️"
        ]
        
        story = random.choice(stories)
        
        endings = [
            "\n\n💕 <i>And they lived happily ever after...</i>",
            "\n\n❤️ <i>True love always finds a way...</i>",
            "\n\n💞 <i>Some people search their whole lives for what they found in each other...</i>",
            "\n\n✨ <i>In a world full of chaos, they found peace in each other...</i>",
            "\n\n💝 <i>Love isn't finding someone perfect, it's finding someone perfect for you...</i>",
            "\n\n🌹 <i>Every love story is beautiful, but theirs was their favorite...</i>",
            "\n\n💫 <i>Love is not about finding the right person, but being the right person for someone...</i>"
        ]
        
        story += random.choice(endings)
        
        romantic_header = random.choice([
            "💕 <b>Love Story</b> 💕",
            "❤️ <b>Tale of Love</b> ❤️", 
            "💞 <b>Romance Story</b> 💞",
            "✨ <b>Love Chronicles</b> ✨",
            "🌹 <b>Romantic Tale</b> 🌹"
        ])
        
        final_story = f"{romantic_header}\n\n{story}"
        await message.reply_text(final_story)
        
        uid, _ = get_user_info(message)
        if uid:
            await update_user_coins(uid, 5)
    except:
        pass

@app.on_message(filters.command(["mygifts", "received"], prefixes=["/", "!", "."]))
async def my_gifts(_, message):
    try:
        uid, username = get_user_info(message)
        if not uid:
            return
        
        await get_user_data(uid)
        
        gifts_received = await gifts_collection.find({"receiver_id": uid}).to_list(length=10)
        
        if not gifts_received:
            await message.reply_text(f"📭 <b>{username}</b>, you haven't received any gifts yet!\n💡 Ask someone to send you gifts using /sendgift")
            return
        
        gifts_text = f"🎁 <b>{username}'s Received Gifts:</b>\n\n"
        
        for i, gift in enumerate(gifts_received, 1):
            gifts_text += f"{i}. {gift['gift_emoji']} <b>{gift['gift_name']}</b> from <b>{gift['sender_name']}</b>\n"
        
        total_gifts = await gifts_collection.count_documents({"receiver_id": uid})
        gifts_text += f"\n💝 <b>Total gifts received:</b> {total_gifts}"
        
        await message.reply_text(gifts_text)
    except:
        pass

@app.on_message(filters.command(["top", "leaderboard"], prefixes=["/", "!", "."]))
async def leaderboard(_, message):
    try:
        top_users = await users_collection.find().sort("coins", -1).limit(10).to_list(length=10)
        
        if not top_users:
            await message.reply_text("📊 No users found in leaderboard!")
            return
        
        leaderboard_text = "🏆 <b>Top 10 Richest Users</b>\n\n"
        medals = ["🥇", "🥈", "🥉"] + ["🏅"] * 7
        
        for i, user in enumerate(top_users):
            medal = medals[i] if i < len(medals) else "🏅"
            leaderboard_text += f"{medal} <b>User {user['user_id']}</b> - {user['coins']} coins\n"
        
        await message.reply_text(leaderboard_text)
    except:
        pass

@app.on_message(filters.text & ~filters.regex(r"^[/!.\-]"))
async def give_coins_and_claim_gifts(_, message):
    try:
        uid, username = get_user_info(message)
        if not uid:
            return
        
        await get_user_data(uid)
        
        gift_count, bonus_coins = await claim_pending_gifts(uid, username)
        
        if gift_count > 0:
            claim_msg = f"""
🎁 <b>Gifts Claimed!</b>

<b>{username}</b>, you received <b>{gift_count}</b> pending gifts!
💰 <b>Bonus coins earned:</b> {bonus_coins} coins

Use /mygifts to see your received gifts! 💝
            """
            await message.reply_text(claim_msg)
        
        if random.randint(1, 100) <= 20:
            await update_user_coins(uid, 1)
    except:
        pass
