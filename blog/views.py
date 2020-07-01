from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


def home(request):
    context = {'posts':Post.objects.all()}
    return render(request, 'blog/home.html', context)

def searchpage(request):
    queryset1= Post.objects.all()
    paginator = Paginator(queryset1, 12)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    return render(request, 'blog/search_page.html',{'queryset':queryset})


def blog_about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    context_object_name = 'queryset' #it defines thelooping variable name
    template_name = 'blog/search_page.html'
    ordering = ['-date_posted']
    paginate_by = 12

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'
    ordering = ['-date_posted']
    paginate_by = 12

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
#it automatically looke for post_detail.html template with context as variable

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content','phonenumber','state','Catagory','district','price', 'userimage', 'userimage2', 'userimage3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#overiding save method to specify the
    #user who submitting the form

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content','phonenumber','state','Catagory','district','price', 'userimage', 'userimage2', 'userimage3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(self, form).form_valid(form)

    def test_func(self):
        #this function checks userpassestexmixin function here
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def bootstrapfilterview(request):
    qs = Post.objects.all()
    title_query = request.GET.get('title')
    catagory_query = request.GET.get('Catagory')
    district_query = request.GET.get('district')
    state_query =request.GET.get('state')
    price_query = request.GET.get('price')

    if title_query !='' and title_query is not None:
        qs = qs.filter(Q(title__icontains=title_query)|Q(content__icontains=title_query)).distinct()
    if catagory_query !='' and catagory_query is not None and             catagory_query !='Catagory':
        qs = qs.filter(Catagory__icontains = catagory_query)
    if district_query != '' and district_query is not None:
        qs = qs.filter(district__icontains=district_query)
    if state_query != '' and state_query is not None and state_query != 'Choose State':
        qs = qs.filter(state__icontains=state_query)
    if price_query !='' and price_query is not None:
        qs = qs.filter(price__lte=price_query)

    queryset2= qs
    paginator = Paginator(queryset2, 12)
    page = request.GET.get('page')
    queryset3 = paginator.get_page(page)
    return render(request,'blog/bootstrap_form.html',{'queryset':queryset3})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)