from  django.urls  import path
from  .views  import index,  product_detail

urlpatterns = [
    path('', index, name='index'),  # Shop ilovasining asosiy sahifasi
    path('category/<int:catigorya_id>', index, name='category'),    # Kategoriyaga oid mahsulotlarni ko'rsatish 
    path('detail/<int:product_id>', product_detail,  name='product-detail')
]
