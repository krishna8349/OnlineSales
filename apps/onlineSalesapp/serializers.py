from rest_framework import serializers
from apps.onlineSalesapp.models import (
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


class AddressSerializer(serializers.ModelSerializer):
    # externalId = serializers.CharField(source="external_id", required=False)
    # addressData = serializers.JSONField(source="address_data", required=False)
    # createdDate = serializers.CharField(source="created_date", required=False)
    # modifiedDate = serializers.CharField(source="modified_date", required=False)

    class Meta:
        model = Address
        # fields = ["externalId", "addressData", "createdDate", "modifiedDate"]
        fields = "__all__"

class CardRegistrationSeriailzer(serializers.ModelSerializer):
    worldpayOrderCode = serializers.CharField(source="worldpay_order_code", required=False)
    registrationStatus = serializers.CharField(source="registration_status", required=False)
    crmCardToken = serializers.CharField(source="crm_card_token", required=False)
    createdDate = serializers.CharField(source="created_date", required=False)
    modifiedDate = serializers.CharField(source="modified_date", required=False)

    class Meta:
        model = CardRegistration
        fields = ["worldpayOrderCode", "registrationStatus", "crmCardToken", "createdDate", "modifiedDate"]

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"

class CustomerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAccount
        fields = "__all__"

class CustomerDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerDocument
        fields = "__all__"

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerRegistration
        fields = "__all__"

class CrmIdCodeSerrializer(serializers.ModelSerializer):

    class Meta:
        model = CrmIdCode
        fields = "__all__"

class CrmIdDescriptionSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = CrmIdDescription
        fields = "__all__"

class IdTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IdType
        fields = "__all__"

class PortingDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortingData
        fields = "__all__"

class ProductSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = "__all__"

class StageDescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StageDescription
        fields = "__all__"

class RegistrationStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationStage
        fields = "__all__"