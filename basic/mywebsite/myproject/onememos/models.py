from django.db import models

# Create your models here.

class Memo(models.Model):
    memo_text = models.CharField(max_length=200)
    # 인스턴스 생성시 날짜가 자동으로 되게끔 auto_now_add=True 설정
    published_date = models.DateTimeField(auto_now_add=True)