from django.urls import include, path
from rest_framework import routers
from account import views as account_views
from project import views as project_views

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'teams', account_views.TeamViewSet)
router.register(r'tags', project_views.TagViewSet)
router.register(r'tickets', project_views.TicketViewSet)
router.register(r'projects', project_views.ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
