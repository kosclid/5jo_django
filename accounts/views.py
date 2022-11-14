# 이미 있는 라이브러리들이다...ㅎㅎㅎ

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import SignupForm
from recommand.models import Movie_rec


login = LoginView.as_view(template_name="accounts/login_form.html")

logout = LogoutView.as_view(next_page="/accounts/login/")


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def profile(request):
    user_id = request.user.id
    user_own_review = Movie_rec.objects.filter(user_id=user_id)
    user_name = request.user.username

    return render(
        request,
        "accounts/profile.html",
        {
            "user_own_review": user_own_review,
            "user_name": user_name,
        },
    )


signup = CreateView.as_view(
    form_class=SignupForm,
    success_url="/accounts/login/",  # 회원가입시 login화면으로 ㄱㄱ
    template_name="accounts/signup_form.html",
)
