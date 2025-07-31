from django.db import models

# Create your models here.
'''
TO DO:
    Descrição
    Data de criação
    Prioridade: Alta, Média e Baixa
    Status: A fazer/ Em Andamento / Concluída
'''

class Tarefa(models.Model):
    OPCOES_STATUS = (
        ('concluido', 'Concluído'),
        ('em_andamento', 'Em Andamento'),
        ('pendente', 'Pendente'),
    )

    OPCOES_PRIORIDADE = (
        ('alta', 'Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'), 
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    prioridade = models.CharField(max_length=25, choices=OPCOES_PRIORIDADE, default='baixa')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')