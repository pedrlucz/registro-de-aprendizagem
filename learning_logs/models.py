from django.db import models

# o tópico que o usuário vai registrar pra poder inserir as anotações dele sobre aquele tópico
    #tem que herdar o models.model  
    #tabela no banco de dados
class Topic(models.Model):
    """Um assunto sobre qual o usuário está aprendendo"""

    #quero uma coluna chamada text, de tipo texto, com tamanha 200
    text = models.CharField(max_length=200)

    # fazer a data e hora automática
    date_added = models.DateTimeField(auto_now_add=True) # ta falando que vai registrar junto com o text

    def __str__(self): #melhorar a organização no painel adm
        """Devolve uma representção em String do modelo"""
        return self.text #
    

