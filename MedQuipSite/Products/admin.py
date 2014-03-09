from django.contrib import admin
from itertools import chain
from operator import attrgetter
from Products.models import Product, Category,Attribute


class AttributeInline(admin.TabularInline):
    model = Attribute
    fields=('description','price','sku')


def hide(modeladmin, request, queryset):
    queryset.update(status='p')
hide.short_description = "hide selected products (Removes them from the website)"
       
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','sku']
    view_on_site = True
    fields = ('name','sku','price','description','short_description','weight','visible')
    inlines = [AttributeInline,]
    actions = ['hide']
    
    def get_search_results(self, request, queryset, search_term):
        
        queryset, use_distinct = super(ProductAdmin, self).get_search_results(request, queryset, search_term)
        
        if(search_term):
            attribute_query_set = Attribute.objects.filter(sku__contains=search_term)
            
            result_list = sorted(chain(queryset, attribute_query_set),key=attrgetter('sku'))
            return result_list,use_distinct
        else:
            return queryset, use_distinct
        
    def hide(self, request, queryset):
        rows_updated = queryset.update(visible=False)
        if rows_updated == 1:
            message_bit = "1 product was"
        else:
            message_bit = "%s products were" % rows_updated
        self.message_user(request, "%s successfully hidden." % message_bit) 
        

    
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
