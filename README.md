# Matplotlib & Seaborn 심화 — Subplot 레이아웃 + 히트맵 완전 정복

여러 그래프를 한 화면에 배치하는 Subplot 레이아웃 패턴과 Seaborn 히트맵 5가지 실전 예제를 다루는 프로젝트입니다.

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

## 핵심 개념 정리

```python
# Matplotlib Subplot
plt.subplots(rows, cols)              # rows×cols 격자 생성 — fig, axes 반환
axes[r, c]                            # 2D 인덱싱으로 각 서브플롯 접근
axes.flat                             # 2D axes를 1D로 순회 (zip과 함께 활용)
plt.subplot(r, c, n)                  # 불규칙 격자 — 칸을 합쳐 넓게 사용
plt.tight_layout()                    # 서브플롯 간 여백 자동 조정
plt.subplots_adjust(hspace=0.3, wspace=0.3)   # 간격 수동 조정
plt.suptitle('제목', y=0.995)         # 전체 figure 공통 제목
ax.fill_between(x, y, alpha=0.3)      # 선 아래 면적 채우기

# Seaborn Heatmap
sns.heatmap(data,
    annot=True,           # 셀 내 숫자 표시
    fmt='d',              # 'd'=정수, '.2f'=소수 2자리
    cmap='coolwarm',      # 색상 팔레트
    center=0,             # 색상 중심값 (상관계수에 필수)
    vmin=-1, vmax=1,      # 색상 범위 고정
    square=True,          # 셀 정사각형
    linewidths=1,         # 셀 구분선 두께
    linecolor='white',    # 셀 구분선 색상
    cbar_kws={'label': '레이블'}
)

data.corr()               # DataFrame 변수 간 상관계수 행렬
```

**주요 색상 팔레트 (cmap):**

| cmap | 색상 범위 | 용도 |
|------|-----------|------|
| `YlOrRd` | 노랑 → 주황 → 빨강 | 방문자 수, 트래픽 |
| `RdYlGn` | 빨강 → 노랑 → 초록 | 성과 지표 (낮음→높음) |
| `coolwarm` | 파랑 ↔ 빨강 | 상관계수 (-1 ~ +1) |
| `viridis` | 보라 → 파랑 → 초록 → 노랑 | 점수/등급 |
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
