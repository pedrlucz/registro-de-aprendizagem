from django.shortcuts import render

def index(request):
    """Página principal"""

    # ele tem que o conteúdo da função jogar para uma página html que vai ser renderizada na tela
    # o return pega tudo que ta sendo trabalhado na função, envia para uma página html que vai ser enviada para o usuário
    return render(request, 'learning_logs/index.html')
            # o render já procura uma pasta chamada templates, ai depois procura o leraning...
