from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView, View

from .forms import CommentForm


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)


class VerifyCaptcha(View):
    def get(self, request):
        captcha_id = CaptchaStore.generate_key()
        return JsonResponse({
            'captcha_id': captcha_id,
            'image_src': captcha_image_url(captcha_id),
        })

    def post(self, request):
        captcha_id = request.POST.get('captcha_id')
        captcha = request.POST.get('captcha')
        captcha = captcha.lower()

        try:
            CaptchaStore.objects.get(response=captcha, hashkey=captcha_id, expiration__gt=timezone.now()).delete()
        except CaptchaStore.DoesNotExist:
            return JsonResponse({'msg': '验证码错误'}, status=400)

        return JsonResponse({})
