from .UsuarioBanco import UsuarioBanco

def authenticate(usnm, passw):
    usbd = UsuarioBanco()
    us = (usnm, passw)
    result = usbd.authenticate(us)
    if(result):
        return True
    return False


