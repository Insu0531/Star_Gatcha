# 📜 Star Gatcha 패치노트 (Changelog)

이 프로젝트의 개발 진행 상황과 변경 내역을 기록하는 파일입니다.

## [v0.0.1] - 2026-03-12
### 🌌 데이터 및 인프라 구축 완료
- **[HYG Database](https://github.com/astronexus/HYG-Database)**: 약 12만 개의 실제 별 데이터를 포함하는 `hygdata_v42.csv` 파일 추가.

- **별 등급 시스템 설계**:
    - **A**: 고유 이름이 있는 별 (499개)
    - **B**: 이름은 없으나 천문 기호가 있는 별 (~2,725개)
    - **C**: 일반 번호 식별 별 (~116,402개)

- **개발 환경 최적화**:
    - 폴더 구조 최적화(Data/, Docs/, Python/, Unity/)

- **GitHub 연동**: `Insu0531/Star_Gatcha` 리포지토리 생성 및 초기 데이터 업로드 완료.

- **`stars_sample.txt`**: HYG Database의 별 데이터를 10개까지 샘플링한 텍스트 파일 추가.
- **`generate_column_docs.py`**: Pandas와 AI를 이용하여 각 컬럼의 특성을 분석하고 쉽게 볼 수 있도록 `Docs/column_description.txt` 생성.
---
