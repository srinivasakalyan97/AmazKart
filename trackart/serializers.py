from rest_framework import serializers

from trackart.models import InvoiceItems


class GetPeopleByNationS(serializers.Serializer):
    country = serializers.CharField(required=True)

class NewCustomerSignupS(serializers.Serializer):
    customerid = serializers.IntegerField(required=True)
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    company =  serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    postalcode = serializers.IntegerField(required=True)
    phone = serializers.CharField(required=True)
    fax = serializers.IntegerField(required=True)
    email = serializers.CharField(required=True)
    supportrepid = serializers.IntegerField(required=True)

class GetInvoiceDetailsS(serializers.Serializer):
    customerid = serializers.IntegerField(required=True)

class invoicesMultipleS(serializers.ModelSerializer):
    invoiceid =  serializers.CharField()
    customerid_id = serializers.CharField()
    invoicedate = serializers.CharField()
    billingaddress = serializers.CharField()
    billingcity = serializers.CharField()
    billingstate = serializers.CharField()
    billingcountry = serializers.CharField()
    billingpostalcode = serializers.CharField()
    total = serializers.CharField()
    class Meta:
        model = InvoiceItems
        fields = ('invoiceid', 'customerid_id', 'invoicedate', 'billingaddress', 'billingcity','billingstate',
                  'billingcountry','billingpostalcode','total')