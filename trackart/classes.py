from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated  # <-- Here

from trackart.serializers import GetPeopleByNationS, NewCustomerSignupS, GetInvoiceDetailsS, invoicesMultipleS


class CustomerOrderDetails(APIView):
    def post(self,request):
        active_database = 'default'
        request_data = GetInvoiceDetailsS(data=request.data)
        if request_data.is_valid():
            customerid = request_data.validated_data['customerid']
            from trackart.models import Invoices, Customers, Albums, Tracks, Artists, Genres, InvoiceItems
            try:
                customerdetails = Customers.objects.using(active_database).filter(customerid=customerid).values()
                invoiceDetails = Invoices.objects.using(active_database).filter(customerid=customerid)
                invoiceDetails = invoicesMultipleS(invoiceDetails,many=True)
                # print("invoiceDetails after passing to result serializer",invoiceDetails.data)
                #Write code here to extract invoice ids
                invoiceItemsDetails = InvoiceItems.objects.using(active_database).filter(invoiceid=284).values()
                #Write code here to extract trackId
                trackidarr = [2316,2322,2328,2334,2340,2346,2352,2358,2364]
                trackidresultarr = []
                for a in trackidarr:
                    trackidDetails = Tracks.objects.using(active_database).filter(trackid=a).values()
                    trackidresultarr.append(trackidDetails)
                #Write code here to extract albumid
                albumsDetails = Albums.objects.using(active_database).filter(albumid=187).values()
                #Write code here to extract artists
                artistDetails = Artists.objects.using(active_database).filter(artistid=122).values()
                if customerdetails:
                    return Response({"SUCCESS": True, "status_code": 1,"customer":customerdetails,"invoice":invoiceDetails.data,"invoiceItemsDetails":invoiceItemsDetails,
                                 "trackidDetails":trackidresultarr,"albumsDetails":albumsDetails,"artistDetails":artistDetails,"message": 'Customer exist!'},
                                status=status.HTTP_200_OK)
                else:
                    return Response({"SUCCESS": True, "status_code": 1,
                                     "message": 'No Customer exist!'},
                                    status=status.HTTP_200_OK)
            except Exception as error:
                print("exception | {}".format(error))
                return Response({"SUCCESS": False, "status_code": 0,
                                 "message": 'Something went wrong while Fetching',
                                 }, status=status.HTTP_200_OK)


class GetInvoiceDetails(APIView):
    def post(self,request):
        active_database = 'default'
        request_data = GetInvoiceDetailsS(data=request.data)
        if request_data.is_valid():
            customerid = request_data.validated_data['customerid']
            from trackart.models import Invoices, Customers
            try:
                customerdetails = Customers.objects.using(active_database).filter(customerid=customerid).values()
                print("customerdetails",customerdetails)
                invoiceobj = Invoices.objects.using(active_database).filter(customerid=customerid).values()
                if customerdetails:
                    if invoiceobj:
                        # print("invoice obj",invoiceobj)
                        print("invoice exists for customer")
                        return Response({"SUCCESS": True, "status_code": 1,"invoices":list(invoiceobj),"customerdetails":list(customerdetails),
                                     "message": 'Customer invoice exist!'},
                                    status=status.HTTP_200_OK)

                    else:
                        print("No invoice found for customer")
                        return Response({"SUCCESS": False, "status_code": 0,
                                     "message": 'No invoice exist for given customer!'},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"SUCCESS": False, "status_code": 0,
                                     "message": 'No customer exist!'},
                                    status=status.HTTP_200_OK)


            except Exception as error:
                print("exception | {}".format(error))
                return Response({"SUCCESS": False, "status_code": 0,
                                 "message": 'Something went wrong while Fetching',
                                 }, status=status.HTTP_200_OK)

class NewCustomerSignup(APIView):
    def post(self,request):
        active_database = 'default'
        request_data = NewCustomerSignupS(data=request.data)
        print(request_data)
        if request_data.is_valid():
            print("inside valid")
            phone = request_data.validated_data['phone']
            # email = request_data.validated_data['email']
            # print("phone email",phone,email)
        from trackart.models import Customers
        try:
            # phone = request_data.validated_data['phone']
            newcobj = Customers.objects.using(active_database).filter(phone=phone)
            print(newcobj.values())
            if newcobj:
                print("user exists")
                return Response({"SUCCESS": True, "status_code": 0,
                                     "message": 'Customer already exist!'},
                                    status=status.HTTP_200_OK)

            else:
                print("we can register lets register")
                customer=Customers.objects.create(customerid = request_data.validated_data['customerid'],firstname = request_data.validated_data['firstname'],lastname = request_data.validated_data['lastname']
                                                  ,company = request_data.validated_data['company'], address = request_data.validated_data['address'], city = request_data.validated_data['city'], state = request_data.validated_data['state'],
                                                  country=request_data.validated_data['country'],postalcode = request_data.validated_data['postalcode'], phone = request_data.validated_data['phone'], fax = request_data.validated_data['fax'],
                                                  email=request_data.validated_data['email'], supportrepid = request_data.validated_data['supportrepid']
                                                  )
                # newcobj.save()
                return Response({"SUCCESS": True, "status_code": 1,
                                 "message": 'Customer enrolled!'},
                                status=status.HTTP_200_OK)
        except Exception as error:
                print("exception | {}".format(error))
                return Response({"SUCCESS": False, "status_code": 0,
                                 "message": 'Something went wrong while Fetching',
                                 }, status=status.HTTP_200_OK)


class GetPeopleByNation(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self,request):
        active_database = 'default'
        request_data = GetPeopleByNationS(data=request.data)
        if request_data.is_valid():
            country = request_data.validated_data['country']
        from trackart.models import Customers
        from trackart.models import Employees
        try:
            customerslist = Customers.objects.using(active_database).filter(country=country).values()
            employeeslist = Employees.objects.using(active_database).filter(country=country).values()
            print("result",list(customerslist))
            return Response({"SUCCESS": True, "status_code": 1,
                                     "message": 'Fetch',
                                     "customers": list(customerslist),"employees":list(employeeslist)}, status=status.HTTP_200_OK)
        except Exception as error:
            print("exception | {}".format(error))
            return Response({"SUCCESS": False, "status_code": 0,
                             "message": 'Not Fetch',
                             }, status=status.HTTP_200_OK)


