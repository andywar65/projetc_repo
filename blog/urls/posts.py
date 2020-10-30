from django.urls import path

from blog.views import (ArticleArchiveIndexView, ArticleYearArchiveView,
    ArticleMonthArchiveView, ArticleDayArchiveView, DetailArticle,
    UserUploadCreateView, AuthorListView, ByAuthorListView, ByUploadListView)
from blog.api.views import (ArticleListCreateAPIView,
    ArticleRetrieveUpdateDestroyAPIView)

app_name = 'blog'
urlpatterns = [
    path('', ArticleArchiveIndexView.as_view(), name = 'post_index'),
    path('<int:year>/', ArticleYearArchiveView.as_view(),
        name = 'post_year'),
    path('<int:year>/<int:month>/', ArticleMonthArchiveView.as_view(),
        name = 'post_month'),
    path('<int:year>/<int:month>/<int:day>/', ArticleDayArchiveView.as_view(),
        name = 'post_day'),
    path('<int:year>/<int:month>/<int:day>/<slug>/', DetailArticle.as_view(),
        name = 'post_detail'),
    path('contributi/', UserUploadCreateView.as_view(),
        name = 'post_upload'),
    path('autori/', AuthorListView.as_view(),
        name = 'post_authors'),
    path('uploads/', AuthorListView.as_view(),
        name = 'post_uploads'),
    path('autori/<username>/', ByAuthorListView.as_view(),
        name = 'post_by_author'),
    path('uploads/<username>/', ByUploadListView.as_view(),
        name = 'upload_by_author'),
    path(route='api/', view=ArticleListCreateAPIView.as_view(),
        name='post_api_list_create'),
    path(route='api/<uuid:uuid>',
        view=ArticleRetrieveUpdateDestroyAPIView.as_view(),
        name='post_api_rud')
    ]
