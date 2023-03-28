def img_src(func):
    def wrapper(*args, **kwargs):
        return f'{func()}<br><img src="https://media.giphy.com/media/gl8ymnpv4Sqha/giphy.gif">'

    return wrapper


def h_teg(func):
    def wrapper(*args, **kwargs):
        return f'<h1>{func(*args, **kwargs)}</h1>'

    return wrapper


def u_teg(func):
    def wrapper(*args, **kwargs):
        return f'<u>{func(*args, **kwargs)}</u?'


def decorator_project_h_l(func):
    def wrapper_inner(number):
        result = func(number)
        if result == "<h1>You found me!</h1>":
            return f"{result}<br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        elif result == "<h1>Too high, try again!</h1>":
            return f"{result}<br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        else:
            return f"{result}<br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    return wrapper_inner
