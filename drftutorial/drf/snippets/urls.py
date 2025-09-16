# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail), 
#     # path('snippets/', views.SnippetList.as_view()),
#     # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     # path('users/', views.UserList.as_view()),
#     # path('users/<int:pk>/', views.UserDetail.as_view()),

#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Router tự động sinh routes
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
