from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView,FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Yaku
from .forms import YakuForm, ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

@method_decorator(login_required, name="dispatch")

class YakuFormView(CreateView):
    form_class = YakuForm
    template_name = "yaku_form.html"
    success_url = reverse_lazy('majanmania:yaku_done')

    def form_valid(self, form):
        yaku_data = form.save(commit=False)
        yaku_data.user = self.request.user
        yaku_data.save()
        return super().form_valid(form)
    
class YakuSuccessView(TemplateView):
    template_name = 'yaku_success.html'
    
class YakubutuView(TemplateView):
    template_name = 'yaku_list.html'

class RuleView(TemplateView):
    template_name = 'rule.html'

class IndexView(ListView):
    queryset = Yaku.objects.order_by('-posted_at')

    template_name = 'index.html'



class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('majanmania:contact')
 
    def from_vaild(self, form):
        name = form.cleaned_date['name']
        email = form.cleaned_date['email']
        title = form.cleaned_date['title']
        message = form.cleaned_date['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:{3}'\
            .format(name, email,message)
        from_email = 'xxxx@gmail.com'
        to_list = ['yingyaqingmu8@gmail.com']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list)
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信され明日。')
        return super().form_valid(form)