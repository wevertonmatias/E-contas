from django.contrib import admin
from .models import *
from django.contrib import admin

# Register your models here.

admin.site.register(Pagamento)
admin.site.register(Fornecedor)
admin.site.register(Empresa)
admin.site.register(LocalPagamento)
admin.site.register(TipoPagamento)
admin.site.register(StatusDoPagamento)
# admin.site.register(Banner)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Venda)


