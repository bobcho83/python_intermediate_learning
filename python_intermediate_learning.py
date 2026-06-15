# Matplotlib & Seaborn 심화 — Subplot 레이아웃 + 히트맵 + 분포도 완전 정복

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
# sns.violinplot()         : 박스플롯 + KDE 분포를 합친 형태
# inner='box'              : violin 내부에 박스플롯 표시
# sns.stripplot()          : 개별 데이터 점 표시 — violin에 겹쳐서 사용

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
