from django.contrib import admin
from .models import Cliente, Pedido


def formatear_pesos_chilenos(monto):
	return f"${monto:,.0f}".replace(",", ".")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ("nombre", "correo_electronico", "telefono", "monto_total_formateado")

	@admin.display(description="Monto total (CLP)")
	def monto_total_formateado(self, obj):
		return formatear_pesos_chilenos(obj.monto_total)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "id_cliente", "fecha", "stock", "monto_formateado")

	@admin.display(description="Monto (CLP)")
	def monto_formateado(self, obj):
		return formatear_pesos_chilenos(obj.monto)
