from django.conf.urls import url, include
import blog.views

urlpatterns = [
    url(r'post', blog.views.show_post),
    url(r'$', blog.views.show_all_posts),
]
