# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import {{ cookiecutter.project_class }}


@plugin_pool.register_plugin
class {{ cookiecutter.project_class }}Plugin(CMSPluginBase):
    model = {{ cookiecutter.project_class }}
    name = _('{{ cookiecutter.project_name }}')
    admin_preview = False
    render_template = '{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
