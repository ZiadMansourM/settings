# 👋 Welcome to smart-settings - [docs](https://www.sreboy.com/settings/)
Inspired by [Django](https://github.com/django/django/blob/main/django/conf/__init__.py), smart-settings is a python package that helps you deal with your project settings in a more Pythonic way.

# why smart-settings
- [X] help decouples settings' location from your code
- [X] ability to add default settings
- [X] ability to add modify settings at run time
- [X] thread-safe implementation
- [ ] ability to save settings modified at run time
- [ ] JSON/YAML support
- [ ] Duplicate check

# Run Example with:
```python
python app.py --setting=config.settings
```

# Project Structure Example:
```
project
│
│  
│
└───config
│   __init__.py
│   settings.py
│
│   
└───smart_settings
|   __init__.py
|   core.py
| 
│
└───app.py
```
