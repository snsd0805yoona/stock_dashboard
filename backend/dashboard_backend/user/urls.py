from django.urls import path

from user import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="list_user"),
    path("<int:id>", views.UserDetailView.as_view(), name="get_user_detail"),
]
