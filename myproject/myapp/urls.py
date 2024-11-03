
from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("createpost/categories-add", views.CategoriesAddView.as_view(), name="categories-add"),
    path("createpost/", views.CreatepostView.as_view(), name="createpost"),
    path("postdetail/<int:post_id>", views.PostdetailView.as_view(), name="postdetail"),
    path("postdetail/<int:post_id>/comment/", views.CreateCommentView.as_view(), name="create_comment"),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),

    

]
