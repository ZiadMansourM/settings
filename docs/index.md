## π Welcome to smart-settings
Inspired by [Django](https://github.com/django/django/blob/main/django/conf/__init__.py),smart-settings is a python package that helps you deal with your project settings in a more Pythonic way.

## Why smart-settings
- [X] help decouples settings' location from your code
- [X] ability to add default settings
- [X] ability to add modify settings at run time
- [X] thread-safe implementation
- [ ] ability to add save settings modified at run time
- [ ] JSON/YAML support
- [ ] Duplicate check

## Run Example with
```python
python app.py --setting=config.settings
```

## Project Structure Example
```
project
β
β  
β
ββββconfig
β   __init__.py
β   settings.py
β
β   
ββββsmart_settings
|   __init__.py
|   core.py
| 
β
ββββapp.py
```