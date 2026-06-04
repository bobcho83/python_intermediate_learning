# Matplotlib 심화 — Subplot 레이아웃 완전 정복

여러 그래프를 한 화면에 배치하는 Subplot 레이아웃 4가지 패턴을 실습하는 프로젝트입니다.

## 학습 내용

| 섹션 | 주제 |
|------|------|
| 1. 기본 Subplot | `plt.subplots(2, 2)` — 2×2 격자, `axes[r, c]` 인덱싱 |
| 2. 차트 조합 | 1×3 격자에 선 그래프·막대 그래프·산점도 동시 배치 |
| 3. 불규칙 격자 | `plt.subplot(r, c, n)` — 위 2칸 + 아래 전체 폭 레이아웃 |
| 4. 간격·제목 조정 | `axes.flat`, `subplots_adjust`, `suptitle`, `grid` |

## 핵심 개념 정리

```python
plt.subplots(rows, cols)      # rows×cols 격자 생성 — fig, axes 반환
axes[r, c]                    # 2D 인덱싱으로 각 서브플롯 접근
axes.flat                     # 2D axes를 1D로 순회 (zip과 함께 활용)
plt.subplot(r, c, n)          # 불규칙 격자 — 칸을 합쳐 넓게 사용
plt.tight_layout()            # 서브플롯 간 여백 자동 조정 (겹침 방지)
plt.subplots_adjust(          # 간격 수동 조정
    hspace=0.3,               #   수직 간격
    wspace=0.3                #   수평 간격
)
plt.suptitle('제목', y=0.995) # 전체 figure 공통 제목
ax.grid(True, alpha=0.3)      # 격자선 (alpha로 투명도 조정)
```

## 실습 데이터

4개 상품(A·B·C·D)의 2026년 상반기(1~6월) 월별 판매량 데이터를 활용합니다.

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
