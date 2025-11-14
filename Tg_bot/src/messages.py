def start_message(username:str,language:str="en"):
    messages = {
        "ru":f"""
Privet epta {username}!
""",
        "en": f"""
Hello {username}!
    """
    }
    return messages.get(language, messages["en"])

def info_message(language:str="en"):
    messages = {
        "ru":f"""
Napishi che nibud!
""",
        "en": f"""
Write me something!
    """
    }
    return messages.get(language, messages["en"])

def wait_message(language:str="en"):
    messages = {
        "ru":f"""
podozdi ya dumau
""",
        "en": f"""
Wait, im thinking
    """
    }
    return messages.get(language, messages["en"])