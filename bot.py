from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scraper import scrape_aliexpress

BOT_TOKEN = "7805938395:AAG1fSoESDTRwi__PxOFkAfHDmrg3oaM43I"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل /search متبوع بالكلمة (مثال: /search phone)")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⛔ أكتب: /search الكلمة")
        return

    query = " ".join(context.args)
    await update.message.reply_text(f"🔍 كنجبد نتائج لـ: {query}...")

    results = scrape_aliexpress(query)
    if not results:
        await update.message.reply_text("😔 ما لقيتش نتائج.")
        return

    for p in results:
        msg = f"🛒 {p['title']}\n💵 {p['price']}\n🔗 {p['link']}"
        await update.message.reply_text(msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("search", search))

if __name__ == "__main__":
    app.run_polling()
