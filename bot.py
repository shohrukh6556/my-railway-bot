import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


# Главное меню
main_menu = [
    [KeyboardButton("🧠 Английский"), KeyboardButton("👨‍💻 Профессии")],
    [KeyboardButton("📘 Книги"), KeyboardButton("🧩 Квизы")]
]

# ===== Команда /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Что хочешь делать сегодня?",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# ===== Обработка выбора =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🧠 Английский":
        await update.message.reply_text("Например: cat = кошка\nХотите пройти тест? Нажмите /quiz")
    elif text == "👨‍💻 Профессии":
        await update.message.reply_text("Выберите профессию: 👩‍🎨 Дизайнер, 👨‍💻 Программист\n(будет 5 бесплатных уроков)")
    elif text == "📘 Книги":
        await update.message.reply_text("Жанры: 📖 Фантастика, 🔍 Детектив, ❤️ Романтика")
    elif text == "🧩 Квизы":
        await update.message.reply_text("Начнем квиз! Вопрос 1:\n🐱 = ?\nA) Cat\nB) Dog\nC) Cow")
    else:
        await update.message.reply_text("Выберите действие из меню ниже ↓")

# ===== Пример команды /quiz =====
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Тест на перевод:\nWhat is the Russian for 'apple'?\nA) Апельсин\nB) Яблоко\nC) Банан")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == "__main__":
    main()
