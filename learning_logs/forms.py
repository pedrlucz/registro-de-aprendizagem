from django import forms
from .models import Topic, Entry

# formulário
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # desse jeito o campo vem vazio pra ser preenchido

# entradas / anotações
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text'] # o único que vai aparecer pra preencher
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs = {'cols':80})} # por exemplo o de cima é um retângulo, só pros tópicos
        # quero mudar o text para Textarea(), attrs = alguns atributos que pode passar pro Textarea, como por exemplo coluna