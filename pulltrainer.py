import os
from unicodedata import name
os.environ.setdefault("DJANGO_SETTINGS_MODULE","nugudjango.settings")
import django
django.setup()
                                
from nuguhome.models import trainer,gymlocation

b = trainer(name='ㅅㅇㅈ',gym='에이블짐',id=1)
print(b.id)