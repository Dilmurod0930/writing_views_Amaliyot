from  django.urls  import path
from  .views  import index,  product_detail

urlpatterns = [
    path('', index, name='index'),  # Shop ilovasining asosiy sahifasi
    path('detail/', product_detail,  name='product-detail')
]
