import bleach
from rest_framework import serializers

from .models import ProdukPost


class ProdukPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProdukPost
        fields = ["id", "nama", "deskripsi", "kategori", "harga", "created_at"]
        read_only_fields = ["id"]

    def validate_nama(self, value):
        sanitized_value = bleach.clean(
            value,
            tags=[],
            strip=True,
        )
        if len(sanitized_value) < 3:
            raise serializers.ValidationError(
                "Nama produk harus lebih dari 3 karakter."
            )
        if len(sanitized_value) > 100:
            raise serializers.ValidationError("Nama produk terlalu panjang.")
        return sanitized_value

    def validate_deskripsi(self, value):
        sanitized_value = bleach.clean(
            value,
            tags=[],
            strip=True,
        )
        return sanitized_value

    def validate_kategori(self, value):
        sanitized_value = bleach.clean(
            value,
            tags=[],
            strip=True,
        )
        if len(sanitized_value) < 3:
            raise serializers.ValidationError(
                "Nama kategori harus lebih dari 3 karakter."
            )
        if len(sanitized_value) > 100:
            raise serializers.ValidationError("Nama kategori terlalu panjang.")
        return sanitized_value

    def validate_harga(self, value):
        if value <= 0:
            raise serializers.ValidationError("Harga harus lebih besar dari 0.")
        return value
