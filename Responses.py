import random

def get_response(message: str) -> str:
    p_message - message.lower()

    if p_message == 'hello':
        return 'Hello you wild animal'
    
    if message == 'roll':
        return str(random.randint(1,20))
    
    if p_message == '?help':
        return 'This is work in progress'
    
    return 'I didn\'t catch that please try "?help".'