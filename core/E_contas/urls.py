from django.contrib import admin
from django.urls import path
from .views import *
from .form import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/fornecedor/', CadastrarFornecedor.as_view(), name='cadastrar_fornecedor'),
    path('cadastro/empresa/', CadastrarEmpresa.as_view(), name='cadastrar_empresa'),
    path('cadastro/pagamento', CadastrarPagamento.as_view(), name='cadastrar_pagamento'),
    path('listar/fornecedor/', ListarFornecedor.as_view(), name='listar_fornecedor'),
    path('listar/empresa/', ListarEmpresa.as_view(), name='listar_empresa'),
    path('listar/pagamento', ListarPagamento.as_view(), name='listar_pagamento'),
    path('atualizar/fornecedor/<int:pk>/', AtualizarFornecedor.as_view(), name='atualizar_fornecedor'),
    path('atualizar/empresa/<int:pk>/', AtualizarEmpresa.as_view(), name='atualizar_empresa'),
    path('atualizar/pagamento/<int:pk>/', AtualizarPagamento.as_view(), name='atualizar_pagamento'),
    path('detalhe/empresa/<int:pk>/', DetalheEmpresa.as_view(), name='detalhe_empresa'),
    path('detalhe/fornecedor/<int:pk>/', DetalheFornecedor.as_view(), name='detalhe_fornecedor'),
    path('detalhe/pagamento/<int:pk>/', DetalhePagamento.as_view(), name='detalhe_pagamento'),
    # path('cadastro/evento/', EventoForm.as_view(), name='cadastrar_evento'),
    # path('cadastro/categoria_evento',CategoriaEventoForm.as_view(),name='cadastrar_categoria_evento'),
    path('grafico/', Grafico.as_view(), name='grafico'),
    # path('graficos/', GraficoPagamento, name='graficos'),
    path('ws/total-cidade-por-etado', WebService.total_cidade_por_estado, name='totalcidades'),

    path('', Index.as_view(), name="index"),
    path('quem_somos', Quem_somos.as_view(), name="quem_somos"),
    path('contato', Contato.as_view(), name="contato"),
    path('parceiro', Parceiro.as_view(), name="parceiro"),
    path('acessar_conta', Acessar_conta.as_view(), name="acessar_conta"),
    path('home_admin/', Home_admin.as_view(), name="home_admin"),
    path('sistema', Sistema.as_view(), name="sistema"),
    path('sistema/cadastrar', Cadastrar.as_view(), name="cadastrar"),
    path('sistema/listar', Listar.as_view(), name="listar"),
    path('sistema/listar2', Listar2.as_view(), name="listar2"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

