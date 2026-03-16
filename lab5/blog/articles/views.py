from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article

# Create your views here.

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {"post": post})

'''
Оригинальный вариант из методички с except

from django.http import Http404

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
'''

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404("Создание статей доступно только авторизованным пользователям")

    if request.method == 'POST':
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')

        # Проверяем заполненность полей
        if title and text:
            # Проверяем уникальность заголовка
            if Article.objects.filter(title=title).exists():
                form = {
                    'title': title,
                    'text': text,
                    'errors': 'Статья с таким названием уже существует'
                }
                return render(request, 'create_post.html', {'form': form})
            
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )

            return redirect('get_article', article_id=article.id)
        else:
            # Если поля не заполнены, формируем словарь с ошибкой и возвращаем форму
            form = {
                'title': title,
                'text': text,
                'errors': 'Не все обязательные поля заполнены!'
            }
            return render(request, 'create_post.html', {'form': form})
    else:
        # GET-запрос
        return render(request, 'create_post.html', {})
