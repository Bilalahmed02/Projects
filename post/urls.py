from django.urls import path
from post.views import ArticleSingleView, ArticleView, ReviewSingleView, ReviewView

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('review/', ReviewView.as_view()),
    path('article/<int:id>', ArticleSingleView.as_view()),
    path('review/<int:id>', ReviewSingleView.as_view()),
]
