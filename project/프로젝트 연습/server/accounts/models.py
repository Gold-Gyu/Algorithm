from django.db import models
from django.contrib.auth.models import AbstractUser

# User 클래스 이름을 직접사용하기 보다는 get user_ model을 불러서 사용한다.
# settings.AUTH_USER_MODEL은 문자열을 가져다 준다.
# get_user_model은 타입을 가져다 준다.
class User(AbstractUser):
    pass
