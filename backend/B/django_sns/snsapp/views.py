from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Post


# class Home(LoginRequiredMixin, ListView):
class Home(ListView):
    """HOMEページで、ユーザー投稿をリスト表示"""
    model = Post
    template_name = 'list.html'


# class MyPost(LoginRequiredMixin, ListView):
#     """自分の投稿のみ表示"""
#     model = Post
#     template_name = 'list.html'
 
#     def get_queryset(self):
#     #自分の投稿に限定
#         return Post.objects.filter(user=self.request.user)

class DetailPost(LoginRequiredMixin, DetailView):
    """投稿詳細ページ"""
    model = Post
    template_name = 'detail.html'

class CreatePost(LoginRequiredMixin, CreateView):
    """投稿フォーム"""
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """投稿編集ページ"""
    model = Post
    template_name = 'update.html'
    fields = ['title', 'content']

    def get_success_url(self,  **kwargs):
        """編集完了後の遷移先"""
        pk = self.kwargs["pk"]
        return reverse_lazy('detail', kwargs={"pk": pk})
    
    def test_func(self, **kwargs):
        """アクセスできるユーザーを制限"""
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        return (post.user == self.request.user)

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """投稿編集ページ"""
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def test_func(self, **kwargs):
        """アクセスできるユーザーを制限"""
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk=pk)
        return (post.user == self.request.user) 