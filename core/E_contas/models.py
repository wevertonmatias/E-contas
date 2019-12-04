from collections import defaultdict

from django.db import models

# Create your models here.
from django.template.defaultfilters import default

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False)
    cnpj_cpf = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=False, blank=False)
    tipo_de_parceria = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.razao_social

class Empresa(models.Model):
    razao_social = models.CharField(max_length=255, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False)
    cnpj_cpf = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.razao_social

class LocalRecebimento(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    adm_cartao = models.CharField(max_length=255, null=False, blank=False)
    bandeira_cartao = models.CharField(max_length=255, null=False, blank=False)
    modo_pagamento = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.titulo

class Venda(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    parcelas = models.IntegerField(null=False, blank=False)
    data = models.DateField(max_length=255, null=False, blank=False)
    local_de_recebimento = models.ForeignKey(LocalRecebimento, on_delete="SET_NULL", null=False, blank=False)
    empresa = models.ForeignKey(Empresa, on_delete="SET_NULL", null=False, blank=False)

    def __str__(self):
        return "R${} - Data:{} - Local de Recebimento:{}".format(self.valor, self.data, self.local_de_recebimento)


class TipoPagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao

class StatusDoPagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.descricao

class Pagamento(models.Model):
    numero_documento = models.CharField(max_length=255, null=False, blank=False, verbose_name="Número documento (*)")
    descricao = models.CharField(max_length=255, null=False, blank=False)
    empresa = models.ForeignKey(Empresa, on_delete='SEL_NULL', null=False, blank=False)
    tipo_de_pagamento = models.ForeignKey(TipoPagamento, on_delete='SET_NULL', null=False, blank=False)
    data_de_vencimento = models.DateField(null=False, blank=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    status_pagamento = models.ForeignKey(StatusDoPagamento, on_delete='SET_NULL', null=False, blank=False)

    fornecedor = models.ForeignKey(Fornecedor, on_delete='SET_NULL', null=False, blank=True)
    parcela = models.CharField(max_length=255, null=True, blank=True)
    competencia = models.CharField(max_length=255, null=True, blank=True)
    valor_juros = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    data_de_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.descricao


class Estado(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=False, blank=False)

class CidadesPorEtado(models.Model):
    sigla = models.CharField(max_length=255, null=False, blank=False)
    total = models.IntegerField(null=False, blank=False)

class Cidade(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete='SET_NULL', null=False, blank=False)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete='SET_NULL', null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete='SET_NULL', null=False, blank=False)


class CategoriaEvento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)

class Evento(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    data_evento = models.DateField(max_length=255, null=False, blank=False)
    hora_evento = models.DateField(null=False, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete='SET_NULL', null=False, blank=False)
    categoria_evento = models.ForeignKey(CategoriaEvento, on_delete='SET_NULL', null=False, blank=False)
    realizado = models.BooleanField(default=False, null=False, blank=False)

class Banner(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.FileField(blank=True, null=True, upload_to='banner')
    class Meta:
        managed = False
        db_table = 'banner'


