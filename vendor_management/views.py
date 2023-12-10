from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, Count, F
from django.utils import timezone
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class VendorListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)

        completed_orders = vendor.purchaseorder_set.filter(status='completed').select_related('vendor')

        total_completed_orders = completed_orders.count()

        on_time_delivery_rate = (
            completed_orders.filter(delivery_date__lte=F('delivery_date')).count() / total_completed_orders
        ) * 100 if total_completed_orders > 0 else 0

        quality_rating_avg = completed_orders.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))[
            'quality_rating__avg'
        ] or 0

        average_response_time = completed_orders.filter(acknowledgment_date__isnull=False).aggregate(
            Avg(F('acknowledgment_date') - F('issue_date'))
        )['acknowledgment_date__avg'] or 0

        fulfillment_rate = (
            completed_orders.filter(acknowledgment_date__isnull=True).count() / total_completed_orders
        ) * 100 if total_completed_orders > 0 else 0

        return Response({
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        })

    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in vendor_performance view: {e}")
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    try:
        po = PurchaseOrder.objects.get(pk=po_id)

        if not po.acknowledgment_date:
            po.acknowledgment_date = timezone.now()
            po.save()

            # Recalculate average_response_time
            vendor = po.vendor
            avg_response_time = vendor.purchaseorder_set.filter(acknowledgment_date__isnull=False).aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg'] or 0
            vendor.average_response_time = avg_response_time
            vendor.save()

            serializer = PurchaseOrderSerializer(po)
            return Response(serializer.data)

        return Response({'error': 'Acknowledgment already recorded for this purchase order.'}, status=status.HTTP_400_BAD_REQUEST)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in acknowledge_purchase_order view: {e}")
        return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
