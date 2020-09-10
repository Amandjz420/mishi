# Mishi

Steps to create the project
## install postgres
## install redis
## git clone
## cd mishi
## create virtualenv and activate it
## pip install -r requirement.txt
## create mishi db in postgres with user you can change in settings
## python manage.py migrate
## python manage.py runserver

### voila!!!!

api : To get product Info
api/product/info/

{
    "product_id": 4539891679299
}


api : To create Orders
api/product/create-order/

{
    "orders": [
        {"id":32011448811587 , "quant": 1},
        {"id":32011448811587 , "quant": 1}
    ]
}

//where id is variant id

