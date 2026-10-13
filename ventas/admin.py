from django.contrib import admin
from .models import Cliente, Pedido

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'correo_electronico', 'telefono', 'monto_total')
    list_filter = ('nombre', 'correo_electronico')
    search_fields = ('nombre', 'correo_electronico')


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_cliente', 'fecha', 'stock', 'monto')
    list_filter = ('fecha', 'id_cliente')
    search_fields = ('nombre', 'id_cliente__nombre')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)