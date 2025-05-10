from django.urls import path

from . import views

urlpatterns = [
    path(
        "produkpost/",
        views.ProdukPostListCreate.as_view(),
        name="ProdukPost-view-create",
    ),
    path(
        "produkpost/<uuid:pk>/", views.ProdukPostRetUpdateDel.as_view(), name="Update"
    ),
]
