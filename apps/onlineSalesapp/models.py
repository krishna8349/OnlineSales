from django.db import models


class Address(models.Model):
    # id = models.IntegerField(primary_key=True)
    external_id = models.TextField(blank=True, null=True)  
    address_data = models.JSONField(blank=True, null=True)  
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Address"
        db_table = 'address'
        
class CardRegistration(models.Model):
    # id = models.IntegerField(primary_key=True)
    worldpay_order_code = models.CharField(max_length=50)
    registration_status = models.CharField(max_length=20)
    crm_card_token = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Card Registration"
        db_table = 'card_registration'

class Cart(models.Model):
    # id = models.IntegerField(primary_key=True)
    delivery_address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    installation_address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name='cart_installation_address_set')
    customer_registration_id = models.ForeignKey('CustomerRegistration', on_delete=models.SET_NULL, blank=True, null=True)
    customer_account_id = models.ForeignKey('CustomerAccount', on_delete=models.SET_NULL, blank=True, null=True)
    is_auto_renew = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cart"
        db_table = 'cart'

class CartItem(models.Model):
    # id = models.IntegerField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    parent_cart_item_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Cart Item"
        db_table = 'cart_item'

class CustomerAccount(models.Model):
    # id = models.IntegerField(primary_key=True)
    customer_registration = models.ForeignKey('CustomerRegistration', on_delete=models.SET_NULL, blank=True, null=True)
    crm_account_number = models.CharField(max_length=20, blank=True, null=True)
    id_type_id = models.ForeignKey('IdType', on_delete=models.SET_NULL, blank=True, null=True)
    id_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=200)
    is_promotion_consent = models.BooleanField(default=False, db_index=True)
    billing_address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    card_registration_id = models.ForeignKey(CardRegistration, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Customer Account"
        db_table = 'customer_account'

class CustomerDocument(models.Model):
    # id = models.IntegerField(primary_key=True)
    crm_doc_filename = models.CharField(max_length=200)
    uploaded_doc_filename = models.CharField(max_length=200)
    is_uploaded = models.BooleanField(default=False)
    crm_doc_path = models.CharField(max_length=200)
    crm_doc_tool = models.CharField(max_length=10)
    crm_doc_profile = models.CharField(max_length=20)
    crm_doc_template = models.CharField(max_length=20)
    crm_doc_type = models.CharField(max_length=10)
    crm_doc_template_area = models.CharField(max_length=20)
    uploaded_doc_type = models.CharField(max_length=20)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    customer_account_id = models.ForeignKey(CustomerAccount, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Customer Document"
        db_table = 'customer_document'

class CustomerRegistration(models.Model):
    # id = models.IntegerField(primary_key=True)
    crm_customer_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    contact_email = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    registration_stage_id = models.ForeignKey('RegistrationStage', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Customer Registration"
        db_table = 'customer_registration'

class CrmIdCode(models.Model):
    # id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Crrm Id Code"
        db_table = "crm_id_code"

class CrmIdDescription(models.Model):
    # id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Crm Id Description"
        db_table = "crm_id_description"

class IdType(models.Model):
    # id = models.IntegerField(primary_key=True)
    crm_id_code_id = models.ForeignKey(CrmIdCode, on_delete=models.SET_NULL, blank=True, null=True)
    crm_id_description_id = models.ForeignKey(CrmIdDescription, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Id Types"
        db_table = 'id_type'


class PortingData(models.Model):
    # id = models.IntegerField(primary_key=True)
    service_number = models.CharField(max_length=15)
    operator_code = models.CharField(max_length=15)
    operator_name = models.CharField(max_length=100)
    is_prepaid = models.BooleanField(default=False)
    iccid = models.CharField(max_length=20, blank=True, null=True)
    is_owner = models.BooleanField(default=False)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    owner_id_type_id = models.ForeignKey(IdType, on_delete=models.SET_NULL, blank=True, null=True)
    owner_id_number = models.CharField(max_length=15)
    owner_nationality = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    cart_item_id = models.ForeignKey(CartItem,  on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Porting Data"
        db_table = 'porting_data'

class Product(models.Model):
    # id = models.IntegerField(primary_key=True)
    crm_product_code = models.CharField(max_length=10)
    crm_description = models.CharField(max_length=100)
    crm_service_yn = models.CharField(max_length=100)
    crm_package_yn = models.CharField(max_length=100)
    crm_service_cd = models.CharField(max_length=100)
    crm_number_plan_code = models.CharField(max_length=10, blank=True, null=True)
    display_information = models.CharField(max_length=200, blank=True, null=True)
    crm_comp_group_code = models.CharField(max_length=10, blank=True, null=True)
    crm_parent_package_code = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    cart_item_id = models.ForeignKey(CartItem,  on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Product"
        db_table = 'product'


class ProductPrice(models.Model):
    # id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product,  on_delete=models.SET_NULL, blank=True, null=True)
    crm_product_code = models.CharField(max_length=10)
    price_type = models.CharField(max_length=10)
    price_version = models.IntegerField()
    tax_category = models.CharField(max_length=10)
    tax_rate = models.FloatField()
    tax_included_amount = models.FloatField()
    tax_excluded_amount = models.FloatField()
    price_start_date = models.DateField()
    price_end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    cart_item_id = models.ForeignKey(CartItem,  on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "product_price"
        db_table = 'product_price'

class StageDescription(models.Model):
    # id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Stage Description"
        db_table = "stage_description"

class RegistrationStage(models.Model):
    # id = models.IntegerField(primary_key=True)
    stage_description_id = models.ForeignKey(StageDescription, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Registration Stages"
        db_table = 'registration_stage'
