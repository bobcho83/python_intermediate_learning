# Matplotlib 심화 — 여러 그래프를 한 화면에 그리기 (Subplot 레이아웃 완전 정복)

# 개념 정리
# plt.subplots(rows, cols)  : rows×cols 격자로 서브플롯 생성 — fig와 axes 배열 반환
# axes[r, c]                : 2D 인덱싱으로 각 서브플롯에 접근
# axes.flat                 : 2D axes 배열을 1D로 순회할 때 사용 (zip과 함께 활용)
# plt.subplot(r, c, n)      : 불규칙 격자 — 특정 칸을 합쳐서 넓게 사용할 때
# plt.tight_layout()        : 서브플롯 간 여백 자동 조정 (겹침 방지)
# plt.subplots_adjust()     : hspace(수직 간격), wspace(수평 간격) 수동 조정
# plt.suptitle()            : 전체 figure에 공통 제목 추가 (y= 로 위치 조정)
# ax.grid(True, alpha=0.3)  : 격자선 추가 (alpha로 투명도 조정)

import numpy as np
import matplotlib.pyplot as plt

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
