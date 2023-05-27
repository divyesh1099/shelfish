from django.shortcuts import render
from .serializers import BookSerializer 
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Book
# Create your views here.
class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    
class BookAPIView(APIView):
    def get_object(self, pk):
            try:
                return Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                raise Http404
            
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = BookSerializer(data)

        else:
            data = Book.objects.all()
            serializer = BookSerializer(data, many=True)

            return Response(serializer.data)
        
    def post(self, request, format=None):
        data = request.data
        serializer = BookSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Todo in the DB
        serializer.save()

        # Return Response to User

        response = Response()

        response.data = {
            'message': 'Book Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        book_to_update = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book_to_update,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated :
            book_to_update.borrowedByUser = request.user.id
            serializer.save()
        response = Response()
        response.data = {
            'message': 'Book Updated Successfully',
            'data': serializer.data
        }
        return response
    
    def delete(self, request, pk, format=None):
        book_to_delete =  Book.objects.get(pk=pk)

        # delete the todo
        if request.user.is_authenticated and ( request.user.is_superuser or request.user.group == 'librarian'):
            book_to_delete.delete()

        return Response({
            'message': 'Book Deleted Successfully'
        })
    
class OrdersView(APIView):
    def get(self, request):  
        return Response({"sub":"Orders","aud":"DCIL","iss":"GeM","data":[{"pgMode":"DCIL","orderId":"GEMC-511687770521106","orderDate":"2023-03-01","acceptedDate":"2023-03-01","orderAmount":"8.00","demandId":"511687770521106","buyerOrg":"Dredging Corporation of India Limited","buyerName":"ShivshankarChoudhury Malhotraanannanan","buyerEmail":"buyerdcil@gov.in","buyerMobile":"9873458715","buyerAddress":"Door 79, Dada Bai Nagar, Bangalore","buyerPincode":"560022","buyerDistrict":"BANGALORE","buyerState":"KARNATAKA","buyerGstn":"","vendorName":"GALAXY ONLINE POWER SYSTEMS PRIVATE LIMITED","vendorAddress":"1,jammu","vendorCode":"GEMPP2334","vendorDistrict":"RITHALA","vendorState":"DELHI","vendorPin":"110085","vendorBankAccountNo":"123456789123456789","vendorBankIfscCode":"SBIN0000676","vendorPan":"AAICA3285B","vendorGstn":"07AGSPG5128K1Z1","vendorUniqueId":"576031","sellerId":"Comp1dda00a5c9a02b0f70744eac880e33ad","supplyOrderNo":"511687770521106","supplyOrderDate":"2023-03-01","designationFinancial":"Test1","ifdConcurrance":"0","ifdDiaryNo":"NA","ifdDiaryDate":"2023-03-01","consignmentDetails":[{"consigneeState":"KARNATAKA","consigneeLastname":"ShivshankarChoudhury Malhotraanannanan","consigneePostId":"M41O_DCIL_DcilZone1_Div-1_Buyer","consigneeMobile":"9873458715","consigneeFname":"ShivshankarChoudhury Malhotraanannanan","items":[{"totalValue":7.68,"unitPrice":2.56,"tdsUnderIncometax":"yes","expectedDeliveryDate":"2023-03-31","productBrand":"Sanity 27","quantityOrdered":3,"productName":"Sanity 27 computer mouse or trackballs","order_item_id":176272,"productCode":"sanity 270a3a250ee53e20b66d31dc86aa1222e9fd1b098f","offering_type":"goods","materialNumber":None,"tdsUnderGst":"yes","quantityUnitType":"pieces"}],"consigneePin":"560022","consigneeAddress":"Door 79, Dada Bai Nagar, Bangalore","consigneeDistrict":"BANGALORE"}],"contractFile":"https:\/\/fulfilment.gemorion.org\/contract\/fds?orderId=bFlYZ0xoYXNOR0pncjllUjBSbUp3QT09","amendedStatus":"0","parentOrderId":"","isMsmeVerified":"true","mseSocialCategory":"","mseGender":"","buyerDep":"Dredging Corporation of India Limited","buyerMin":"Ministry of Shipping","buyerOffice":"DcilZone1","buyerOrgType":"Central Government","prNumber":None,"prDate":None},{"pgMode":"DCIL","orderId":"GEMC-511687767508174","orderDate":"2023-03-01","acceptedDate":"2023-03-01","orderAmount":"8.00","demandId":"511687767508174","buyerOrg":"Dredging Corporation of India Limited","buyerName":"ShivshankarChoudhury Malhotraanannanan","buyerEmail":"buyerdcil@gov.in","buyerMobile":"9873458715","buyerAddress":"Door 79, Dada Bai Nagar, Bangalore","buyerPincode":"560022","buyerDistrict":"BANGALORE","buyerState":"KARNATAKA","buyerGstn":"","vendorName":"GALAXY ONLINE POWER SYSTEMS PRIVATE LIMITED","vendorAddress":"1,jammu","vendorCode":"GEMPP2334","vendorDistrict":"RITHALA","vendorState":"DELHI","vendorPin":"110085","vendorBankAccountNo":"123456789123456789","vendorBankIfscCode":"SBIN0000676","vendorPan":"AAICA3285B","vendorGstn":"07AGSPG5128K1Z1","vendorUniqueId":"576031","sellerId":"Comp1dda00a5c9a02b0f70744eac880e33ad","supplyOrderNo":"511687767508174","supplyOrderDate":"2023-03-01","designationFinancial":"Test1","ifdConcurrance":"0","ifdDiaryNo":"NA","ifdDiaryDate":"2023-03-01","consignmentDetails":[{"consigneeState":"KARNATAKA","consigneeLastname":"ShivshankarChoudhury Malhotraanannanan","consigneePostId":"M41O_DCIL_DcilZone1_Div-1_Buyer","consigneeMobile":"9873458715","consigneeFname":"ShivshankarChoudhury Malhotraanannanan","items":[{"totalValue":7.68,"unitPrice":2.56,"tdsUnderIncometax":"yes","expectedDeliveryDate":"2023-03-31","productBrand":"Sanity 27","quantityOrdered":3,"productName":"Sanity 27 computer mouse or trackballs","order_item_id":176273,"productCode":"sanity 270a3a250ee53e20b66d31dc86aa1222e9fd1b098f","offering_type":"goods","materialNumber":None,"tdsUnderGst":"yes","quantityUnitType":"pieces"}],"consigneePin":"560022","consigneeAddress":"Door 79, Dada Bai Nagar, Bangalore","consigneeDistrict":"BANGALORE"}],"contractFile":"https:\/\/fulfilment.gemorion.org\/contract\/fds?orderId=Um4weEh5aVlyWmxuMVhhdlZwalczZz09","amendedStatus":"0","parentOrderId":"","isMsmeVerified":"true","mseSocialCategory":"","mseGender":"","buyerDep":"Dredging Corporation of India Limited","buyerMin":"Ministry of Shipping","buyerOffice":"DcilZone1","buyerOrgType":"Central Government","prNumber":None,"prDate":None}]}, status=200)


