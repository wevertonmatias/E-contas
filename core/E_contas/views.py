from datetime import timezone
from django.shortcuts import render, get_object_or_404
from .form import *
from .models import *
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect ,JsonResponse
import json

class Cadastrar(TemplateView):
    template_name = 'adm/cadastrar/cadastrar.html'

class CadastrarFornecedor(CreateView):
    template_name = 'adm/cadastrar/fornecedor.html'
    model = Fornecedor
    fields = '__all__'
    # form_class = FornecedorForm
    def get_success_url(self):
        return reverse_lazy('listar_fornecedor')

    # def from_valid(self, form):
    #     formulario = form
    #     formulario.save(commit=False)

class CadastrarEmpresa(CreateView):
    template_name = 'adm/cadastrar/empresa.html'
    model = Empresa
    fields = '__all__'
    # form_class = EmpresaForm
    #
    def get_success_url(self):
        return reverse_lazy('cadastrar')

class CadastrarPagamento(CreateView):
    template_name = 'adm/cadastrar/empresa.html'
    model = Pagamento
    fields = '__all__'
    # form_class = EmpresaForm

    def get_success_url(self):
        return reverse_lazy('listar_pagamento')

    # def from_valid(self, form):
    #     formulario = form
    #     formulario.save(commit=False)

class Listar(TemplateView):
    template_name = 'adm/listar/listar.html'

class Listar2(TemplateView):
    template_name = 'adm/listar/listar2.html'

class ListarFornecedor(ListView):
    template_name = 'adm/listar/fornecedor.html'
    model = Fornecedor
    fields = '__all__'
    paginate_by = 10

class ListarEmpresa(ListView):
    template_name = 'adm/listar/empresa.html'
    model = Empresa
    fields = '__all__'
    paginate_by = 10

class ListarPagamento(ListView):
    template_name = 'adm/listar/pagamento.html'
    model = Pagamento
    fields = '__all__'
    paginate_by = 10

class AtualizarFornecedor(UpdateView):
    template_name = 'adm/atualizar/fornecedor.html'
    model = Fornecedor
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_fornecedor')

class AtualizarEmpresa(UpdateView):
    template_name = 'adm/atualizar/empresa.html'
    model = Empresa
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_empresa')

class AtualizarPagamento(UpdateView):
    template_name = 'adm/atualizar/pagamento.html'
    model = Pagamento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_pagamento')

class DetalheEmpresa(DetailView):
    template_name = 'adm/detalhes/empresa.html'
    model = Empresa

class DetalheFornecedor(DetailView):
    template_name = 'adm/detalhes/fornecedor.html'
    model = Fornecedor

class DetalhePagamento(DetailView):
    template_name = 'adm/detalhes/pagamento.html'
    model = Pagamento

class CadastrarEvento(CreateView):
    template_name = 'adm/cadastro/evento.html'
    models = Evento
    form_class = EventoForm

    def get_success_url(self):
        return reverse_lazy('cadastrar_evento.html')

    def from_valid(self, form):
        formulario = form
        formulario.save(commit=False)


class CadastrarCategoriaEvento(CreateView):
    template_name = 'adm/cadastro/categoria.html'
    models = CategoriaEvento
    form_class = CategoriaEventoForm

    def get_success_url(self):
        return reverse_lazy('cadastrar_categoria_evento')

class WebService(View):
    def total_cidade_por_estado(self):
        retorno = CidadesPorEtado.objects.raw("select e.id, e.sigla, count(c.descricao) as total"
                                              " from econtas_cidade c inner join econtas_estado e "
                                              " on c.estado_id = e.id"
                                              " group by e.id, e.sigla")

        dicionario = {}
        for item in retorno:
            dicionario[item.sigla] = item.total

        return JsonResponse(dicionario)

class Grafico(TemplateView):
    template_name = 'admin/graficos/grafico.html'

def GraficoPagamento(request):
    queryset = Pagamento.objects.all()
    empresas = [obj.empresa.pk for obj in queryset]
    valores = [int(obj.valor) for obj in queryset]

    context = {
        'empresas': json.dumps(empresas),
        'valores': json.dumps(valores),
    }
    return render(request, 'site/graficos/grafico.html', context)


class Index(TemplateView):
    template_name ='site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(Index, self).get_context_data(**kwargs)
        ctx['banners'] = Banner.objects.all()
        return ctx

class Sistema(TemplateView):
    template_name = 'adm/sistema.html'
#
#     def get_context_data(self, **kwargs):
#         ctx = super(Relatorio, self).get_context_data(**kwargs)
#         ctx['boletos'] = Boleto.objects.all()
#         return ctx

class Home_admin(TemplateView):
    template_name = 'adm/home_admin.html'

class Quem_somos(TemplateView):
    template_name = 'site/quem-somos.html'

class Contato(TemplateView):
    template_name = 'site/contato.html'

class Parceiro(TemplateView):
    template_name = 'site/parceiro.html'

class Acessar_conta(TemplateView):
    template_name = 'site/acessar_conta.html'
