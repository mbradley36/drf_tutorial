### run venv

source venv/bin/activate

### run server

python manage.py runserver 8000

### project setup

python manage.py startapp products
python manage.py makemigrations
python manage.py migrate

### command line

python manage.py shell
Product.objects.create(title="hello world", content="stuff", price=0.00)
Product.objects.all().order_by("?").first()
exit()
