# Matplotlib & Seaborn 심화 — Subplot + 히트맵 + 분포도 완전 정복

여러 그래프 배치(Subplot), Seaborn 히트맵 5종, 분포도·박스플롯·바이올린 플롯을 다루는 시각화 심화 프로젝트입니다.

## 학습 내용

| 섹션 | 주제 |
|------|------|
| 1. 기본 Subplot | `plt.subplots(2, 2)` — 2×2 격자, `axes[r, c]` 인덱싱 |
| 2. 차트 조합 | 1×3 격자에 선 그래프·막대 그래프·산점도 동시 배치 |
| 3. 불규칙 격자 | `plt.subplot(r, c, n)` — 위 2칸 + 아래 전체 폭 레이아웃 |
| 4. 간격·제목 조정 | `axes.flat`, `subplots_adjust`, `suptitle`, `grid` |
| 5. 마케팅 대시보드 | 트래픽·전환율·고객비용·매출 4가지 KPI + `fill_between` |
| 6. 히트맵 — 카페 방문자 | 요일 × 시간대별 패턴, `cmap='YlOrRd'` |
| 7. 히트맵 — 지역 판매 | 상품 × 지역 판매량, `cmap='RdYlGn'`, `linewidths` |
| 8. 히트맵 — 상관계수 | `data.corr()`, `cmap='coolwarm'`, `center=0`, `square=True` |
| 9. 히트맵 — 특성 평가 | `cmap='viridis'`, `vmin·vmax`, `linecolor='white'` |
| 10. 히트맵 — 고객 세그먼트 | 세대별 카테고리 구매액, `cmap='BuGn'` |
| 11. 히스토그램 | `hist(bins=20)`, `density=True` + KDE 곡선 (`scipy.stats`) |
| 12. Box Plot | 세로/가로 박스플롯, IQR·이상치 해석 |
| 13. Violin Plot | `sns.violinplot(inner='box')` + `sns.stripplot` 개별 데이터 점 |

## 핵심 개념 정리

```python
# Matplotlib Subplot
plt.subplots(rows, cols)                      # rows×cols 격자 생성
axes[r, c] / axes.flat                        # 2D 인덱싱 / 1D 순회
plt.subplot(r, c, n)                          # 불규칙 격자
plt.tight_layout() / plt.subplots_adjust()    # 여백 자동/수동 조정
ax.fill_between(x, y, alpha=0.3)              # 선 아래 면적 채우기

# Seaborn Heatmap
sns.heatmap(data, annot=True, fmt='d',
    cmap='coolwarm', center=0,
    vmin=-1, vmax=1, square=True,
    linewidths=1, linecolor='white')
data.corr()                                   # 상관계수 행렬

# 분포도
ax.hist(x, bins=20, density=True)             # 히스토그램 (density=True → KDE와 함께)
stats.gaussian_kde(x)                         # scipy KDE 곡선

# Box Plot / Violin Plot
ax.boxplot(data, vert=False)                  # 가로 박스플롯
sns.violinplot(data=df, x='그룹', y='값',
    inner='box')                              # violin 내부 박스플롯
sns.stripplot(color='black', alpha=0.3)       # 개별 데이터 점 겹치기
```

**Box Plot 해석:**
```
최대값 ─ 이상치를 제외한 최대값
  75분위 ┐
         ├ IQR (가운데 50% 데이터)
  25분위 ┘
최소값 ─ 이상치를 제외한 최소값
  ●     ─ 이상치 (IQR × 1.5 바깥)
```

**주요 색상 팔레트 (cmap):**

| cmap | 색상 범위 | 용도 |
|------|-----------|------|
| `YlOrRd` | 노랑 → 주황 → 빨강 | 방문자 수, 트래픽 |
| `RdYlGn` | 빨강 → 노랑 → 초록 | 성과 지표 |
| `coolwarm` | 파랑 ↔ 빨강 | 상관계수 (-1 ~ +1) |
| `viridis` | 보라 → 초록 → 노랑 | 점수/등급 |
| `BuGn` | 파랑 → 초록 | 구매액, 양수 데이터 |

## 파일 구성

```
python_intermediate_learning/
├── python_intermediate_learning.ipynb   # Jupyter 노트북 (실습 원본)
└── python_intermediate_learning.py      # 정리된 Python 스크립트
```

## 실행 방법

```bash
python python_intermediate_learning.py
```
