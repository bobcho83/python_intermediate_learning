# Matplotlib & Seaborn 심화 — Subplot 레이아웃 + 히트맵 완전 정복

여러 그래프를 한 화면에 배치하는 Subplot 레이아웃 패턴과 Seaborn 히트맵을 실습하는 프로젝트입니다.

## 학습 내용

| 섹션 | 주제 |
|------|------|
| 1. 기본 Subplot | `plt.subplots(2, 2)` — 2×2 격자, `axes[r, c]` 인덱싱 |
| 2. 차트 조합 | 1×3 격자에 선 그래프·막대 그래프·산점도 동시 배치 |
| 3. 불규칙 격자 | `plt.subplot(r, c, n)` — 위 2칸 + 아래 전체 폭 레이아웃 |
| 4. 간격·제목 조정 | `axes.flat`, `subplots_adjust`, `suptitle`, `grid` |
| 5. 마케팅 대시보드 | 트래픽·전환율·고객비용·매출 4가지 KPI 한 화면에 |
| 6. 히트맵 (카페) | `sns.heatmap` — 요일 × 시간대별 방문자 패턴 |
| 7. 히트맵 (판매) | 상품 × 지역 판매량, `cmap='RdYlGn'`, `linewidths` |

## 핵심 개념 정리

```python
# Matplotlib Subplot
plt.subplots(rows, cols)      # rows×cols 격자 생성 — fig, axes 반환
axes[r, c]                    # 2D 인덱싱으로 각 서브플롯 접근
axes.flat                     # 2D axes를 1D로 순회 (zip과 함께 활용)
plt.subplot(r, c, n)          # 불규칙 격자 — 칸을 합쳐 넓게 사용
plt.tight_layout()            # 서브플롯 간 여백 자동 조정
plt.subplots_adjust(hspace=0.3, wspace=0.3)   # 간격 수동 조정
plt.suptitle('제목', y=0.995) # 전체 figure 공통 제목
ax.fill_between(x, y, alpha=0.3)  # 선 아래 면적 채우기 — 추세 강조

# Seaborn Heatmap
sns.heatmap(data,
    xticklabels=cols,         # x축 레이블
    yticklabels=rows,         # y축 레이블
    cmap='YlOrRd',            # 색상 팔레트 (노랑→빨강)
    annot=True,               # 셀 내 숫자 표시
    fmt='d',                  # 숫자 포맷 (d=정수, .1f=소수)
    linewidths=0.5,           # 셀 구분선
    cbar_kws={'label': '...'} # 컬러바 레이블
)
```

**주요 색상 팔레트:**
- `YlOrRd` — 노랑 → 주황 → 빨강 (값이 높을수록 진함)
- `RdYlGn` — 빨강(낮음) → 노랑 → 초록(높음)
- `Blues`, `Greens` — 단색 계열

## 실습 데이터

- 4개 상품(A·B·C·D) 2026년 상반기 월별 판매량
- 마케팅 KPI: 웹사이트 트래픽·전환율·고객 획득 비용·매출액
- 카페 방문자: 7요일 × 5시간대 히트맵
- 지역별 판매: 4개 상품 × 6개 지역

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
