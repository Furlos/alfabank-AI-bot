def start_message(username:str,language:str="en"):
    messages = {
        "ru":f"""
Привет! {username}, (тут тоже че то надо думаю)!
""",
        "en": f"""
Hello {username}!
    """
    }
    return messages.get(language, messages["en"])

def info_message(language:str="en"):
    messages = {
        "ru":f"""
Напишите ваш запрос!
""",
        "en": f"""
Write me something!
    """
    }
    return messages.get(language, messages["en"])

def main_menu_message(language:str="en"):
    messages = {
        "ru":f"""
Мы в главном меню, что дальше?
""",
        "en": f"""
Back to the main menu. What should we ask now?
    """
    }
    return messages.get(language, messages["en"])

def wait_message(language:str="en"):
    messages = {
        "ru":f"""
Идет процесс осмысления...
""",
        "en": f"""
Wait, im thinking
    """
    }
    return messages.get(language, messages["en"])