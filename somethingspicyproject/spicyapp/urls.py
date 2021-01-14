from django.urls import path

from . import views
urlpatterns = [
    # login / reg page
    path('', views.index),
    # login/reg functions
    path('register', views.register),
    path('login', views.login),
    # Success page
    path('main', views.main_page),
    # videos page
    path('videos', views.videos),
    path('unlike/<int:id>/<int:done>', views.unlike),
    path('like/<int:id>/<int:done>', views.like),
    path('unlike2/<int:id>/<int:done>', views.unlike2),
    path('like2/<int:id>/<int:done>', views.like2),
    path('unlike3/<int:id>/<int:done>', views.unlike3),
    path('like3/<int:id>/<int:done>', views.like3),
    path('commentvideo1/<int:id>', views.commentvideo1),
    path('commentvideo2/<int:id>', views.commentvideo2),
    path('commentvideo3/<int:id>', views.commentvideo3),
    # suggestions
    path('suggest/<int:id>',views.suggest),
    #forums
    path('forum', views.forum),

    # logout
    path('logout', views.logout),
]