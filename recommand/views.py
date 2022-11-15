from django.shortcuts import render, redirect

from recommand.forms import CommentForm
from recommand.models import Movie, Ost, mv_ost_recomand, Movie_rec, Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    poster = Movie.objects.all().order_by("movie_id")
    return render(
        request,
        "recommand/index.html",
        {
            "poster": poster,
        },
    )


def home(request):
    return render(request, "recommand/home.html", {})


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def search(request):
    searched = request.GET["searched"]
    # movie_sh = Movie.objects.filter(movie_name__icontains=searched)
    ost_sh = Ost.objects.filter(ost_name__icontains=searched)

    ost_mv = []
    for ost_mv_id in ost_sh:
        ost_mv.append(ost_mv_id.movie_id_id)

    movie_sh = Movie.objects.filter(
        Q(movie_name__icontains=searched)
        | Q(movie_ger__icontains=searched)
        | Q(movie_dir__icontains=searched)
        | Q(movie_id__in=ost_mv)
    )
    mo_id = []
    for mov_id in movie_sh:
        mo_id.append(mov_id.movie_id)
    forign = Ost.objects.filter(movie_id_id__in=mo_id)

    return render(
        request,
        "recommand/searched.html",
        {"searched": searched, "movie_sh": movie_sh, "forign": forign},
    )


def relist(request, sel_id):
    search_ost = Ost.objects.get(id=sel_id)
    search_movie = Movie.objects.get(movie_id=search_ost.movie_id_id)
    re_mov_list = mv_ost_recomand(sel_id)[0]
    re_ost_list = mv_ost_recomand(sel_id)[1]
    rec_mv = Movie.objects.filter(movie_id__in=re_mov_list)
    rec_ost = Ost.objects.filter(id__in=re_ost_list)
    choose_ost = Ost.objects.get(id=sel_id)
    choose_ost = choose_ost.id
    comment_list = search_ost.comment_set.all()  # search_ost에 대한 댓글목록 얻기 아래랑 같은 의미
    # comment_list = Comment.objects.filter(ost = search_ost)
    comment_form = CommentForm()
    return render(
        request,
        "recommand/recomlist.html",
        {
            "rec_mv": rec_mv,
            "rec_ost": rec_ost,
            "choose_ost": choose_ost,
            "search_ost": search_ost,
            "search_movie": search_movie,
            "comment_list": comment_list,
            "comment_form": comment_form,
        },
    )


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def comment_new(request, ost_id):
    ost_ch = Ost.objects.get(id=ost_id)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.ost = ost_ch
            comment.save()
            redirect_url = f"/recommand/list/{comment.ost_id}"
            return redirect(redirect_url)
    else:
        form = CommentForm()
    return render(
        request,
        "recommand/comment_form.html",
        {
            "form": form,
        },
    )


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def comment_edit(request, ost_id, com_id):
    comment = Comment.objects.get(id=com_id)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            redirect_url = "/accounts/profile/"
            return redirect(redirect_url)
    else:
        form = CommentForm(instance=comment)
    return render(
        request,
        "recommand/comment_form.html",
        {
            "form": form,
        },
    )


@login_required
def comment_delete(request, ost_id, com_id):
    comment = Comment.objects.get(id=com_id)

    # ToDo: delete memory
    if request.method == "POST":
        comment.delete()
        redirect_url = "/accounts/profile/"
        return redirect(redirect_url)
    return render(
        request,
        "recommand/comment_delete.html",
        {
            "comment": comment,
        },
    )


@login_required
def review_delete(request, rev_id):
    wt_mov_rec = Movie_rec.objects.get(id=rev_id)

    # ToDo: delete memory
    if request.method == "POST":
        wt_mov_rec.delete()
        redirect_url = "/accounts/profile/"
        return redirect(redirect_url)
    return render(
        request,
        "recommand/comment_delete.html",
        {
            "wt_mov_rec": wt_mov_rec,
        },
    )


def thank(request):
    if request.method == "POST":
        review_list = []
        for i in range(10):
            if request.POST.get("{}_btn".format(i + 1)) is None:
                review_list.append("no")
            else:
                review_list.append(request.POST.get("{}_btn".format(i + 1)))
        for rec in review_list:
            if rec == "no":
                pass

            else:
                user_id = request.user
                user_name = request.user.username

                rec = rec.split("_")
                sel_ost = Ost.objects.get(id=rec[0])
                recom_ost = Ost.objects.get(id=rec[1])

                ch_ost_id = sel_ost.id
                ch_ost = Ost.objects.get(id=ch_ost_id)
                ch_ost_name = ch_ost.ost_name
                ch_mov_id = ch_ost.movie_id_id
                ch_mov = Movie.objects.get(movie_id=ch_mov_id)
                ch_mov_name = ch_mov.movie_name

                rec_ost_id = recom_ost.id
                rec_ost = Ost.objects.get(id=rec_ost_id)
                rec_ost_name = rec_ost.ost_name
                rec_mov_id = rec_ost.movie_id_id
                rec_mov = Movie.objects.get(movie_id=rec_mov_id)
                rec_mov_name = rec_mov.movie_name

                review = rec[2]

                same_check = Movie_rec.objects.filter(
                    Q(ost_id=ch_ost_id)
                    & Q(user_id=user_id)
                    & Q(rec_ost_name=rec_ost_name)
                )
                if same_check.exists():
                    same_check.delete()

                mov_rec = Movie_rec(
                    ost_id=ch_ost,
                    user_id=user_id,
                    user_name=user_name,
                    ch_ost_name=ch_ost_name,
                    ch_mov_name=ch_mov_name,
                    rec_ost_name=rec_ost_name,
                    rec_mov_name=rec_mov_name,
                    review=review,
                )
                mov_rec.save()

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
    else:
        return render(request, "recommand/thank.html", {})
