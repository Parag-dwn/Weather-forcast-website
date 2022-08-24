from django.db import models

# Create your models here.
def post(request):
    country_code=request.POST['country_code']