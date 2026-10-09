import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post, Comment
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.mail import send_mail
from django.urls import reverse

print("=" * 60)
print("INICIANDO BATERIA DE TESTES: CAPÍTULOS 1, 2 E 3")
print("=" * 60)

# 1. Teste de Conexão com o Banco de Dados (PostgreSQL via Docker)
try:
    user_count = User.objects.count()
    print(f"✅ [Cap 1] Banco de dados conectado com sucesso! (Usuários no sistema: {user_count})")
except Exception as e:
    print(f"❌ [Cap 1] Erro de conexão com o banco: {e}")

# 2. Teste do Modelo Post e Manager Customizado 'published'
try:
    total_posts = Post.objects.count()
    published_posts = Post.published.count()
    print(f"✅ [Cap 1] Modelo Post OK. Total: {total_posts} | Publicados: {published_posts}")
except Exception as e:
    print(f"❌ [Cap 1] Erro no modelo Post ou manager 'published': {e}")

# 3. Teste de URLs e get_absolute_url
try:
    if Post.objects.exists():
        sample_post = Post.published.first() or Post.objects.first()
        url = sample_post.get_absolute_url()
        print(f"✅ [Cap 1] get_absolute_url() funcionando: {url}")
    else:
        print("⚠️ [Cap 1] get_absolute_url() não testado pois não há posts cadastrados.")
except Exception as e:
    print(f"❌ [Cap 1] Erro no get_absolute_url(): {e}")

# 4. Teste de Tags (django-taggit - Capítulo 2)
try:
    tag_count = Tag.objects.count()
    print(f"✅ [Cap 2] Sistema de Tags integrado com sucesso! Total de tags: {tag_count}")
except Exception as e:
    print(f"❌ [Cap 2] Erro no Taggit / Tags: {e}")

# 5. Teste de Comentários (Capítulo 2)
try:
    comment_count = Comment.objects.count()
    print(f"✅ [Cap 2] Sistema de Comentários OK. Total de comentários: {comment_count}")
except Exception as e:
    print(f"❌ [Cap 2] Erro no modelo de Comentários: {e}")

# 6. Teste de Configuração de E-mail (Capítulo 2 - Compartilhamento por e-mail)
try:
    # Apenas valida se as configurações essenciais existem nas settings
    from django.conf import settings
    email_backend = getattr(settings, 'EMAIL_BACKEND', 'Não definido')
    print(f"✅ [Cap 2] Backend de E-mail configurado: {email_backend}")
except Exception as e:
    print(f"❌ [Cap 2] Erro nas configurações de e-mail: {e}")

# 7. Teste de Busca Full-Text do PostgreSQL (Capítulo 3)
try:
    search_vector = SearchVector('title', 'body')
    search_query = SearchQuery('django')
    results = Post.objects.annotate(
        search=search_vector, rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query)
    print(f"✅ [Cap 3] Busca Full-Text do PostgreSQL compilada com sucesso! (Resultados para 'django': {results.count()})")
except Exception as e:
    print(f"❌ [Cap 3] Erro na Busca Full-Text: {e}")

print("=" * 60)
print("BATERIA DE TESTES CONCLUÍDA!")
print("=" * 60)