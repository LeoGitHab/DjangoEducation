from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order
from .admin_mixins import ExportAsMixins


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description='Archive products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsMixins):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'price', 'quantity', 'date_received', 'description_short', 'archived',
    list_display_links = 'pk', 'name',
    ordering = '-name', '-pk',
    search_fields = 'name', 'description',
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Price-count options', {
            'fields': ('price', 'quantity'),
            'classes': ('wide', 'collapse',),
        }),
        ('Choose additional guarantee options', {
            'fields': ('has_additional_guarantee',),
            'classes': ('collapse',),
            'description': ("Choose this option for adding additional guarantee.",),
        }),
        ('Extra options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': ("Extra option. Field 'archived' for sort delete.",),
        }),
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 50:
            return obj.description
        return obj.description[:50] + '...'


# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose',

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

# admin.site.register(Product, ProductAdmin)
