from django.shortcuts import render
from .models import Topic

def index(request):
    """Página principal"""

    # ele tem que o conteúdo da função jogar para uma página html que vai ser renderizada na tela
    # o return pega tudo que ta sendo trabalhado na função, envia para uma página html que vai ser enviada para o usuário
    return render(request, 'learning_logs/index.html')
            # o render já procura uma pasta chamada templates, ai depois procura o leraning...

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added') # to pegando o objeto dentro de topic (o que ta dentro do db), ai eu quero ordenar ele por date_added
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas"""
    
    # vou passar na url o id, que vai vir pra view, e ela vai receber esse id e pesquisar se existe algum registro com esse id
    topic = Topic.objects.get(id = topic_id) #pra receber o tópico específico que eu quero, com o get eu aviso que só quero um, e nele eu falo qual atributo que eu quero resgatar
    entries = topic.entry_set.order_by('-data_added') #buscar o mais recente 
                    # entry_set pra fazer uma busca no db, e o order_by pra ordenar essa busca
    context = {'topic': topic,
               'entries': entries
               } # o contexto pra jogar no template, na pag
    
    return render(request, 'learning_logs/topic.html', context)
