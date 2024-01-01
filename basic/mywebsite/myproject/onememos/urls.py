from django.urls import path

from . import views

urlpatterns = [
    # 프로젝트의 urls.py에서 default uri를 지정해줄 것이기 때문에
    # 여기서는 일단 path를 그냥 둔다.
    # 이 urls.py가 API uri를 맡을 것
    path("", views.index, name="index"),
]
