from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('landingpage' , LandingPage.as_view()),

    path('hero', HeroList.as_view()),
    path('hero/create', HeroCreate.as_view()),
    path('hero/update/<int:pk>', HeroUpdate.as_view()),
    path('hero/delete/<int:pk>', HeroDelete.as_view()),

    path('price', PriceList.as_view()),
    path('price/create', PriceCreate.as_view()),
    path('price/update/<int:pk>', PriceUpdate.as_view()),
    path('price/delete/<int:pk>', PriceDelete.as_view()),

    path('service', ServiceList.as_view()),
    path('service/create', ServiceCreate.as_view()),
    path('service/update/<int:pk>', ServiceUpdate.as_view()),
    path('service/delete/<int:pk>', ServiceDelete.as_view()),

    path('portofolio', PortofolioList.as_view()),
    path('portofolio/create', PortofolioCreate.as_view()),
    path('portofolio/update/<int:pk>', PortofolioUpdate.as_view()),
    path('portofolio/delete/<int:pk>', PortofolioDelete.as_view()),

    path('contact', ContactList.as_view()),
    path('contact/create', ContactCreate.as_view()),
    path('contact/delete/<int:pk>', ContactDelete.as_view()),

    path('partnership', PartnershipList.as_view()),
    path('partnership/create', PartnershipCreate.as_view()),
    path('partnership/update/<int:pk>', PartnershipUpdate.as_view()),
    path('partnership/delete/<int:pk>', PartnershipDelete.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)