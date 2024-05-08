from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerRegistration, CustomerAccount, Address
from .serializers import CustomerRegistrationSerializer, CustomerAccountSerializer, AddressSerializer


class OnlineSale(viewsets.ViewSet):
    queryset = CustomerRegistration.objects.all()
    serializer_class = CustomerRegistrationSerializer

    def create(self, request):
        # try:
            data = request.data
            
            # creating Customer Registration instance
            CustomerRegistration_serializer = CustomerRegistrationSerializer(data = data.get("aboutYou"))
            CustomerRegistration_serializer.is_valid(raise_exception=True)
            CustomerRegistration_instance = CustomerRegistration_serializer.save()
            
            #customer_account isinstance
            identity = data.get("identity")
            identity["customer_registration"] = CustomerRegistration_instance.id
            customer_account_serializer = CustomerAccountSerializer(data = identity)
            customer_account_serializer.is_valid(raise_exception=True)
            customer_account_instance = customer_account_serializer.save()

            # ceating address instance
            deliveryAddrress = {}
            address = data.get("deliveryAddrress")
            address_data = {
                "address_data": address
            }
            address_serializer = AddressSerializer(data = address_data)
            address_serializer.is_valid(raise_exception=True)
            addess_instace = address_serializer.save()

            # Serialize both instances for response
            customer_registration_data = CustomerRegistrationSerializer(CustomerRegistration_instance).data
            customer_account_data = CustomerAccountSerializer(customer_account_instance).data
            addess_instace_data = AddressSerializer(addess_instace).data

            return Response({"CustomerRegistration": customer_registration_data, "CustomerAccount": customer_account_data, "Addess":addess_instace_data})
        # except Exception as e:
        #     response_body = {
        #         "code": "400",
        #         "reason": str(e),
        #         "message": str(e),
        #         "status": status.HTTP_400_BAD_REQUEST,
        #         "referenceError": str(e),
        #     }
        #     return Response(response_body, status=status.HTTP_400_BAD_REQUEST)
