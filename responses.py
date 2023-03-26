import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1,10))

    if p_message == 'dance':
        return '💃'

    if p_message == 'help':
        return 'help help'

    if p_message == 'most beautiful person':
        return 'Muhammad'

    return 'i dont understand what are you writing'