from django.contrib import admin
from django.urls import path
from .views import *
from .form import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adm-base', AdmBase.as_view(), name='adm-base'),
    path('adm', Adm.as_view(), name='adm'),
    path('adm/grafico/', Grafico.as_view(), name='grafico'),
    path('adm/grafico/conta_paga_receber', GraficoContaPagarReceber.as_view(), name='grafico_conta_paga_recebe'),
    path('adm/grafico/conta_paga_por_empresa', GraficoContaPagaPorEmpresa.as_view(), name='grafico_conta_paga_por_empresa'),
    path('adm/relatorio/', Relatorio.as_view(), name='relatorio'),
    path('adm/relatorio/a_pagar', RelAPagar.as_view(), name='relatorio_conta_pagar'),
    path('adm/cadastro/', Cadastro.as_view(), name='cadastro'),
    path('adm/cadastro/venda/', CadastroVenda.as_view(), name='cadastro_venda'),
    path('adm/cadastro/fornecedor/', CadastroFornecedor.as_view(), name='cadastro_fornecedor'),
    path('adm/cadastro/empresa/', CadastroEmpresa.as_view(), name='cadastro_empresa'),
    path('adm/cadastro/pagamento', CadastroPagamento.as_view(), name='cadastro_pagamento'),
    path('adm/cadastro/local_de_recebimento', CadastroLocalRecebimento.as_view(), name='cadastro_local_recebimento'),
    path('adm/gerenciamento', Gerenciamento.as_view(), name='gerenciamento'),
    path('adm/lista/venda/', ListaVenda.as_view(), name='lista_venda'),
    path('adm/lista/fornecedor/', ListaFornecedor.as_view(), name='lista_fornecedor'),
    path('adm/lista/empresa/', ListaEmpresa.as_view(), name='lista_empresa'),
    path('adm/lista/pagamento', ListaPagamento.as_view(), name='lista_pagamento'),
    path('adm/lista/local_recebimento', ListaLocalRecebimento.as_view(), name='lista_local_recebimento'),
    path('adm/atualiza/venda/<int:pk>/', AtualizaVenda.as_view(), name='atualiza_venda'),
    path('adm/atualiza/fornecedor/<int:pk>/', AtualizaFornecedor.as_view(), name='atualiza_fornecedor'),
    path('adm/atualiza/empresa/<int:pk>/', AtualizaEmpresa.as_view(), name='atualiza_empresa'),
    path('adm/atualiza/pagamento/<int:pk>/', AtualizaPagamento.as_view(), name='atualiza_pagamento'),
    path('adm/atualiza/local_recebimento/<int:pk>/',
         AtualizaLocalRecebimento.as_view(), name='atualiza_local_recebimento'),
    path('adm/detalhe/venda/<int:pk>/', DetalheVenda.as_view(), name='detalhe_venda'),
    path('adm/detalhe/empresa/<int:pk>/', DetalheEmpresa.as_view(), name='detalhe_empresa'),
    path('adm/detalhe/fornecedor/<int:pk>/', DetalheFornecedor.as_view(), name='detalhe_fornecedor'),
    path('adm/detalhe/pagamento/<int:pk>/', DetalhePagamento.as_view(), name='detalhe_pagamento'),
    path('adm/detalhe/local_recebimento/<int:pk>/',
         DetalheLocalRecebimento.as_view(), name='detalhe_local_recebimento'),
    path('adm/deleta/empresa/<int:pk>', DeletaEmpresa.as_view(), name='deleta_empresa'),
    path('adm/deteta/venda/<int:pk>', DeletaVenda.as_view(), name='deleta_venda'),
    path('adm/deleta/pagamento/<int:pk>', DeletaPagamento.as_view(), name='deleta_pagamento'),
    path('adm/deleta/fornecedor/<int:pk>', DeletaFornecedor.as_view(), name='deleta_fornecedor'),
    path('adm/deletar/local_recebimento/<int:pk>', DeletaLocalRecebimento.as_view(), name='deleta_local_recebimento'),
    path('', Index.as_view(), name="index"),
    path('contato', Contato.as_view(), name="contato"),
    path('parceiro', Parceiro.as_view(), name="parceiro"),
    path('acessar_conta', Acessar_conta.as_view(), name="acessar_conta"),

    # path('cadastro/evento/', EventoForm.as_view(), name='cadastrar_evento'),
    # path('cadastro/categoria_evento',CategoriaEventoForm.as_view(),name='cadastrar_categoria_evento'),
    # path('grafico-pagamento/', GraficoPagamento, name='grafico-pagamento'),
    # path('ws/total-cidade-por-etado', WebService.total_cidade_por_estado, name='totalcidades'),
    # path('home_admin/', Home_admin.as_view(), name="home_admin"),
    # path('sistema', Sistema.as_view(), name="sistema"),
    # path('sistema/cadastro', Cadastro.as_view(), name="cadastro"),
    # path('sistema/lista', Listar.as_view(), name="lista"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

