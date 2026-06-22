# Matplotlib & Seaborn 심화 + Plotly 인터랙티브 + 종합 프로젝트 — 시각화 완전 정복

Subplot 레이아웃, 히트맵, 분포도·박스플롯·바이올린 플롯, Plotly 인터랙티브, GridSpec 종합 대시보드까지 다루는 시각화 심화 프로젝트입니다.

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
| 16. Plotly 선 그래프 | `go.Scatter`, `hovermode='x unified'` |
| 17. Plotly 막대 그래프 | `go.Bar`, `text`, `hovertemplate` |
| 18. Plotly 산점도 | `px.scatter(color=, size=)` — 3차원 표현 |
| 19. Plotly Box Plot | `go.Box` — hover로 Q1/중앙값/Q3 자동 표시 |
| 20. Plotly Sunburst | `go.Sunburst(labels, parents, values)` — 계층적 원형 차트 |
| 21. Plotly 대시보드 | `make_subplots(rows, cols)` + `fill='tozeroy'` |
| **22. 종합 프로젝트** | **GridSpec 6칸 대시보드 — twinx·patch_artist·axvline·barh·text 총집합** |

## 핵심 개념 정리

```python
# Matplotlib Subplot / GridSpec
plt.subplots(rows, cols)                      # 균일 격자
fig.add_gridspec(3, 3, hspace=, wspace=)      # 불규칙 크기 격자
gs[0, :2]                                     # 슬라이싱으로 칸 합치기
ax.twinx()                                    # 이중 y축 (막대+선 동시)
ax.axvline(x, color=, linestyle='--')         # 수직 참조선
ax.text(x, y, str, ha='center', va='bottom')  # 막대 위 값 표시
ax.barh(y, x)                                 # 가로 막대 그래프
ax.boxplot(data, patch_artist=True)           # 박스플롯 색상 채우기
pd.cut(data, bins, labels)                    # 연속값 → 구간 카테고리

# Seaborn
sns.heatmap(data, annot=True, fmt='d', cmap='coolwarm', center=0)
data.corr()                                   # 상관계수 행렬
sns.violinplot(inner='box') + sns.stripplot() # violin + 개별 점

# 이상치 탐지 (IQR)
Q1, Q3 = np.percentile(data, 25), np.percentile(data, 75)
outliers = data[(data < Q1-1.5*(Q3-Q1)) | (data > Q3+1.5*(Q3-Q1))]

# Plotly
go.Figure() → add_trace(go.Scatter/Bar/Box/Sunburst)
fig.update_layout(hovermode='x unified', template='plotly_white')
make_subplots(rows=2, cols=2) → add_trace(..., row=, col=)
fill='tozeroy'                                # 누적 면적 강조
px.scatter(df, color='그룹', size='값')
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
