## mongoDB 사용시 command

- 9월 13일 
### terminal에서 
> - use study_data_analytics ;
     - db 선택(변경)
> - db. 
     - db 명령어라 표시
> - db.mycollection(collection이름).insertMany(여러개 삽입);
     - 여러개 삽입할때
        array 형식으로 넣어야함. 
            documents = [
            {"name": "Alice", "age": 25, "city": "Seoul"},
            {"name": "Bob", "age": 30, "city": "Busan"},
            {"name": "Charlie", "age": 35, "city": "Incheon"}
]
        ** Json 형식으로 들어감. 
> - db.mycollection.updateMany({어떤것?}, {어떻게?})
     - ex: name의 Alice → age : 26
        = ({name:Alice}, {age:26})

        - 여기서 mongoDB에다가 $set이라는 명령어를 입력해야 update가 이뤄짐 이때 변경되는 사항 앞에 넣어준다. 
         {$set:{age:26}}
         '$' 이건 mongoDB의 명령어를 쓰기위함. 
         $set : update때 꼭 사용함. 
### mongoDB에서 filter 사용시 
> mongoDB : 약속어
