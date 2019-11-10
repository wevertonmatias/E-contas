from django import forms
from .models import *
from django.views.generic import View


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = ['nome_fantasia']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data_evento', 'hora_evento',
                  'categoria_evento', 'realizado']

class CategoriaEventoForm(forms.ModelForm):
    class Meta:
        model = CategoriaEvento
        fields = ['descricao']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'nome_fantasia', 'cnpj_cpf', 'telefone']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['descricao', 'sigla']

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['descricao', 'estado']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'bairro', 'cep', 'cidade', 'estado']


