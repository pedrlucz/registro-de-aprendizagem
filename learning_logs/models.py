from django.db import models

# o tópico que o usuário vai registrar pra poder inserir as anotações dele sobre aquele tópico
    #tem que herdar o models.model  
    #tabela no banco de dados
class Topic(models.Model):
    """Um assunto sobre qual o usuário está aprendendo"""

    #quero uma coluna chamada text, de tipo texto, com tamanha 200
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True) # registra junto com o text a hora automática

    def __str__(self): #melhorar a organização no painel adm
        """Devolve uma representção em String do modelo"""
        return self.text #
        
# pra cada tópico várias anotações

# entry porque? to entrando com uma determinada anotação 
class Entry(models.Model):
    """Algo específico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # cada entrada eu tenho um tópico relacionado
    # on delete signifique que vai falar pro db, quando excluir um tópico, precisa excluir todas as entradas que estão relacionadas com esse tópico
    # o texto que vai ser a anotação
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        #quando o django quiser utilizar o Entry no plural, ele use 'entries'
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Devolve uma string do modelo"""
        return self.text[:50] + '...'

