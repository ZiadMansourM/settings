"""Simulates an Application that uses settings"""
from smart_settings import settings


print(list(settings.as_dict().keys())) # ['DB_PASSWORD', 'DB_USER']

print(settings.DB_USER) # ZIADMANSOUR

"""When you try to access a SETTING that
doesn't exist in "config/settings"
an AttributeError Exception will be raised
"""
# print(settings.DEBUG) # AttributeError: You did not set DEBUG setting