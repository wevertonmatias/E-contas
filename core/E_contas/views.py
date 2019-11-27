from datetime import timezone
from django.shortcuts import render, get_object_or_404
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin

from .form import *
from .models import *
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, View, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.db.models import Sum


class AdmBase(TemplateView):
    template_name = 'adm/comuns/adm_base.html'


class Adm(TemplateView):
    template_name = 'adm/comuns/adm.html'


class Cadastro(TemplateView):
    template_name = 'adm/cadastro/cadastro_base.html'


class CadastroVenda(CreateView):
    template_name = 'adm/cadastro/venda.html'
    model = Venda
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class CadastroFornecedor(CreateView):
    template_name = 'adm/cadastro/fornecedor.html'
    model = Fornecedor
    fields = '__all__'

    # form_class = FornecedorForm
    def get_success_url(self):
        return reverse_lazy('listar_fornecedor')

    # def from_valid(self, form):
    #     formulario = form
    #     formulario.save(commit=False)


class CadastroEmpresa(CreateView):
    template_name = 'adm/cadastro/empresa.html'
    model = Empresa
    fields = '__all__'

    # form_class = EmpresaForm
    #
    def get_success_url(self):
        return reverse_lazy('cadastro')


class CadastroPagamento(CreateView):
    template_name = 'adm/cadastro/pagamento.html'
    model = Pagamento
    fields = '__all__'

    # form_class = EmpresaForm

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')

    # def from_valid(self, form):
    #     formulario = form
    #     formulario.save(commit=False)


class Gerenciamento(TemplateView):
    template_name = 'adm/gerenciamento/gerenciamento_base.html'


class Lista(TemplateView):
    template_name = 'adm/lista/lista_base.html'


class ListaVenda(ListView):
    template_name = 'adm/gerenciamento/lista/venda.html'
    model = Venda
    fields = '__all__'
    paginate_by = 10


class ListarFornecedor(ListView):
    template_name = 'adm/lista/fornecedor.html'
    model = Fornecedor
    fields = '__all__'
    paginate_by = 10


class ListaEmpresa(ListView):
    template_name = 'adm/gerenciamento/lista/empresa.html'
    model = Empresa
    fields = '__all__'
    paginate_by = 10


class ListaPagamento(ListView):
    template_name = 'adm/gerenciamento/lista/pagamento.html'
    model = Pagamento
    fields = '__all__'


class AtualizaVenda(UpdateView):
    template_name = 'adm/gerenciamento/atualiza/venda.html'
    model = Venda
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class AtualizarFornecedor(UpdateView):
    template_name = 'adm/atualiza/fornecedor.html'
    model = Fornecedor
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_fornecedor')


class AtualizaEmpresa(UpdateView):
    template_name = 'adm/gerenciamento/atualiza/empresa.html'
    model = Empresa
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_empresa')


class AtualizaPagamento(UpdateView):
    template_name = 'adm/gerenciamento/atualiza/pagamento.html'
    model = Pagamento
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')


class DetalheVenda(DetailView):
    template_name = 'adm/gerenciamento/detalhe/venda.html'
    model = Venda


class DetalheEmpresa(DetailView):
    template_name = 'adm/gerenciamento/detalhe/empresa.html'
    model = Empresa


class DetalheFornecedor(DetailView):
    template_name = 'adm/detalhe/fornecedor.html'
    model = Fornecedor


class DetalhePagamento(DetailView):
    template_name = 'adm/gerenciamento/detalhe/pagamento.html'
    model = Pagamento
    field = '__all__'


class DeletaVenda(DeleteView):
    model = Venda
    template_name = 'adm/gerenciamento/deleta/venda.html'

    def get_success_url(self):
        return reverse_lazy('lista_venda')


class DeletaEmpresa(DeleteView):
    model = Empresa
    template_name = 'adm/gerenciamento/deleta/empresa.html'

    def get_success_url(self):
        return reverse_lazy('lista_empresa')

class DeletaPagamento(DeleteView):
    model = Pagamento
    template_name = 'adm/gerenciamento/deleta/pagamento.html'

    def get_success_url(self):
        return reverse_lazy('lista_pagamento')


class Grafico(TemplateView):
    template_name = 'adm/grafico/grafico_base.html'


class GraficoContaPagarReceber(TemplateView):
    template_name = 'adm/grafico/grafico_conta_pagar_receber.html'

    def get_context_data(self, **kwargs):
        ctx = super(GraficoContaPagarReceber, self).get_context_data(**kwargs)
        ctx['pagar'] = Pagamento.objects.aggregate(Sum('valor'))
        ctx['receber'] = Venda.objects.aggregate(Sum('valor'))
        return ctx

class GraficoContaPagaPorEmpresa(TemplateView):
    template_name = 'adm/grafico/grafico_paga_por_empresa.html'

    def get_context_data(self, **kwargs):
        ctx = super(GraficoContaPagaPorEmpresa, self).get_context_data(**kwargs)
        ctx['empresas'] = Empresa.objects.all()
        ctx['valores'] = Pagamento.objects.values('empresa_id').annotate(Sum('valor'))
        return ctx


class Relatorio(TemplateView):
    template_name = 'adm/relatorios/relatorio.html'


class RelAPagar(ListView, PDFTemplateResponseMixin):
    template_name = 'adm/relatorios/a_pagar.html'
    model = Pagamento
    fields = '__all__'


class Index(TemplateView):
    template_name = 'site/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(Index, self).get_context_data(**kwargs)
        ctx['banners'] = Banner.objects.all()
        return ctx


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


class Sistema(TemplateView):
    template_name = 'adm/sistema.html'


#
#     def get_context_data(self, **kwargs):
#         ctx = super(Relatorio, self).get_context_data(**kwargs)
#         ctx['boletos'] = Boleto.objects.all()
#         return ctx

def GraficoPagamento(request):
    queryset = Pagamento.objects.all()
    empresas = [obj.empresa.pk for obj in queryset]
    valores = [int(obj.valor) for obj in queryset]

    context = {
        'empresas': json.dumps(empresas),
        'valores': json.dumps(valores),
    }
    return render(request, 'site/grafico/grafico.html', context)


class WebService(View):
    def total_cidade_por_estado(self):
        retorno = CidadesPorEtado.objects.raw("select e.id, e.sigla, count(c.descricao) as total"
                                              " from E_Contas_cidade c inner join E_Contas_estado e "
                                              " on c.estado_id = e.id"
                                              " group by e.id, e.sigla")
        dicionario = {}
        for item in retorno:
            dicionario[item.sigla] = item.total

        return JsonResponse(dicionario)


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
