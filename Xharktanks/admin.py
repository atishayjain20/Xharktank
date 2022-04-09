from django.contrib import admin
from Xharktanks import models
from .models import Investors,Entre
# Register your models here.

# To register The models Into Admin Page so that admin can delete or update any of the pitch

@admin.register(Entre)
class EntreAdmin(admin.ModelAdmin):
    fields=['entrepreneur','pitchTitle','pitchIdea','askAmount','equity','offers']


@admin.register(Investors)
class InvestorsAdmin(admin.ModelAdmin):
    fields=['investor','amount','equity','comment']
    # 'investedBy'