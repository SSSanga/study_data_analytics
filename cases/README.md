### DDA 특징 및 DDA의 그래프

- 샘플의 정규분포 확인의 필수!!
        → 모집단의 수집 정당성을 확인하기 위함

- 정규분포 = Normal Distribution = Gaussian






<details>
<summary>NHIS DB </summary>

## NHIS DB 


| 변수명    | 변수 설명     | 변수값 설명 | 의견
|-----------|---------------|-----------------------------|--------|
| RN_INDI   | 개인고유번호 | 7자리의 개인 고유번호, 연계코드 |범주-명목형, 분석에 필요함|
| BTH_YYYY  | 출생년도      | 대상자의 출생년도 (1921LE ~ 2015) |날짜형(순서형) 또는 범주형|
| DTH_YYYYMM  | 사망연월    | 사망자의 사망연월, 년월로 표기됨 |날짜형(순서형), 연속형|
| COD1      | 사망원인1     | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 1차 분류로 기재된 코드| 범주형|
| COD2      | 사망원인2     | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 2차 분류(상세 원인)로 기재된 코드 |범주형, 2차 사망 원인|

### 분석 기준 
- 년도별 주요 사망 원인 분석 (그래프_ x:DTH_YYYYMM 년도별 y: COD1 사망원인1 )
- 계절별 주요 사망 원인 분석 (그래프_ x:DTH_YYYYMM (여름, 겨울) y: COD1 사망원인1 )



</details>


<details>
<summary>Recurrence Of Surgery </summary>

## MongoDB: db_medicals



| 변수명 | 변수 설명 | 데이터 타입 | 의견 |
| ------|------|------|------|
| 환자ID | 환자 고유 식별자 | - | - |
| Large Lymphocyte | 대형 림프구 수치 | 수치형 순서형?| 림프구 수치에 따라서 현재 환자의 면역?상태 추측가능_ 수술전 컨디션에 대한 보조기준? |
| Location of herniation | 탈출증의 위치 (디스크터진위치?) | 수치 | 디스크 위치 확인 가능_위치에 따라 수술 접근법이 다르겠나? ( 3_657, 2_563,1_493,4_147,5_34) |
| ODI | Oswestry Disability Index 계산값 (기능장애지수) | 수치, 범주-순서? | 지수에 따라서 심각도 예측 가능, 터진 위치 별 기능장애지수|
| 가족력 | 가족 중 만성 질병 여부  | 수치 ([ 0.,  1., nan])| 가족력 여부에 따라 디스크 환자 확률?|
| 간질성폐질환 | 간질성 폐질환 여부 | 수치 ([0, 1]) | 수술전 컨디션.. |
| 고혈압여부 | 고혈압 여부 | 수치 [0, 1]| 수술전 컨디션.., |
| 과거수술횟수 | 과거 수술 횟수  | 수치 [0, 1, 2, 3] | 이건 전반적인 과거수술 횟수? 수술의 위험도? |
| 당뇨여부 | 당뇨병 여부  | 수치 [0, 1] | - |
| 말초동맥질환여부 | 말초동맥질환 여부 | 수치 [0, 1] | - |
| 빈혈여부 | 빈혈 여부  | 수치 [0, 1] | - |
| 성별 | 환자 성별  | 수치 [2, 1] | - |
| 스테로이드치료 | 스테로이드 치료 여부 | 수치 [1, 0]  | 스테로이드치료에 따라 수술실패 여부 있지 않을까? 그 민감도가 떨어질텐데..? |
| 신부전여부 | 신부전 여부  | 수치 [0, 1] | - |
| 신장 | 환자의 키 | 수치 | - |
| 심혈관질환 | 심혈관 질환 여부  | 수치 [0, 1] | - |
| 암발병여부 | 암 발병 여부  | 수치 [0, 1] | - |
| 연령 | 환자의 나이 | 수치 | - |
| 우울증여부 | 우울증 여부 | 수치 [0, 1, 2] | 우울정도에 따라 디스크 수술 회복 여부 or 디스크 정도? 우울감이 심하면 활동량이 줄어들거나 앉아있거나 누워있는 시간이 많을거같으니까?|
| 입원기간 | 입원한 기간 | 수치 [최소 1, 최대 51] | - |
| 입원일자 | 입원한 날짜 | 날짜 | - |
| 종양진행여부 | 종양 진행 여부  | 수치 [0, 1] | - |
| 직업 | 환자의 직업  | 범주 [자영업, 특수전문직, 운동선수 etc] | 직업별 디스크 터진 부위 or 수술 기법 |
| 체중 | 환자의 체중 | 수치, 선수 | 체중대별로 디스크 수술 환자수 확인 가능 |
| 퇴원일자 | 퇴원한 날짜 | 날짜 | - |
| 헤모글로빈수치 | 혈액 내 헤모글로빈 | 수치 | 수술 전 컨디션 확인 |
| 혈전합병증여부 | 혈전 합병증 여부 | 수치 [0, 1] | 이건 수술 후 일거같음. 연령대별 수술 후 혈전합병증에 걸리는거 볼 수 있을거같음.  |
| 환자통증정도 | 환자의 통증 정도 | 수치 [10,  7,  8,  9,  2,  1,  6,  5,  3,  4] | 연령대별 스테로이드치료여부에 따른 환자 통증 정도? 환자통증은 수술전?수술후?아?  |
| 흡연여부 | 흡연 여부  | 수치 [0, 1] | 흡연 여부에 따른 헤모글로빈수치 |
| 통증기간(월) | 통증 지속 기간(월)  | 수치 | - |
| 수술기법 | 적용된 수술 기법  | 범주 ['TELD', 'IELD', nan] | 연령대에 따른 적용된 수술 기법/디스크터진위치에따른 적용기법/ 질환여부에 따른 적용기법 |
| 수술시간 | 수술 시간 | 수치 | 연령대별 걸리는 수술시간 or 디스크 터진 위치별 걸리는 수술 시간 or 스테로이드  |
| 수술실패여부 | 수술 실패 여부 | 수치 [0, 1] | 성공: 1779/ 실패: 115 |
| 수술일자 | 수술이 수행된 날짜 | 수치 | 기간별 수술이 수행된 날짜_주로 연휴 껴서 할거같으니까ㅋㅋ |
| 재발여부 | 수술 후 재발 여부 | 수치 [0, 1] | 연령대별 재발여부, 디스크터진위치별 재발여부, 수술 기법별 재발여부 |
| 혈액형 | 환자의 혈액형 | 범주형 ['RH+A', 'RH+B', 'RH+O', 'RH+AB'] | 환자 정보 |
| 전방디스크높이(mm) | 전방 디스크 높이(mm) | 수치 | - |
| 후방디스크높이(mm) | 후방 디스크 높이(mm) | 수치 | - |
| 지방축적도 | 지방 축적도 | 수치 | - |
| Instability | 척추 불안정성 |수치 [0, 1] | - |
| MF + ES | MF + ES 미세파열 + 추간판 탈출_디스크 손상의 정도 | 수치 | - |
| Modic change | Modic 변화 | 수치 [3, 0, 2, 1] | - |
| PI | Pain Intensity_ 디스크 관련 통증을 묘사하는 용어로서, 신경근계의 만성적인 염증으로 인한 통증 / 골반과 척추의 기울기 상태를 확인 | 수치 | - |
| PT | PT(혈액검사_혈액응고인자 검사?) Prothrombin Time | 수치 | 만약 혈액 응고인자 검사라면 수술후 지혈 정도를 보고 연령대별 or 디스크 심한 정도 or 수술기법별로 지혈 시간 정도를 볼 수 있을거같음.  |
| Seg Angle(raw) | 디스크의 실제 크기와 형태를 분석_MRI 같은 영상분석/ 디스크 이미지에서 선분의 시작점과 끝점을 연결하여 만든 각도/  각도는 디스크가 탈출한 정도와 연관되어 있으며, 디스크의 차원을 평가하고 환자의 통증을 알아내는 데 도움 or 디스크 수술에서 Seg Angle(raw)는 디스크 조각이 분리된 각도를 나타내는 측정 항목입니다. 이 값은 수술이 원활하게 수행되었는지를 평가하는 데 도움이 됩니다. 일반적으로 Seg Angle(raw) 값이 작을수록 좋으며, 이는 디스크가 조심스럽게 제거되었고 더 적은 조각으로 나뉘었기 때문입니다. Seg Angle(raw) 값이 높을수록 디스크가 불규칙하게 조각나거나 너무 많은 힘이 가해져 부서져 나뉘어졌을 가능성이 있습니다. 따라서 수술 후 이 값을 평가하는 것은 수술 결과의 질을 판단하는 데 중요합니다.| 수치 | - |
| Vaccum disc |  디스크가 수축하여 작아지고, 내부의 액체가 감소하는 상태를 묘사_주변 조직 간의 압력이 저하되어 조직 간 간격이 줄어들고 신경근계 및 혈관에 압력이 가해지는 결과_고연령대 나타나고 후천적 생길수 있음. _수술 기법_!!| 수치 [0: 1787, 1: 107] | 수술 전에 판단하는 걸까?  _고연령대에서 Vaccum disc가 1 많은가?|
| 골밀도 | 환자의 골밀도 | 수치 | 이게 수술전인건가??양수면 뼈의 조밀도가 높음/음수면 뼈의 조밀도가 낮음/ 이게 회복수치인가.. 뭔가..?? |
| 디스크단면적 | 디스크 단면적 | 수치 | 디스크 수술 후 디스크 단면적 수치를 평가한다면 일반적으로 수술의 성공여부나 수술후 디스크 상태를 평가하기 위함. (절대적은아님) |
| 디스크위치 | 디스크 위치 | 수치 [ 4,  5,  3,  2, 45, 25, 12, 34, 23, 11, 10, 35,  1] | ?? 이건 뭐지..? 디스크 문제 위치? 탈출증이랑은 다른건가? |
| 척추이동척도 | 척추 이동 척도 | 면적 | - |
| 척추전방위증 | 척추 전방위증 | 수치 | - | 








</details>


