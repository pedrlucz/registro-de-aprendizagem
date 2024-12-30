from django.contrib import admin
from learning_logs.models import Topic, Entry

# preciso importar aqui pra dentro os modelos que quero no meu painel de admin

admin.site.register(Topic) # não pode passar as duas classes aqui
admin.site.register(Entry)
