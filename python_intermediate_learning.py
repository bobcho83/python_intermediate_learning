# Matplotlib & Seaborn 심화 + Plotly 인터랙티브 + 종합 프로젝트 — 시각화 완전 정복

# 개념 정리
# plt.subplots(rows, cols)  : rows×cols 격자로 서브플롯 생성 — fig와 axes 배열 반환
# axes[r, c]                : 2D 인덱싱으로 각 서브플롯에 접근
# axes.flat                 : 2D axes 배열을 1D로 순회할 때 사용 (zip과 함께 활용)
# plt.subplot(r, c, n)      : 불규칙 격자 — 특정 칸을 합쳐서 넓게 사용할 때
# plt.tight_layout()        : 서브플롯 간 여백 자동 조정 (겹침 방지)
# plt.subplots_adjust()     : hspace(수직 간격), wspace(수평 간격) 수동 조정
# plt.suptitle()            : 전체 figure에 공통 제목 추가 (y= 로 위치 조정)
# ax.grid(True, alpha=0.3)  : 격자선 추가 (alpha로 투명도 조정)
# ax.fill_between()         : 선 그래프 아래 면적 채우기 — 추세 강조
# sns.heatmap()             : 2D 데이터를 색상으로 표현 — annot=True로 숫자 표시
# cmap                      : 색상 팔레트 — 'YlOrRd'(노랑→빨강), 'RdYlGn'(빨→녹)
# fmt='d'                   : annot 숫자 포맷 — 'd'=정수, '.2f'=소수 2자리
# center=0 / vmin·vmax     : 히트맵 색상 중심값·범위 고정 — 상관계수 시각화에 필수
# square=True              : 각 셀을 정사각형으로 표시
# cmap='coolwarm'          : 파랑(음수) ↔ 빨강(양수) — 상관계수 히트맵에 최적
# cmap='viridis'           : 보라→파랑→초록→노랑 — 점수/등급 데이터에 적합
# cmap='BuGn'              : 파랑→초록 — 구매액 등 양수 데이터에 적합
# data.corr()              : DataFrame 변수 간 상관계수 행렬 계산 (Pandas)
# ax.hist(bins=20)         : 히스토그램 — bins 수로 막대 개수 조절
# density=True             : hist를 빈도 대신 밀도(density)로 표시 — KDE와 함께 쓸 때
# stats.gaussian_kde()     : scipy KDE 곡선 — 분포의 연속 추정선
# ax.boxplot(vert=False)   : 가로 박스플롯 — vert=True(기본)=세로
# sns.boxplot()            : Seaborn 박스플롯 — DataFrame과 x/y 지정으로 그룹 비교 편리
# sns.violinplot()         : 박스플롯 + KDE 분포를 합친 형태
# inner='box'              : violin 내부에 박스플롯 표시
# sns.stripplot()          : 개별 데이터 점 표시 — violin에 겹쳐서 사용
# np.percentile(data, 25)  : 사분위수 계산 — Q1(25%), Q3(75%)
# IQR = Q3 - Q1           : 사분위 범위 — 이상치 기준: Q1-1.5×IQR ~ Q3+1.5×IQR
# go.Figure() / go.Scatter / go.Bar : Plotly 인터랙티브 그래프 객체 생성
# go.Box()                 : Plotly 인터랙티브 박스플롯 — hover로 Q1/Q3/중앙값 확인
# go.Sunburst()            : 계층적 데이터를 원형 트리맵으로 표현 (labels, parents, values)
# fig.add_trace()          : Plotly Figure에 데이터 계열 추가
# fig.update_layout()      : Plotly 레이아웃(제목·축·template) 설정
# hovermode='x unified'    : 마우스 hover 시 같은 x값의 모든 계열 동시 표시
# px.scatter(color=, size=): Plotly Express 산점도 — 색상/크기로 추가 차원 표현
# template='plotly_white'  : Plotly 기본 테마 (흰 배경)
# make_subplots(rows, cols): Plotly 서브플롯 격자 생성 — row/col 지정으로 계열 배치
# fill='tozeroy'           : 선 아래 면적을 0까지 채움 — 누적 그래프 강조
# fig.add_gridspec(r, c)   : Matplotlib GridSpec — 불규칙 크기 서브플롯 레이아웃
# gs[0, :2]                : GridSpec 슬라이싱 — 특정 행/열 범위를 하나의 플롯으로 합침
# ax.twinx()               : 동일 x축에 y축 두 개 — 방문자(막대)+전환율(선) 동시 표현
# ax.axvline()             : 수직 참조선 추가 — 평균, 기준값 표시에 활용
# ax.text(x, y, str)       : 막대 위 값 직접 표시 — bar.get_height()로 y값 추출
# ax.barh()                : 가로 막대 그래프
# patch_artist=True        : boxplot 상자를 색으로 채울 때 필요
# pd.cut(data, bins, labels): 연속값을 구간별 카테고리로 변환 (나이대 분류 등)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 깨짐 방지 설정
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# 공통 데이터: 4개 상품의 상반기 월별 판매량
months    = ['1월', '2월', '3월', '4월', '5월', '6월']
product_a = [100, 120, 115, 140, 160, 180]
product_b = [80,  95,  100, 110, 120, 135]
product_c = [150, 145, 160, 170, 175, 190]
product_d = [90,  110, 105, 125, 140, 155]

# ===== 초급: 기본 Subplot — 2×2 격자 =====

print("=== 1. 기본 Subplot (2×2) ===")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# axes[행, 열] 인덱싱으로 각 칸에 접근

axes[0, 0].plot(months, product_a, marker='o', color='red')
axes[0, 0].set_title('상품 A 판매량')
axes[0, 0].set_ylabel('판매량')

axes[0, 1].plot(months, product_b, marker='s', color='blue')
axes[0, 1].set_title('상품 B 판매량')
axes[0, 1].set_ylabel('판매량')

axes[1, 0].plot(months, product_c, marker='^', color='green')
axes[1, 0].set_title('상품 C 판매량')
axes[1, 0].set_xlabel('월')
axes[1, 0].set_ylabel('판매량')

axes[1, 1].plot(months, product_d, marker='d', color='orange')
axes[1, 1].set_title('상품 D 판매량')
axes[1, 1].set_xlabel('월')
axes[1, 1].set_ylabel('판매량')

plt.tight_layout()
plt.show()

# ===== 중급: 다양한 차트 조합 — 1×3 격자 =====

print("\n=== 2. 다양한 차트 한 화면에 (1×3) ===")
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 선 그래프 — 상품별 추세 비교
axes[0].plot(months, product_a, marker='o', label='상품A')
axes[0].plot(months, product_b, marker='s', label='상품B')
axes[0].set_title('선 그래프: 상품별 비교')
axes[0].legend()

# 막대 그래프 — 나란히 배치 (grouped bar)
x_pos = np.arange(len(months))
width = 0.2
axes[1].bar(x_pos - width/2, product_a, width, label='상품A')
axes[1].bar(x_pos + width/2, product_b, width, label='상품B')
axes[1].set_title('막대 그래프: 상품 A vs B')
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(months)
axes[1].legend()

# 산점도 — A와 B의 상관 관계
axes[2].scatter(product_a, product_b, s=100, alpha=0.6)
axes[2].set_title('산점도: A와 B의 관계')
axes[2].set_xlabel('상품A')
axes[2].set_ylabel('상품B')

plt.tight_layout()
plt.show()

# ===== 고급: 불규칙 격자 + 간격 조정 + 공통 제목 =====

# 불규칙 격자 — 위 2칸 + 아래 1칸(전체 폭)
print("\n=== 3. 불규칙한 격자 구성 ===")
fig = plt.figure(figsize=(12, 8))

ax1 = plt.subplot(2, 2, 1)          # 위 왼쪽
ax1.plot(months, product_a, marker='o', color='red')
ax1.set_title('상품A')

ax2 = plt.subplot(2, 2, 2)          # 위 오른쪽
ax2.plot(months, product_b, marker='s', color='blue')
ax2.set_title('상품B')

ax3 = plt.subplot(2, 1, 2)          # 아래 전체 — 2행 1열의 2번 칸 = 전체 폭
ax3.plot(months, product_a, marker='o', label='상품A')
ax3.plot(months, product_b, marker='s', label='상품B')
ax3.plot(months, product_c, marker='^', label='상품C')
ax3.plot(months, product_d, marker='d', label='상품D')
ax3.set_title('모든 상품 비교')
ax3.legend()
ax3.set_xlabel('월')
ax3.set_ylabel('판매량')

plt.tight_layout()
plt.show()

# 간격 조정 + 공통 제목 + axes.flat 순회
print("\n=== 4. 크기와 간격 조정 ===")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

all_products = [product_a, product_b, product_c, product_d]
colors = ['red', 'blue', 'green', 'orange']
titles = ['상품 A', '상품 B', '상품 C', '상품 D']

# axes.flat — 2D axes를 1D로 순회하여 zip 활용
for ax, product, color, title in zip(axes.flat, all_products, colors, titles):
    ax.plot(months, product, marker='o', color=color, linewidth=2)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylabel('판매량', fontsize=11)
    ax.grid(True, alpha=0.3)   # 격자선 추가

# hspace: 수직 간격 / wspace: 수평 간격
plt.subplots_adjust(hspace=0.3, wspace=0.3)
plt.suptitle('2026년 상반기 상품별 판매 현황', fontsize=16, fontweight='bold', y=0.995)
plt.show()

# ===== 실무 예제: 마케팅 대시보드 — 4가지 KPI 한 화면에 =====

print("\n=== 5. 실무 예제: 마케팅 4가지 지표 ===")
np.random.seed(42)

website_traffic = np.array([1000, 1200, 1100, 1400, 1600, 1800])
conversion_rate = np.array([5.2, 5.8, 5.5, 6.2, 6.5, 7.0])
customer_cost   = np.array([5000, 5200, 4800, 5500, 5800, 6200])
revenue         = np.array([50000, 60000, 55000, 70000, 80000, 95000])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 웹사이트 트래픽 — 막대 그래프
axes[0, 0].bar(months, website_traffic, color='skyblue')
axes[0, 0].set_title('월별 웹사이트 방문자', fontweight='bold')
axes[0, 0].set_ylabel('방문자 수')
axes[0, 0].grid(True, alpha=0.3, axis='y')

# 전환율 — 선 그래프 + fill_between으로 면적 강조
axes[0, 1].plot(months, conversion_rate, marker='o', color='green', linewidth=2)
axes[0, 1].fill_between(range(len(months)), conversion_rate, alpha=0.3, color='green')
axes[0, 1].set_title('월별 전환율', fontweight='bold')
axes[0, 1].set_ylabel('전환율 (%)')
axes[0, 1].grid(True, alpha=0.3)

# 고객 획득 비용
axes[1, 0].bar(months, customer_cost, color='coral')
axes[1, 0].set_title('월별 고객 획득 비용', fontweight='bold')
axes[1, 0].set_xlabel('월')
axes[1, 0].set_ylabel('비용 (원)')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 매출액
axes[1, 1].bar(months, revenue, color='lightgreen')
axes[1, 1].set_title('월별 매출액', fontweight='bold')
axes[1, 1].set_xlabel('월')
axes[1, 1].set_ylabel('매출액 (원)')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.suptitle('2026년 상반기 마케팅 성과 분석', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# ===== Seaborn 히트맵 — 2D 데이터 패턴 시각화 =====

# 예제 1: 요일별 × 시간대별 카페 방문자
print("\n=== 6. 히트맵: 카페 방문자 (요일 × 시간대) ===")

days  = ['월', '화', '수', '목', '금', '토', '일']
hours = ['09시', '12시', '15시', '18시', '21시']

# 방문자 수 행렬 (7일 × 5시간대) → .T 로 (5시간대 × 7일) 변환
cafe_data = np.array([
    [50,  100, 120, 80,  60],   # 월
    [55,  110, 130, 85,  65],   # 화
    [52,  105, 125, 82,  63],   # 수
    [60,  115, 135, 90,  70],   # 목
    [70,  130, 150, 100, 80],   # 금
    [100, 180, 200, 150, 120],  # 토
    [90,  170, 190, 140, 110],  # 일
]).T  # 행=시간대, 열=요일

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(cafe_data,
            xticklabels=days,
            yticklabels=hours,
            cmap='YlOrRd',      # 노랑 → 주황 → 빨강 (값이 높을수록 진함)
            annot=True,          # 각 셀에 숫자 표시
            fmt='d',             # 정수 포맷
            cbar_kws={'label': '방문자 수'},
            ax=ax)
ax.set_title('요일별 × 시간대별 카페 방문자', fontsize=14, fontweight='bold')
ax.set_xlabel('요일')
ax.set_ylabel('시간대')
plt.tight_layout()
plt.show()

# 예제 2: 상품 × 지역 판매량
print("\n=== 7. 히트맵: 상품 × 지역 판매량 ===")

products = ['상품A', '상품B', '상품C', '상품D']
regions  = ['서울', '경기', '인천', '부산', '대구', '대전']

sales_data = np.array([
    [150, 120, 100, 80,  70,  90],
    [100, 130, 90,  100, 110, 95],
    [120, 90,  110, 95,  100, 105],
    [110, 100, 120, 110, 95,  100],
])

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(sales_data,
            xticklabels=regions,
            yticklabels=products,
            cmap='RdYlGn',      # 빨강(낮음) → 노랑 → 초록(높음)
            annot=True,
            fmt='d',
            cbar_kws={'label': '판매량 (개)'},
            linewidths=0.5,      # 셀 구분선
            ax=ax)
ax.set_title('지역별 상품 판매량', fontsize=14, fontweight='bold')
ax.set_xlabel('지역')
ax.set_ylabel('상품')
plt.tight_layout()
plt.show()

# 예제 3: 변수 간 상관계수 히트맵
print("\n=== 8. 히트맵: 마케팅 변수 간 상관계수 ===")

np.random.seed(42)
n_sample = 100
data = pd.DataFrame({
    '웹사이트 트래픽': np.random.randn(n_sample).cumsum(),
    '전환율':          np.random.randn(n_sample).cumsum(),
    '고객 만족도':     np.random.randn(n_sample).cumsum(),
    '판매액':          np.random.randn(n_sample).cumsum(),
    '반복 구매율':     np.random.randn(n_sample).cumsum()
})

correlation_matrix = data.corr()  # Pandas .corr() 로 상관계수 행렬 계산

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix,
            annot=True,
            fmt='.2f',
            cmap='coolwarm',    # 파랑(음수) ↔ 빨강(양수) — 상관계수에 최적
            center=0,           # 색상 중심을 0으로 고정
            vmin=-1, vmax=1,    # 상관계수 범위 고정
            square=True,        # 셀을 정사각형으로
            linewidths=1,
            cbar_kws={'label': '상관계수'},
            ax=ax)
ax.set_title('마케팅 변수 간 상관계수', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 예제 4: 상품별 특성 평가 — viridis 색상 + linecolor
print("\n=== 9. 히트맵: 상품 특성 평가 점수 ===")

product_features = np.array([
    [8, 7, 6, 9, 5],
    [6, 8, 7, 7, 8],
    [7, 6, 8, 6, 7],
    [9, 5, 7, 8, 6]
])
features = ['가격경쟁력', '디자인', '품질', '배송속도', '고객지원']
products_feat = ['상품A', '상품B', '상품C', '상품D']

df_feat = pd.DataFrame(product_features, index=products_feat, columns=features)

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_feat,
            annot=True,
            fmt='d',
            cmap='viridis',         # 보라→파랑→초록→노랑
            vmin=5, vmax=10,
            cbar_kws={'label': '점수 (5~10점)'},
            linewidths=2,
            linecolor='white',      # 셀 구분선 색상
            ax=ax)
ax.set_title('상품별 특성 평가 점수', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 예제 5: 고객 세대별 카테고리 구매 패턴
print("\n=== 10. 히트맵: 고객 세그먼트 × 상품 카테고리 ===")

customer_segments = ['20대', '30대', '40대', '50대', '60대']
categories = ['패션', '전자제품', '식품', '생활용품', '책']

purchase_amount = np.array([
    [150, 200, 80,  100, 50],   # 20대
    [120, 180, 120, 130, 60],   # 30대
    [100, 150, 150, 140, 80],   # 40대
    [80,  120, 140, 160, 100],  # 50대
    [60,  100, 130, 150, 120],  # 60대
])

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(purchase_amount,
            xticklabels=categories,
            yticklabels=customer_segments,
            annot=True,
            fmt='d',
            cmap='BuGn',            # 파랑 → 초록
            cbar_kws={'label': '구매액 (만원)'},
            linewidths=1,
            ax=ax)
ax.set_title('고객 세대별 상품 카테고리 구매액', fontsize=14, fontweight='bold')
ax.set_xlabel('상품 카테고리')
ax.set_ylabel('고객 세대')
plt.tight_layout()
plt.show()

# ===== 분포도·박스플롯·바이올린 플롯 =====

from scipy import stats

np.random.seed(42)
# 고객 100명의 월간 구매액 (정규분포, 최소 10000원)
customer_purchase = np.maximum(np.random.normal(loc=50000, scale=15000, size=100), 10000)

print("\n=== 기초 통계 ===")
print(f"평균: {np.mean(customer_purchase):,.0f}원  /  표준편차: {np.std(customer_purchase):,.0f}원")
print(f"최솟값: {np.min(customer_purchase):,.0f}원  /  최댓값: {np.max(customer_purchase):,.0f}원")

# 히스토그램 — 기본 + KDE 곡선 비교
print("\n=== 11. 히스토그램 (기본 vs KDE) ===")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(customer_purchase, bins=20, color='skyblue', edgecolor='black')
axes[0].set_title('기본 히스토그램')
axes[0].set_xlabel('구매액 (원)')
axes[0].set_ylabel('빈도')
axes[0].grid(True, alpha=0.3, axis='y')

# density=True → 밀도(y축)로 변환해야 KDE 곡선과 스케일 일치
axes[1].hist(customer_purchase, bins=20, color='skyblue', edgecolor='black', density=True, alpha=0.7)
kde = stats.gaussian_kde(customer_purchase)   # KDE: 분포의 연속 추정선
x_range = np.linspace(customer_purchase.min(), customer_purchase.max(), 100)
axes[1].plot(x_range, kde(x_range), 'r-', linewidth=2, label='KDE')
axes[1].set_title('KDE 곡선이 있는 히스토그램')
axes[1].set_xlabel('구매액 (원)')
axes[1].set_ylabel('밀도')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# Box Plot — 세로 vs 가로
print("\n=== 12. Box Plot (세로 vs 가로) ===")
product_a_sales = np.random.normal(loc=100, scale=25, size=50)
product_b_sales = np.random.normal(loc=120, scale=20, size=50)
product_c_sales = np.random.normal(loc=90,  scale=30, size=50)
box_data = [product_a_sales, product_b_sales, product_c_sales]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].boxplot(box_data, labels=['상품A', '상품B', '상품C'])
axes[0].set_title('세로 Box Plot')
axes[0].set_ylabel('판매액')
axes[0].grid(True, alpha=0.3, axis='y')

axes[1].boxplot(box_data, labels=['상품A', '상품B', '상품C'], vert=False)  # vert=False → 가로
axes[1].set_title('가로 Box Plot')
axes[1].set_xlabel('판매액')
axes[1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.show()

# Box Plot 구조 설명
print("""
[Box Plot 해석]
  최대값 ─ 이상치를 제외한 최대값
        |
  75분위 ┐
         ├ 가운데 50% 데이터 (IQR)
  25분위 ┘
        |
  최소값 ─ 이상치를 제외한 최소값
  ● 점    ─ 이상치 (IQR × 1.5 바깥)
""")

# Violin Plot — Box Plot + KDE 분포를 합친 형태
print("\n=== 13. Violin Plot ===")
plot_data = pd.DataFrame({
    '판매액': np.concatenate([product_a_sales, product_b_sales, product_c_sales]),
    '상품':   ['상품A']*50 + ['상품B']*50 + ['상품C']*50
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.violinplot(data=plot_data, x='상품', y='판매액', ax=axes[0])
axes[0].set_title('Violin Plot')
axes[0].grid(True, alpha=0.3, axis='y')

# inner='box' → violin 내부에 박스플롯 / stripplot → 개별 데이터 점 겹쳐 표시
sns.violinplot(data=plot_data, x='상품', y='판매액', ax=axes[1], inner='box')
sns.stripplot(data=plot_data, x='상품', y='판매액', ax=axes[1], color='black', alpha=0.3, size=3)
axes[1].set_title('Violin Plot + 개별 데이터')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# ===== 실무 예제: 연령대별 구매액 분포 비교 =====

print("\n=== 14. 연령대별 구매액 분포 (Box vs Violin) ===")
age_20s = np.random.normal(loc=40000, scale=12000, size=50)
age_30s = np.random.normal(loc=55000, scale=15000, size=50)
age_40s = np.random.normal(loc=65000, scale=18000, size=50)
age_50s = np.random.normal(loc=60000, scale=20000, size=50)

purchase_by_age = pd.DataFrame({
    '구매액': np.concatenate([age_20s, age_30s, age_40s, age_50s]),
    '연령대': ['20대']*50 + ['30대']*50 + ['40대']*50 + ['50대']*50
})

fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# sns.boxplot — DataFrame + x/y 지정으로 그룹별 비교 편리
sns.boxplot(data=purchase_by_age, x='연령대', y='구매액', ax=axes[0])
axes[0].set_title('연령대별 구매액 분포 (Box Plot)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('구매액 (원)')
axes[0].grid(True, alpha=0.3, axis='y')

sns.violinplot(data=purchase_by_age, x='연령대', y='구매액', ax=axes[1])
axes[1].set_title('연령대별 구매액 분포 (Violin Plot)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('구매액 (원)')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# ===== 이상치 탐지 — IQR 방법 =====

print("\n=== 15. 이상치 탐지 (IQR 방법) ===")
outlier_data = np.concatenate([
    np.random.normal(loc=50000, scale=10000, size=95),
    [200000, 210000, 220000, 230000, 2400000]  # 이상치 5개
])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(outlier_data, bins=30, color='skyblue', edgecolor='black')
axes[0].set_title('이상치가 포함된 데이터 (히스토그램)')
axes[0].set_xlabel('값')
axes[0].set_ylabel('빈도')

axes[1].boxplot(outlier_data)
axes[1].set_title('이상치가 포함된 데이터 (Box Plot)')
axes[1].set_ylabel('값')
axes[1].grid(True, alpha=0.3, axis='y')

# IQR 이상치 기준 계산: Q1 - 1.5×IQR ~ Q3 + 1.5×IQR 바깥이 이상치
Q1 = np.percentile(outlier_data, 25)
Q3 = np.percentile(outlier_data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = outlier_data[(outlier_data < lower_bound) | (outlier_data > upper_bound)]
print(f"정상 범위: {lower_bound:,.0f} ~ {upper_bound:,.0f}원")
print(f"이상치 개수: {len(outliers)}개  /  값: {sorted(outliers.astype(int))}")

plt.tight_layout()
plt.show()

# ===== Plotly 인터랙티브 그래프 =====

import plotly.graph_objects as go
import plotly.express as px

months_p    = ['1월', '2월', '3월', '4월', '5월', '6월']
product_a_p = [100, 120, 115, 140, 160, 180]
product_b_p = [80,  95,  100, 110, 120, 135]
product_c_p = [150, 145, 160, 170, 175, 190]

# 인터랙티브 선 그래프 — hover로 값 확인, 범례 클릭으로 계열 on/off
print("\n=== 16. Plotly 인터랙티브 선 그래프 ===")
fig_p = go.Figure()
for name, data, color in [('상품A', product_a_p, 'red'), ('상품B', product_b_p, 'blue'), ('상품C', product_c_p, 'green')]:
    fig_p.add_trace(go.Scatter(
        x=months_p, y=data,
        mode='lines+markers',
        name=name,
        line=dict(color=color, width=2),
        marker=dict(size=8)
    ))
fig_p.update_layout(
    title='2026년 상반기 상품별 판매량',
    xaxis_title='월', yaxis_title='판매량',
    hovermode='x unified',   # 같은 x값의 모든 계열을 한 번에 표시
    template='plotly_white'
)
fig_p.show()

# 인터랙티브 막대 그래프 — text=values로 막대 위 값 자동 표시
print("\n=== 17. Plotly 인터랙티브 막대 그래프 ===")
categories_p = ['상품A', '상품B', '상품C', '상품D', '상품E']
values_p     = [150, 120, 180, 90, 110]

fig_p2 = go.Figure(data=[go.Bar(
    x=categories_p,
    y=values_p,
    marker=dict(color=['red', 'blue', 'green', 'orange', 'purple']),
    text=values_p,
    textposition='auto',
    hovertemplate='<b>%{x}</b><br>판매량: %{y}개<extra></extra>'
)])
fig_p2.update_layout(title='상품별 6월 판매량', xaxis_title='상품', yaxis_title='판매량', template='plotly_white')
fig_p2.show()

# 인터랙티브 산점도 — color=그룹, size=연속값으로 3차원 정보 표현
print("\n=== 18. Plotly 인터랙티브 산점도 ===")
np.random.seed(42)
n_customers  = 100
customer_age = np.random.randint(20, 70, n_customers)
purchase_amt = customer_age * 1000 + np.random.normal(0, 20000, n_customers)
loyalty      = np.random.rand(n_customers)
age_group    = ['20대' if a < 30 else '30대' if a < 40 else '40대' if a < 50 else '50대' if a < 60 else '60대'
                for a in customer_age]

df_scatter = pd.DataFrame({'age': customer_age, 'purchase': purchase_amt, 'loyalty': loyalty, 'age_group': age_group})

fig_p3 = px.scatter(
    df_scatter,
    x='age', y='purchase',
    color='age_group',       # 그룹별 색상 자동 지정
    size='loyalty',          # 충성도 → 점 크기
    hover_data={'loyalty': ':.2f'},
    title='고객 나이 vs 구매액 (크기=충성도)',
    labels={'age': '고객 나이', 'purchase': '구매액 (원)'},
    template='plotly_white'
)
fig_p3.show()

# Plotly 인터랙티브 Box Plot — hover로 Q1/중앙값/Q3 자동 표시
print("\n=== 19. Plotly 인터랙티브 Box Plot ===")
np.random.seed(42)
age_20s_b = np.random.normal(40000, 12000, 50)
age_30s_b = np.random.normal(55000, 15000, 50)
age_40s_b = np.random.normal(65000, 18000, 50)

fig_box = go.Figure()
for name, data, color in [('20대', age_20s_b, 'red'), ('30대', age_30s_b, 'blue'), ('40대', age_40s_b, 'green')]:
    fig_box.add_trace(go.Box(y=data, name=name, marker=dict(color=color)))

fig_box.update_layout(title='연령대별 구매액 분포', yaxis_title='구매액 (원)', template='plotly_white')
fig_box.show()

# Sunburst Chart — 계층적 데이터를 원형 트리맵으로 표현
print("\n=== 20. Plotly Sunburst Chart (계층적 데이터) ===")
categories_data = pd.DataFrame({
    'category':    ['의류', '의류', '의류', '의류', '전자제품', '전자제품', '전자제품', '식품', '식품', '식품'],
    'subcategory': ['셔츠', '바지', '신발', '액세서리', '스마트폰', '노트북', '태블릿', '음료', '과자', '라면'],
    'sales':       [150, 120, 180, 90, 200, 250, 180, 100, 120, 110]
})

labels  = ['전체'] + list(categories_data['category'].unique()) + list(categories_data['subcategory'])
parents = [''] + ['전체'] * 3 + ['의류'] * 4 + ['전자제품'] * 3 + ['식품'] * 3
values  = ([sum(categories_data['sales'])] +
           [categories_data[categories_data['category'] == cat]['sales'].sum()
            for cat in categories_data['category'].unique()] +
           list(categories_data['sales']))

fig_sun = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    hovertemplate='<b>%{label}</b><br>판매액: %{value}만원<extra></extra>',
    marker=dict(colorscale='RdBu')
))
fig_sun.update_layout(title='상품 카테고리별 판매액 분포', width=800, height=800)
fig_sun.show()

# Plotly make_subplots — 인터랙티브 마케팅 대시보드
print("\n=== 21. Plotly make_subplots 마케팅 대시보드 ===")
from plotly.subplots import make_subplots

np.random.seed(42)
days_d        = list(range(1, 31))
traffic_d     = np.cumsum(np.random.normal(50, 20, 30)) + 500
conv_rate_d   = np.random.uniform(4, 8, 30)
revenue_d     = traffic_d * conv_rate_d * 100

fig_dash = make_subplots(
    rows=2, cols=2,
    subplot_titles=('일일 웹사이트 방문자', '전환율', '일일 매출액', '누적 매출액')
)

fig_dash.add_trace(go.Scatter(x=days_d, y=traffic_d,   name='방문자',   line=dict(color='blue')),   row=1, col=1)
fig_dash.add_trace(go.Scatter(x=days_d, y=conv_rate_d, name='전환율',   line=dict(color='green')),  row=1, col=2)
fig_dash.add_trace(go.Scatter(x=days_d, y=revenue_d,   name='매출액',   line=dict(color='orange')), row=2, col=1)
fig_dash.add_trace(go.Scatter(
    x=days_d, y=np.cumsum(revenue_d),
    name='누적 매출액',
    fill='tozeroy',             # 선 아래 면적을 0까지 채움
    line=dict(color='red')
), row=2, col=2)

for r, c, yt in [(1,1,'명'), (1,2,'%'), (2,1,'원'), (2,2,'원')]:
    fig_dash.update_xaxes(title_text='일', row=r, col=c)
    fig_dash.update_yaxes(title_text=yt,  row=r, col=c)

fig_dash.update_layout(title_text='2026년 6월 마케팅 성과 대시보드', height=800)
fig_dash.show()

# ===== 종합 프로젝트: 온라인 쇼핑몰 마케팅 분석 보고서 =====

print("\n" + "="*70)
print("온라인 쇼핑몰 마케팅 분석 보고서")
print("="*70)

np.random.seed(42)

# 데이터 준비
months_proj   = ['1월', '2월', '3월', '4월', '5월', '6월']
month_num     = np.arange(1, 7)
monthly_sales = np.array([500, 550, 580, 650, 720, 800]) * 10000
monthly_visitors   = np.array([1000, 1100, 1200, 1400, 1600, 1800])
monthly_conversion = np.array([5.2, 5.5, 5.8, 6.2, 6.5, 7.0])

# 고객 200명 데이터
n_customers    = 200
customer_age   = np.clip(np.random.normal(40, 15, n_customers), 20, 70).astype(int)
customer_purchase = np.maximum(15000 * (customer_age / 40) + np.random.normal(0, 20000, n_customers), 20000)
satisfaction   = np.clip(np.random.normal(7.5, 1.5, n_customers), 1, 10)
age_group      = pd.cut(customer_age, bins=[0, 30, 40, 50, 100], labels=['20~30대', '30~40대', '40~50대', '50대+'])

# 상품 카테고리 / 마케팅 채널 데이터
categories_proj  = ['패션', '전자제품', '생활용품', '식품', '책']
category_sales   = np.array([150, 200, 120, 100, 80]) * 10000
channels         = ['검색광고', 'SNS광고', '이메일', '제휴', '직접방문']
channel_visits   = np.array([450, 600, 300, 200, 250])
channel_revenue  = np.array([350, 380, 150, 120, 100]) * 10000

# --- Matplotlib GridSpec 대시보드 ---
print("\n=== 22. 종합 프로젝트 — Matplotlib GridSpec 대시보드 ===")
fig = plt.figure(figsize=(16, 12))
gs  = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

# 1행 왼쪽 2칸: 월별 판매액 추세 (fill_between)
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(month_num, monthly_sales/10000, marker='o', linewidth=2.5, markersize=8, color='darkblue')
ax1.fill_between(month_num, monthly_sales/10000, alpha=0.3, color='skyblue')
ax1.set_title('월별 판매액 추세', fontsize=12, fontweight='bold')
ax1.set_xlabel('월')
ax1.set_ylabel('판매액 (만원)')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(month_num)
ax1.set_xticklabels(months_proj)

# 1행 오른쪽 1칸: 방문자 막대 + 전환율 선 (twinx — 이중 y축)
ax2      = fig.add_subplot(gs[0, 2])
ax2_twin = ax2.twinx()
ax2.bar(month_num, monthly_visitors, color='lightblue', alpha=0.7)
ax2_twin.plot(month_num, monthly_conversion, marker='s', color='red', linewidth=2)
ax2.set_title('방문자 vs 전환율', fontsize=12, fontweight='bold')
ax2.set_ylabel('방문자 수', color='blue')
ax2_twin.set_ylabel('전환율 (%)', color='red')
ax2.set_xticks(month_num)
ax2.set_xticklabels(months_proj)
ax2.grid(True, alpha=0.3, axis='y')

# 2행 왼쪽 2칸: 나이대별 구매액 Box Plot (patch_artist=True로 색상 적용)
ax3 = fig.add_subplot(gs[1, :2])
age_purchase_data = [customer_purchase[age_group == g] for g in age_group.categories]
bp = ax3.boxplot(age_purchase_data, tick_labels=age_group.categories, patch_artist=True)
for patch, color in zip(bp['boxes'], ['red', 'blue', 'green', 'orange']):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)
ax3.set_title('고객 나이대별 구매액 분포', fontsize=12, fontweight='bold')
ax3.set_ylabel('구매액 (원)')
ax3.grid(True, alpha=0.3, axis='y')

# 2행 오른쪽 1칸: 고객 만족도 히스토그램 + axvline 평균선
ax4 = fig.add_subplot(gs[1, 2])
ax4.hist(satisfaction, bins=15, color='purple', alpha=0.7, edgecolor='black')
ax4.axvline(np.mean(satisfaction), color='red', linestyle='--', linewidth=2,
            label=f'평균: {np.mean(satisfaction):.1f}')
ax4.set_title('고객 만족도 분포', fontsize=12, fontweight='bold')
ax4.set_xlabel('만족도 점수')
ax4.set_ylabel('빈도')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

# 3행 왼쪽 2칸: 카테고리별 판매액 막대 + 값 표시
ax5 = fig.add_subplot(gs[2, :2])
colors_cat = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
bars = ax5.bar(categories_proj, category_sales/10000, color=colors_cat, alpha=0.8, edgecolor='black')
ax5.set_title('상품 카테고리별 판매액', fontsize=12, fontweight='bold')
ax5.set_ylabel('판매액 (만원)')
ax5.grid(True, alpha=0.3, axis='y')
for bar in bars:
    h = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., h, f'{int(h)}', ha='center', va='bottom', fontweight='bold')

# 3행 오른쪽 1칸: 마케팅 채널별 ROI 가로 막대
ax6 = fig.add_subplot(gs[2, 2])
channel_roi = channel_revenue / (channel_visits * 5000) * 100
ax6.barh(channels, channel_roi, color='teal', alpha=0.8)
ax6.set_title('마케팅 채널별 ROI', fontsize=12, fontweight='bold')
ax6.set_xlabel('ROI (%)')
ax6.grid(True, alpha=0.3, axis='x')

plt.suptitle('온라인 쇼핑몰 마케팅 성과 대시보드 (Matplotlib)', fontsize=16, fontweight='bold', y=0.995)
plt.show()

# ===== 종합 프로젝트: Plotly 인터랙티브 대시보드 =====

print("\n=== 23. 종합 프로젝트 — Plotly 인터랙티브 대시보드 ===")

fig_plotly = make_subplots(
    rows=2, cols=2,
    subplot_titles=('월별 판매액 추세', '카테고리별 판매액', '나이대별 구매액', '채널별 방문자'),
    specs=[[{'type': 'scatter'}, {'type': 'pie'}], [{'type': 'box'}, {'type': 'bar'}]]
)

# 1. 월별 판매액 (scatter) — row=1, col=1
fig_plotly.add_trace(
    go.Scatter(x=months_proj, y=monthly_sales/10000, mode='lines+markers', name='판매액', line=dict(color='blue', width=3)),
    row=1, col=1
)

# 2. 카테고리별 판매액 (파이차트) — row=1, col=2
fig_plotly.add_trace(
    go.Pie(labels=categories_proj, values=category_sales/10000, name='카테고리'),
    row=1, col=2
)

# 3. 나이대별 구매액 (박스플롯) — specs type='box' → row=2, col=1
age_group_unique = age_group.unique()
for ag in age_group_unique:
    fig_plotly.add_trace(
        go.Box(y=customer_purchase[age_group == ag], name=str(ag)),
        row=2, col=1
    )

# 4. 채널별 방문자 (막대그래프) — specs type='bar' → row=2, col=2
fig_plotly.add_trace(
    go.Bar(x=channels, y=channel_visits, name='방문자', marker=dict(color='teal')),
    row=2, col=2
)

fig_plotly.update_xaxes(title_text='월', row=1, col=1)
fig_plotly.update_xaxes(title_text='채널', row=2, col=2)
fig_plotly.update_yaxes(title_text='판매액 (만원)', row=1, col=1)
fig_plotly.update_yaxes(title_text='구매액 (원)', row=2, col=1)
fig_plotly.update_yaxes(title_text='방문자 수', row=2, col=2)

fig_plotly.update_layout(
    title_text='온라인 쇼핑몰 마케팅 인터랙티브 대시보드 (Plotly)',
    height=800,
    showlegend=True
)

fig_plotly.show()

# ============= 분석 결과 요약 =============

print("\n" + "=" * 70)
print("주요 분석 결과")
print("=" * 70)

growth       = (monthly_sales[-1] - monthly_sales[0]) / monthly_sales[0] * 100
best_cat     = categories_proj[np.argmax(category_sales)]
worst_cat    = categories_proj[np.argmin(category_sales)]
best_ch      = channels[np.argmax(channel_roi)]
most_visit_ch = channels[np.argmax(channel_visits)]

print(f"판매 성과:")
print(f"  총 판매액: {np.sum(monthly_sales):,.0f}원  /  월평균: {np.mean(monthly_sales):,.0f}원  /  성장률: {growth:.1f}%")
print(f"고객 분석:")
print(f"  평균 나이: {np.mean(customer_age):.0f}세  /  평균 구매액: {np.mean(customer_purchase):,.0f}원  /  만족도: {np.mean(satisfaction):.1f}/10점")
print(f"카테고리:")
print(f"  최고: {best_cat} ({np.max(category_sales)/10000:.0f}만원)  /  최저: {worst_cat} ({np.min(category_sales)/10000:.0f}만원)")
print(f"채널:")
print(f"  최고 효율: {best_ch} (ROI {np.max(channel_roi):.1f}%)  /  최다 방문: {most_visit_ch} ({np.max(channel_visits)}명)")
print(f"전환율: 최저 {np.min(monthly_conversion):.1f}% → 최고 {np.max(monthly_conversion):.1f}%  /  평균 {np.mean(monthly_conversion):.1f}%")

print("\n 권장 사항:")
print("  1. SNS 광고 채널 방문자 수 유지 + 전환율 개선")
print("  2. 40~50대 타겟 마케팅 강화 (만족도 높은 층)")
print("  3. 패션 카테고리 확대, 책 카테고리 활성화 방안 모색")
print("  4. 상승 추세 유지 — 현재 전략 고도화")
print("  5. 고객 만족도 7.5점 이상 목표 유지")

print("\n" + "=" * 70)
print("분석 완료")
print("=" * 70)
