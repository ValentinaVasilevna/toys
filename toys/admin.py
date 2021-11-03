from django.contrib import admin
from toys.models import Toy, Material, Cat
# Register your models here.
class ToyAdmin(admin.ModelAdmin):
    pass

class MaterialAdmin(admin.ModelAdmin):
    pass

class CatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Toy, ToyAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Cat, CatAdmin)
