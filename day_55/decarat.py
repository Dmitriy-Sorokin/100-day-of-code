def img_src(func):
    def wrapper(*args, **kwargs):
        return f'{func()}<br><img src="https://media.giphy.com/media/gl8ymnpv4Sqha/giphy.gif">'

    return wrapper


def h_teg(func):
    def wrapper(*args, **kwargs):
        return f'<h1>{func(*args, **kwargs)}</h1?'

    return wrapper


def u_teg(func):
    def wrapper(*args, **kwargs):
        return f'<u>{func(*args, **kwargs)}</u?'

    return wrapper
