from .add import add
from .dell import dell
from .upd import upd

all_operations = {'add': add, 'del': dell, 'upd': upd}

__all__ = ['all_operations']