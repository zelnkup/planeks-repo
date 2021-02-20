from django.views import generic

from schemas.models import Schema


class UserProfileView(generic.TemplateView):
    """
    Главная страница пользователя
    """

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({"schemas": Schema.objects.all()})

        return context
