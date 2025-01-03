from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

# GET É REQUISIÇÃO POR URL, O SERVIDOR TRATA PELA URL E DEVOLVE PRO CLIENTE
# O MÉTODO POST É FEITO POR BAIXO DOS PANOS, VOCÊ NÃO VÊ OS DADOS SENDO PASSADO (requisição e mudança do db), geralmente se usa para os formulários
def new_topic(request):
    """Adiciona um novo assunto"""
    # o request recebe um formulário, quando recebe dados de um formulário, recebe em métodos POST
    # se não for post não passou dado nenhum
    if request.method != 'POST':
        # nenhum dado submetido, cria um formulário em branco
        form = TopicForm() # vai passar o TopicForm() vazio = formulário em branco
    
    else:
        # redirecionar para pág forms
        # dados POST submetidos, processa os dados
        form = TopicForm(request)
        
        # validação de formulário
        if form.is_valid(): # recebe um true e entra no if
            form.save() # ele tem o acesso ao db, ent e suave
            return HttpResponseRedirect(reverse('topics')) # exige uma url pra onde ele vai redirecionar 
                # redirecionamento
                # reverse() utiliza o name para a pag de redirecionamento da que corresponde o name (da urls)
    
    # se entrar no else ele não vai chegar a executar o context nem o return, só vai redirecionar para o 'topics'
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um assunto em particular"""
    topic = Topic.objects.get(id = topic_id) # pegar lá no db
    
    # que você só está clicando
    