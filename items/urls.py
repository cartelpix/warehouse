from django.urls import path

from . import views

app_name = "items_app"

urlpatterns = [
    path("items-create-view/", views.ItemCreateView.as_view(), name="items-create-view"),
    path("items-detail-view/<pk>/", views.ItemDetailView.as_view(), name="items-detail-view"),
    path("items-update-view/<pk>/", views.ItemUpdateView.as_view(), name="items-update-view"),
    path("items-delete-view/<pk>/", views.ItemDeleteView.as_view(), name="items-delete-view"),
    path("items-list-view/", views.ItemListView.as_view(), name="items-list-view"),
    path('items/index/', views.index, name="index"),
    path('items/', views.items, name="items"),
    path("company-delete-view/<pk>/", views.CompanyDeleteView.as_view(), name="company-delete-view"),
    path("company-detail-view/<pk>/", views.CompanyDetailView.as_view(), name="company-detail-view"),
    path("company-list-view/", views.CompanyListView.as_view(), name="company-list-view"),
    path("company-model-form-view/", views.CompanyModelFormView.as_view(), name="company-model-form-view"),
    path("company-template-view/", views.CompanyTemplateView.as_view(), name="company-template-view"),
    path("company-update-view/", views.CompanyUpdateView.as_view(), name="company-update-view"),

]