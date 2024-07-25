from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response

# Combined view untuk LandingPage
class LandingPage(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # Mengambil hero dengan id tertinggi
        latest_hero = Home.objects.latest('id')

        # Mengambil semua harga
        prices = Price.objects.all()

        data = {
            'heroes': HeroSerializer([latest_hero], many=True).data,
            'prices': PriceSerializer(prices, many=True).data
        }
        serializer = CombinedSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# CRUD Hero
class HeroList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HeroSerializer

class HeroCreate(generics.CreateAPIView):
    serializer_class = HeroSerializer
    queryset = Home.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Hero berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class HeroUpdate(generics.RetrieveUpdateAPIView):
    queryset = Home.objects.all()
    serializer_class = HeroSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Hero berhasil diperbarui', 'data': response.data}, status=status.HTTP_200_OK)

class HeroDelete(generics.DestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HeroSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Hero berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Price
class PriceCreate(generics.CreateAPIView):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Harga berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class PriceList(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Harga berhasil diperbarui', 'data': response.data}, status=status.HTTP_200_OK)

class PriceDelete(generics.DestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Harga berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Service
class ServiceCreate(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Service berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Service berhasil diperbarui', 'data': response.data}, status=status.HTTP_200_OK)

class ServiceDelete(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Service berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Portofolio
class PortofolioCreate(generics.CreateAPIView):
    serializer_class = PortofolioSerializer
    queryset = Portofolio.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Portofolio berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class PortofolioList(generics.ListAPIView):
    queryset = Portofolio.objects.all()
    serializer_class = PortofolioSerializer

class PortofolioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Portofolio.objects.all()
    serializer_class = PortofolioSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Portofolio berhasil diperbarui', 'data': response.data}, status=status.HTTP_200_OK)

class PortofolioDelete(generics.DestroyAPIView):
    queryset = Portofolio.objects.all()
    serializer_class = PortofolioSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Portofolio berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Contact
class ContactCreate(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Kontak berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDelete(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Kontak berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)

# CRUD Partnership
class PartnershipCreate(generics.CreateAPIView):
    serializer_class = PartnershipSerializer
    queryset = Partnership.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Partnership berhasil ditambahkan', 'data': response.data}, status=status.HTTP_201_CREATED)

class PartnershipList(generics.ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

class PartnershipUpdate(generics.RetrieveUpdateAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Partnership berhasil diperbarui', 'data': response.data}, status=status.HTTP_200_OK)

class PartnershipDelete(generics.DestroyAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Partnership berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)
