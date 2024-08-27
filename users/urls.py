from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import UserModelViewSet

router = SimpleRouter()
router.register("", UserModelViewSet)
app_name = UsersConfig.name

urlpatterns = [] + router.urls
