import pandas as pd
from sklearn import preprocessing
from math import pi
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import matplotlib.pyplot as plt
import random

df = pd.read_csv('/content/데이터완성본_id추가_중복제거.csv', encoding='utf-8')
df.head()

df = df.replace('emt', np.NaN)
df.dropna(axis=0, inplace=True)

# 데이터 정규화
featurelist = df[['valence', 'acousticness', 'danceability', 'energy', 'loudness', 'tempo']]
scaler = preprocessing.MinMaxScaler()
norm_value = scaler.fit_transform(featurelist)
norm_value = pd.DataFrame(norm_value)
norm_value.columns = featurelist.columns
norm_value  # 정규화된 features
norm_value = norm_value.mul(10)

df1 = df[['movie_name', 'year']]
df = pd.concat([df1, norm_value], axis=1)

df.head()

for i in range(0, len(df['movie_name'])):
    labels = norm_value.columns[:]
    num_labels = len(labels)

    angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]  # 각 등분점
    angles += angles[:1]  # 시작점으로 다시 돌아와야하므로 시작점 추가

    my_palette = plt.cm.get_cmap("Set2", len(norm_value.index))

    fig = plt.figure(figsize=(8, 8), dpi=100)
    fig.set_facecolor('white')

    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])][0]

    data = norm_value.iloc[i].tolist()
    data += data[:1]

    ax = plt.subplot(1, 1, 1, polar=True)
    ax.set_theta_offset(pi / 2)  # 시작점
    ax.set_theta_direction(-1)  # 그려지는 방향 시계방향

    plt.xticks(angles[:-1], labels, fontsize=13)  # x축 눈금 라벨
    ax.tick_params(axis='x', which='major', pad=15)  # x축과 눈금 사이에 여백을 준다.

    ax.set_rlabel_position(0)  # y축 각도 설정(degree 단위)
    plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2', '4', '6', '8', '10'], fontsize=10)  # y축 눈금 설정
    plt.ylim(0, 10)

    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')  # 레이더 차트 출력
    ax.fill(angles, data, color=color, alpha=0.4)  # 도형 안쪽에 색을 채워준다.

    plt.title(df['movie_name'][i], size=30, color=color, x=0.5, y=1, ha='center')  # 타이틀은 캐릭터 클래스로 한다.

    plt.tight_layout(pad=5)  # subplot간 패딩 조절
    #  plt.show()
    save_name = df['movie_name'][i] + '_' + str(df['year'][i])
    if '/' in save_name:
        plt.savefig('{}.png'.format(save_name), bbox_inches='tight', pad_inches=0.3)

        pass
    else:
        plt.savefig('/content/drive/MyDrive/graphy/{}.png'.format(save_name), bbox_inches='tight', pad_inches=0.3)
        print(df['movie_name'][i])
