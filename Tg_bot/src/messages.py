def start_message(username: str, language: str = "en"):
    messages = {
        "ru": f"""
👋 Добро пожаловать, {username}!

🤖 **Я — AI-помощник Альфа-Банка для вашего бизнеса**

Я здесь, чтобы помочь вам с:
• 📊 Финансовыми расчетами и аналитикой
• ⚖️ Юридическими консультациями  
• 🎯 Маркетинговыми стратегиями
• 📈 Бизнес-планированием
• 💼 Оптимизацией процессов

Просто напишите ваш вопрос — и я подготовлю детальный ответ с учетом специфики вашего бизнеса!

👇 Выберите действие ниже или сразу задайте вопрос
""",
        "en": f"""
👋 Welcome, {username}!

🤖 **I'm Alfa-Bank AI Assistant for your business**

I'm here to help you with:
• 📊 Financial calculations & analytics
• ⚖️ Legal consultations
• 🎯 Marketing strategies  
• 📈 Business planning
• 💼 Process optimization

Just write your question — and I'll prepare a detailed answer considering your business specifics!

👇 Choose an action below or ask your question right away
"""
    }
    return messages.get(language, messages["en"])

def info_message(language: str = "en"):
    messages = {
        "ru": f"""
💡 **Как я могу вам помочь?**

Вы можете спросить меня о:
• Открытии и регистрации бизнеса
• Налоговом планировании и отчетности
• Юридических документах и договорах
• Маркетинговых кампаниях и продвижении
• Финансовых расчетах и аналитике
• Оптимизации бизнес-процессов

🎯 **Просто опишите вашу задачу подробнее — и я дам экспертное решение!**
""",
        "en": f"""
💡 **How can I help you?**

You can ask me about:
• Business registration and setup
• Tax planning and reporting
• Legal documents and contracts
• Marketing campaigns and promotion
• Financial calculations and analytics
• Business process optimization

🎯 **Just describe your task in detail — and I'll provide an expert solution!**
"""
    }
    return messages.get(language, messages["en"])

def main_menu_message(language: str = "en"):
    messages = {
        "ru": f"""
🏠 **Главное меню**

Выберите категорию или просто задайте ваш вопрос:

📋 • Консультация по бизнесу
⚖️ • Юридические вопросы  
📊 • Финансы и аналитика
🎯 • Маркетинг и продажи
📈 • Стратегия и развитие

💬 **Или просто напишите — в чем ваша текущая задача?**
""",
        "en": f"""
🏠 **Main Menu**

Choose a category or just ask your question:

📋 • Business consultation
⚖️ • Legal questions
📊 • Finance & analytics
🎯 • Marketing & sales
📈 • Strategy & development

💬 **Or simply write — what's your current challenge?**
"""
    }
    return messages.get(language, messages["en"])

def wait_message(language: str = "en"):
    messages = {
        "ru": f"""
⏳ **Анализирую ваш запрос...**

🔄 Изучаю бизнес-контекст
📚 Проверяю актуальную информацию  
💡 Формирую оптимальное решение

Пожалуйста, подождите немного ⏱️
""",
        "en": f"""
⏳ **Analyzing your request...**

🔄 Studying business context
📚 Checking relevant information
💡 Forming optimal solution

Please wait a moment ⏱️
"""
    }
    return messages.get(language, messages["en"])