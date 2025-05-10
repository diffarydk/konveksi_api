import uuid

from django.db import models


# Create your models here.
class ProdukPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(null=False, blank=False)
    kategori = models.TextField(null=False, blank=False, max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
