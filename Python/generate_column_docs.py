import os

def generate_docs():
    # Base directory
    base_dir = r"g:\내 드라이브\2026\바이브코딩 게임 20260311"
    output_path = os.path.join(base_dir, "Docs", "column_description.txt")

    descriptions = {
        "id": "Star Database primary key. (각 별의 고유 ID)",
        "hip": "ID in the Hipparcos Catalog. (히파르코스 항성 목록 번호)",
        "hd": "ID in the Henry Draper Catalog. (헨리 드레이퍼 항성 목록 번호)",
        "hr": "ID in the Harvard Revised (Bright Star) Catalog. (브라이트 스타 항성 목록 번호)",
        "gl": "ID in the Gliese Catalog of nearby stars. (글리제 근접 항성 목록 번호)",
        "bf": "Bayer/Flamsteed designation. (바이어/플램스티드 항성 명명법)",
        "proper": "Commonly-used name for the star (e.g., Sirius). (별의 고유 이름 - 예: 시리우스)",
        "ra": "Right Ascension (hours). (적경 - 시간 단위)",
        "dec": "Declination (degrees). (적위 - 도 단위)",
        "dist": "Distance in parsecs. (거리 - 파섹 단위)",
        "pmra": "Proper motion in RA (milliarcseconds/year). (적경 방향 고유 운동 - 밀리초/년)",
        "pmdec": "Proper motion in Dec (milliarcseconds/year). (적위 방향 고유 운동 - 밀리초/년)",
        "rv": "Radial velocity (km/sec). (시선 속도 - km/s)",
        "mag": "Apparent visual magnitude. (겉보기 등급 - 숫자가 작을수록 밝음)",
        "absmag": "Absolute visual magnitude. (절대 등급 - 10파섹 거리에서의 밝기)",
        "spect": "Spectral type (e.g., G2V). (스펙트럼 분류 - 별의 온도와 크기 정보)",
        "ci": "Color index (B-V). (색지수 - 별의 온도를 나타내는 지표)",
        "x, y, z": "Cartesian coordinates in parsecs (Equatorial). (3차원 카테시안 좌표 - 파섹 단위)",
        "vx, vy, vz": "Velocity components in parsecs/year. (3차원 속도 성분 - 파섹/년)",
        "rarad, decrad": "RA and Dec in radians. (적경과 적위를 라디안 값으로 변환한 값)",
        "pmrarad, pmdecrad": "Proper motion in radians/year. (고유 운동을 라디안 단위로 변환한 값)",
        "bayer": "Bayer designation (part of bf). (바이어 명명법 - 그리스 문자 등)",
        "flam": "Flamsteed number (part of bf). (플램스티드 명명법 - 숫자)",
        "con": "Standard abbreviation for constellation (e.g., Ori). (별지기/별자리 약칭 - 예: 오리온자리는 Ori)",
        "comp, comp_primary, base": "Information for binary/multiple star systems. (다중성계 정보)",
        "lum": "Luminosity relative to the Sun. (태양 대비 광도)",
        "var": "Variable star designation. (변광성 명칭)",
        "var_min, var_max": "Magnitude range for variable stars. (변광성의 최소/최대 등급)"
    }

    print(f"Generating column documentation at {output_path}...")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== HYG Database Column Descriptions (Star Gatcha Project) ===\n")
        f.write("Reference: https://github.com/astronexus/HYG-Database\n\n")
        
        for col, desc in descriptions.items():
            f.write(f"- {col.ljust(18)}: {desc}\n")
            
    print("Documentation generated successfully.")

if __name__ == "__main__":
    generate_docs()
