from django.shortcuts import render
from recommand.models import Movie, Ost, movie_recomand, ost_recomand, Movie_rec, ost_movie
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    poster = Movie.objects.all().order_by('movie_id')
    return render(
        request,
        "recommand/index.html",
        {'poster': poster, })


def home(request):
    return render(
        request,
        "recommand/home.html",
        {})


@login_required  # 함수위에 씌워주면 로그인시에만 확인 가능
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # movie_sh = Movie.objects.filter(movie_name__icontains=searched)
        ost_sh = Ost.objects.filter(
            ost_name__icontains=searched
        )

        ost_mv = []
        for ost_mv_id in ost_sh:
            ost_mv.append(ost_mv_id.movie_id_id)

        movie_sh = Movie.objects.filter(
            Q(movie_name__icontains=searched) |
            Q(movie_ger__icontains=searched) |
            Q(movie_dir__icontains=searched) |
            Q(movie_id__in=ost_mv))
        mo_id = []
        for mov_id in movie_sh:
            mo_id.append(mov_id.movie_id)
        forign = Ost.objects.filter(movie_id_id__in=mo_id)

        return render(request, 'recommand/searched.html',
                      {'searched': searched, 'movie_sh': movie_sh, 'forign': forign})
    else:
        return render(request, 'recommand/searched.html', {})


def relist(request, sel_id):
    recom_list = movie_recomand(sel_id)
    re_ost_list = ost_recomand(sel_id)
    rec_mv = Movie.objects.filter(movie_id__in=recom_list)
    rec_ost = Ost.objects.filter(id__in=re_ost_list)
    choose_ost = Ost.objects.get(id=sel_id)
    choose_ost = choose_ost.id
    return render(
        request,
        "recommand/recomlist.html",
        {'rec_mv': rec_mv, 'rec_ost': rec_ost, 'choose_ost': choose_ost})


def thank(request):
    if request.method == 'POST':
        review_list = []
        for i in range(10):
            if request.POST.get('{}_btn'.format(i + 1)) is None:
                review_list.append('no')
            else:
                review_list.append(request.POST.get('{}_btn'.format(i + 1)))

        # mov_rec = Movie_rec()
        for rec in review_list:
            if rec == 'no':
                pass

            else:
                rec = rec.split('_')
                sel_ost = Ost.objects.get(id=rec[0])
                recom_ost = Ost.objects.get(id=rec[1])

                ost_id = sel_ost
                user_id = request.user
                recodation = recom_ost
                review = rec[2]

                same_check = Movie_rec.objects.filter(
                    Q(ost_id=ost_id) &
                    Q(user_id=user_id) &
                    Q(recodation=recodation))
                if same_check.exists():
                    same_check.delete()

                mov_rec = Movie_rec(ost_id=ost_id, user_id=user_id, recodation=recodation, review=review)
                mov_rec.save()

        return render(request, 'recommand/thank.html',
                      {'rev_list': review_list})
    else:
        return render(request, 'recommand/thank.html',
                      {})
