<details>
<summary>TITANIC FROM DISASTER</summary>


#### DDA
| Variable | Definition | Key | Opinion |
| --- | --- | --- | --- |
| passengerid | PassengerId | Numbering | 범주(명목형?), Data확인결과_데이터 사이의 크기와 순서 X |
| survival | Survival | 0 = No, 1 = Yes | 범주형(순서), Data 확인결과_특정기준에 분류 가능 (생존여부)|
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서), Data 확인결과_특정기준에 분류 가능 (등급별) |
| sex | Sex | 'male', 'female' | 범주형(순서), Data 확인결과_특정기준에 분류 가능(성별)|
| Age | Age in years | Number | 수치형(연속), Data 확인결과_ 앞 뒤 연계? 크기별로 나열할수있음.  |
| sibsp | # of siblings / spouses aboard the Titanic | Number | 범주형(순서),Data 확인결과_특정 기준 분류 가능 (형제자매 수) |
| parch | # of parents / children aboard the Titanic | Number | 범주형(순서),Data 확인결과_특정 기준 분류 가능 (부모와 자녀의 동반탑승) |
| ticket | Ticket number | Letter | 범주형(명목?), Data 확인결과_티켓에 중복된 count는 가족일거같음..|
| fare | Passenger fare | Number | 범주형(순서)?, Data 확인결과_특정기준에 분류 가능(티켓가격으로 어린이, 어른 or 등급별 볼수있다?) |
| cabin | Cabin number | Letter | 범주형(순서), Data 확인결과_객실번호? 아..A,B,C,D에 따른 객실 등급들을 볼수있나.. |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(순서), Data 확인결과_특정기준에 분류 가능(탑승항구 위치로 ?) |



</details>


<details>
<summary>Type Of Contract Channel</summary>

#### DDA

| Variable | Definition | Key | Opinion |
| --- | --- | --- | --- |
| id | 고객 id인지 렌탈품목의id인지 | Letter | 범주-명목, 확인결과_..valuecount에서 25777820 이 id가 187이라는데..??일단 id 기준으로 분류 .. ..데이터간 크기와 순서 존재하지 않음. |
| type_of_contract | '렌탈', '멤버십', nan  | Letter | 범주-순서, 확인결과_렌탈 or 멤버십 기준으로 분류  |
| type_of_contract2 | 패키지, 홍보, 개별 등 | Letter | 범주-순서, 확인결과_Promotion과 Normal의 valuecount 많음_ contract2 기준 분류 가능|
| channel | 접근경로 | Letter | 범주-순서, 확인결과_서비스 방문부터 R법인까지 다양한 접근 경로로 기준 분류 가능 |
| datetime | 접근날짜 | Letter | 수치-연속? 확인결과_동일 날짜에 count가 잡힘. 하지만 날짜는 ..연속성?앞뒤 연결됨?음..|
| Term | 계약기간? 60, 12, 36, 39 | Number | 수치-이산?범주-순서, 확인결과_숫자가 정해져 있는데.. 그게 count되는건데 .. 개월수로 나눌수는 있는데 그럼 이것도 범주-순서에도 해당되는거 아닌가? 크기와 순서 존재하는거같은데|
| payment_type | 결제종류 'CMS', '카드이체', '가상계좌', '지로', '무통장' | Letter | 범주-순서, 확인결과_결제 종류로 분류 가능 |
| product | 'K1', 'K3', 'K2', 'K4', 'K6', nan, 'K5' | Letter | 범주-순서, 확인결과_K1 부터 K6 까지 종류 분류 가능, 그에 해당하는 count수도 차이 존재함 |
| amount | 계약금?  | Number | 범주-순서, 확인결과_96900에 잡히는 count수가 많음. 이렇게 되면 금액대로 분류 가능 |
| state | 계약 상황 | Letter | 범주-순서, 확인결과_각 상황이 분류 기준될 듯 |
| overdue_count | 연체횟수? | Number | 수치-이산, 확인결과_잘 모르겠음.. |
| overdue | '없음', '있음', nan | Letter | 범주-순서, 확인결과_없음, 있음으로 나눠지고 countsize로 크고 작음 비교 ..?  |
| credit rating | 금리 | Number | 범주-순서, 확인결과_각 rating을 기준으로 나눌 수 있을거같은...? |
| bank | 은행 | Letter | 범주-명목, 확인결과_근데 순서는 없어도 크기는 있지 않나? 순서가 될수 없을까? 일단 기준이 안보이는데 |
| cancellation | '정상', '해약', nan | Letter | 범주-순서, 확인결과_이게 크기 비교가 가능하잖아? 아.. 모르겠네 볼수록 헷갈리는.. |
| age | 뭐랬지? | Number | 범주-순서, 확인결과_ 연령대를 나눌수있다? |
| Mileage | 마일리지 | Letter | 수치-이산, 확인결과_마일리지를 몇천점대 나눌수있을거같은데.. 아 헷갈리는군..|





</details>
