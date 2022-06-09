import importlib
import sys
import threading

class SingletonMeta(type):
    """This is a thread-safe implementation of the Singleton"""

    _lock: threading.Lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        super(SingletonMeta, self).__init__(*args, **kwargs)
        self._instance = None
    
    def __call__(self, *args, **kwargs):
        with self._lock:
            if self._instance is None:
                self._instance = super(SingletonMeta, self).__call__(*args, **kwargs)
        return self._instance


class _Settings(metaclass=SingletonMeta):
    """ This Class Mimics Django's way of dealling with settings 
    configuration in runtime Safely

    More information:
        https://github.com/django/django/blob/main/django/conf/__init__.py
    """
    def __init__(self):
        self._dict = {}
        self._setup()

    def _setup(self):
        self._settings_module = self._get_settings_from_cmd_line()
        if not self._settings_module:
            raise RuntimeError('Settings are not configured')
        self._load_settings_module()

    def _get_settings_from_cmd_line(self):
        for argument in sys.argv:
            if argument.startswith("--setting"):
                try:
                    return argument.split("=")[1]
                except IndexError:
                    return None

    def _load_settings_module(self):
        module = importlib.import_module(self._settings_module)
        self._dict = {setting: getattr(module, setting) 
            for setting in dir(module)
            if setting.isupper() and not setting.startswith("_")
        }

    def __getattr__(self, attr):
        try:
            return self._dict[attr]
        except KeyError as e:
            raise AttributeError(f"You did not set {attr} setting") from e

    def as_dict(self):
        return self._dict.copy()


settings = _Settings()