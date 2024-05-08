from django.contrib import admin

# Register your models here.
from .models import (
    Address,
    CardRegistration,
    Cart,
    CartItem,
    CustomerAccount,
    CustomerDocument,
    CustomerRegistration,
    CrmIdCode,
    CrmIdDescription,
    IdType,
    PortingData,
    Product,
    ProductPrice,
    StageDescription,
    RegistrationStage
)

admin.site.register(Address)
admin.site.register(CardRegistration)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CustomerAccount)
admin.site.register(CustomerDocument)
admin.site.register(CustomerRegistration)
admin.site.register(CrmIdCode)
admin.site.register(CrmIdDescription)
admin.site.register(IdType)
admin.site.register(PortingData)
admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(StageDescription)
admin.site.register(RegistrationStage)
