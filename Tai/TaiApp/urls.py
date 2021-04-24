# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('',views.index, name ="index"),
#
# ]

from django.urls import path
from . import views
from .views import HomeView,PackagesView, NairobiView, BigfiveView, BirdView, BeachView, nightView, nakuruView,maraView, maraSixView,maraSevenView, nairobiParkView, book
from django.conf import settings
from django.conf.urls.static import static

app_name = 'TaiApp'
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('packages/', PackagesView.as_view(), name = 'packages'),
    path('packages/nairobi', NairobiView.as_view(), name = 'nairobi'),
    path('packages/big5', BigfiveView.as_view(), name = 'big5'),
    path('packages/birdwatching', BirdView.as_view(), name = 'bird'),
    path('packages/beach', BeachView.as_view(), name = 'beach'),
    path('packages/maasainight', nightView.as_view(), name = 'night'),
    path('packages/nakuru', nakuruView.as_view(), name = 'nakuru'),
    path('packages/mara', maraView.as_view(), name = 'mara'),
    path('packages/mara6', maraSixView.as_view(), name = 'maraSix'),
    path('packages/mara7', maraSevenView.as_view(), name = 'maraSeven'),
    path('packages/nairobipark', nairobiParkView.as_view(), name = 'nairobipark'),
    path('packages/book', views.book, name = 'book'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
