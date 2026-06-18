# Matplotlib & Seaborn 심화 + Plotly 인터랙티브 — 시각화 완전 정복

Subplot 레이아웃, 히트맵, 분포도·박스플롯·바이올린 플롯, Plotly 인터랙티브 그래프(Box/Sunburst/대시보드)까지 다루는 시각화 심화 프로젝트입니다.

## 학습 내용

| 섹션 | 주제 |
|------|------|
| 1. 기본 Subplot | `plt.subplots(2, 2)` — 2×2 격자, `axes[r, c]` 인덱싱 |
| 2. 차트 조합 | 1×3 격자에 선 그래프·막대 그래프·산점도 동시 배치 |
| 3. 불규칙 격자 | `plt.subplot(r, c, n)` — 위 2칸 + 아래 전체 폭 레이아웃 |
| 4. 간격·제목 조정 | `axes.flat`, `subplots_adjust`, `suptitle`, `grid` |
| 5. 마케팅 대시보드 (Matplotlib) | 트래픽·전환율·고객비용·매출 4가지 KPI + `fill_between` |
| 6. 히트맵 — 카페 방문자 | 요일 × 시간대별 패턴, `cmap='YlOrRd'` |
| 7. 히트맵 — 지역 판매 | 상품 × 지역 판매량, `cmap='RdYlGn'`, `linewidths` |
| 8. 히트맵 — 상관계수 | `data.corr()`, `cmap='coolwarm'`, `center=0`, `square=True` |
| 9. 히트맵 — 특성 평가 | `cmap='viridis'`, `vmin·vmax`, `linecolor='white'` |
| 10. 히트맵 — 고객 세그먼트 | 세대별 카테고리 구매액, `cmap='BuGn'` |
| 11. 히스토그램 | `hist(bins=20)`, `density=True` + KDE 곡선 (`scipy.stats`) |
| 12. Box Plot | 세로/가로 박스플롯, IQR·이상치 구조 해석 |
| 13. Violin Plot | `sns.violinplot(inner='box')` + `sns.stripplot` |
| 14. 연령대별 분포 비교 | `sns.boxplot` + `sns.violinplot` 그룹 비교 |
| 15. 이상치 탐지 | IQR 방법 — `Q1 - 1.5×IQR ~ Q3 + 1.5×IQR` |
| 16. Plotly 선 그래프 | `go.Scatter`, `hovermode='x unified'`, 범례 클릭 on/off |
| 17. Plotly 막대 그래프 | `go.Bar`, `text`, `hovertemplate` |
| 18. Plotly 산점도 | `px.scatter(color=, size=)` — 색상·크기로 3차원 표현 |
| 19. Plotly Box Plot | `go.Box` — hover로 Q1/중앙값/Q3 자동 표시 |
| 20. Plotly Sunburst | `go.Sunburst(labels, parents, values)` — 계층적 데이터 원형 표현 |
| 21. Plotly 대시보드 | `make_subplots(rows, cols)` + `fill='tozeroy'` 누적 면적 |

## 핵심 개념 정리

```python
# Matplotlib Subplot
plt.subplots(rows, cols)                      # 격자 생성
axes.flat                                     # 2D axes → 1D 순회
ax.fill_between(x, y, alpha=0.3)              # 선 아래 면적

# Seaborn Heatmap
sns.heatmap(data, annot=True, fmt='d',
    cmap='coolwarm', center=0, vmin=-1, vmax=1,
    square=True, linewidths=1, linecolor='white')
data.corr()                                   # 상관계수 행렬

# 분포도 / 박스플롯
ax.hist(x, bins=20, density=True)
stats.gaussian_kde(x)                         # KDE 곡선
sns.boxplot(data=df, x='그룹', y='값')
sns.violinplot(inner='box')
sns.stripplot(color='black', alpha=0.3)

# 이상치 탐지 (IQR)
Q1, Q3 = np.percentile(data, 25), np.percentile(data, 75)
IQR = Q3 - Q1
outliers = data[(data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)]

# Plotly 기본
fig = go.Figure()
fig.add_trace(go.Scatter(x=, y=, mode='lines+markers'))
fig.add_trace(go.Bar(x=, y=, text=, hovertemplate='...'))
fig.add_trace(go.Box(y=data, name='그룹'))
fig.update_layout(hovermode='x unified', template='plotly_white')

# Plotly 고급
go.Sunburst(labels=, parents=, values=)       # 계층적 원형 차트
make_subplots(rows=2, cols=2)                 # 인터랙티브 서브플롯 격자
fig.add_trace(..., row=1, col=1)              # 특정 칸에 계열 배치
fill='tozeroy'                                # 선 아래 면적 채움 (누적 강조)
px.scatter(df, color='그룹', size='값')       # Plotly Express 간편 산점도
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
pip install plotly   # Plotly 섹션 실행 시 필요
python python_intermediate_learning.py
```
