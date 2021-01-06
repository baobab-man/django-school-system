# 코드리뷰
### 장고 요청/응답 FLOW
1. tistory 디렉토리 - urls.py - 첫 화면(/blogs/post)에서 첫번째 경로 /blogs 확인
2. include('blogs.urls') : blogs 디렉토리 - urls.py 확인
3. /post 경로 확인 - views.py에 있는 posts_list 함수 확인
4. posts_list 함수 요청 - models.py에 있는 Post 클래스에서 객체를 불러와서 정렬한 데이터를 posts에 변수로 선언
   - order_by('-created_at') : default는 오름차순 정렬, - 가 붙으면 내림차순 정렬
5. 선언한 posts를 반환해주고 templates으로 넘겨줌
6. templates의 posts_list.html에 넘겨준 posts는 템플릿 태그에 의해 for문을 돌면서 화면에 출력됨 
   - {% tag %} : 템플릿태그, 반복문(for문)이나 제어문(if문)을 사용하여 흐름을 제어
   - {{ 변수 }} : 템플릿변수, 뷰에서 템플릿으로 context 전달(함수에서 html문서로 객체를 보내는 수단)
   - {{ 변수 | 필터 }} : 템플릿필터, 템플릿 변수의 값을 특정 형식으로 변환시 사용
### 게시글 생성 FLOW
##### @ : 데코레이터(Decorator)란?
- 함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수
- 함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용
- 함수의 전처리나 후처리에 대한 필요가 있을 때 사용
- 반복을 줄이고 메소드나 함수의 책임을 확장함
- 대상 함수를 wrapping하고, 이 wrapping 된 함수의 앞뒤에 추가적으로 꾸며질 구문들을 정의해서 손쉽게 재사용 가능하게 해주는 것
1. POST 메소드를 이용하여 _get_post 함수로 title이란 키에 해당하는 value값을 넣어줌
   - strip() : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거(공백이 있을시 공백제거)
   - 함수내에서 if문 사용시 긍정문보다 부정문이 먼저 오는 코드가 좋은 코드
   
### 데이터베이스(12월 21일)
##### PK, FK
- PK : 테이블을 각 엔티티를 식별할 수 있는 대표 키, 중복되지 않는 값
- FK : 
##### one to one, one to many, many to many
- 1:1 : 어느 엔티티쪽에서 상대 엔티티를 보더라도 반드시 단 하나씩 관계를 가지는 것
- 1:N : 한 쪽 엔티티가 관계를 맺은 엔티티 쪽의 여러 객체를 가질 수 있는 것
- N:M : 관계를 가진 양쪽 엔티티 모두에서 1:M 관계가 존재할 때
##### schema

### Choice 클래스의 choice_text 생성 후, 필터 검색
    
    
    >>> from polls.models import Question, Choice
    >>> q = Question.objects.all().first()
    >>> q.choice_set.all() # choice_set : reverse reference(역참조)
    >>> q.choice_set.create(choice_text='test 1', votes=0)
    >>> q.choice_set.filter(choice_text__contains='test')
    
##### 성능테스트
- 1초를 넘지 않아야함
  - select related, prepatch related
  
##### assertIs(firstValue, secondValue, message)
- 첫 번째 및 두 번째 입력값이 동일한 객체로 평가되는지 여부를 테스트하기 위해 단위 테스트에서 사용되는 단위 테스트 라이브러리
  - 두 입력이 동일한 객체로 평가되면 true를 반환, 그렇지 않으면 false를 반환
##### assertContains(firstValue, text)
- 텍스트가 응답에서 한번 이상 발생하면 참
