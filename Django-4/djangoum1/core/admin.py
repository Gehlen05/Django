from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        return queryset.filter(autor=request.user)
