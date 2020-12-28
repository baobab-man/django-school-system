# part 1
- 사람들이 투표하고 투표결과를 볼 수 있게 해주는 공식 사이트
- 투표결과를 추가하고, 수정하고, 삭제할 수 있는 admin 사이트


    $ python - django --version
- 장고 버전과 파이썬 버전 맞춤
### 프로젝트 생성
    
    
    $ django-admin startproject mysite
- startproject 생성
    
    
    mysite/
        manage.py/
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
- The outer mysite/ : 프로젝트 컨테이너
- manage.py : command-line utility
- The inner mysite/ : 프로젝트의 파이썬 패키지, 이 안에 있는 파일들을 사용해야 할 때(ex - mysite.urls)  
- mysite/__ init__.py : mysite 디렉토리가 python 패키지로 간주되어야 함을 python 에게 알리는 빈 파일
- mysite/settings.py : 장고 프로젝트의 설정/구성
- mysite/urls.py : 이 장고 프로젝트에 대한 url 선언   
- mysite/asgi.py : 프로젝트를 제공하기 위한 ASGI 호환 웹 서버의 entry-point(코드가 시작될 때 실행이 시작되는 파일)
- mysite/wsgi.py : 프로젝트를 제공하기 위한 WSGI 호환 웹 서버의 entry-point(코드가 시작될 때 실행이 시작되는 파일)
### 개발 서버
    
    
    $ python manage.py runserver
- 웹브라우저에서 http://127.0.0.1:8000을 방문(데이터베이스 migration에 대한 경고 무시)
- 기본적으로 runserver 명령은 포트 8000의 내부 IP에서 개발 서버 시작
- 서버의 포트를 변경하려면 runserver 뒤에 전달 

    
    $ python manage.py runserver 8080
    $ python manage.py runserver 0:8000 # 0은 0.0.0.0의 바로가기
### Polls app 생성
- project ? 특정 웹 사이트에 대한 구성 및 앱 모음
- app ? 웹 로그 시스템, 공개 기록 데이터베이스 또는 소규모 설문 조사 앱과 같은 작업을 수행하는 웹 어플리케이션
- 프로젝트에는 여러 앱이 포함될 수 있음, 앱은 여러 프로젝트에 있을 수 있음

    
    $ python manage.py startapp polls
- polls 디렉토리 생성
    
    
    polls/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
### 첫번째 뷰 작성
- polls/views.py
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
- 뷰를 호출하려면 URL에 매핑해야하고, 이를 위해서는 URLconf가 필요함
    
    
    polls/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
##### Django가 요청을 처리하는 방법
1. django는 사용할 루트 URLconf 모듈을 결정. 일반적으로 ROOT_URLCONF 값이지만, 들어오는 HttpRequest 개체에 urlconf 속성이 있는 경우,
해당 값이 ROOT_URLCONF 대신 사용됨
2. django는 해당 파이썬 모듈을 로드하고 다양한 urlpatterns를 찾음. django.urls.path()와 django.urls.re_path()의 인스턴스들의 리스트여야함
3. django는 각 URL 패턴을 순서대로 실행하고 요청된 URL과 일치하는 첫번째 패턴(path_info와 일치하지 않는)에서 멈춤
4. URL 패턴 중 하나가 일치한다면, django는 파이선 함수나 클래스 기반의 뷰인 주어진 뷰를 가져와 호출함. 이 뷰들은 다음을 따름
   - HttpRequest의 인스턴스
   - 일치하는 URL 패턴이 명명되지 않은 그룹을 포함한다면, 정규표현식의 일치항목이 위치인수로 제공
   - 키워드 인수는 django.urls.path()나 django.urls.re_path()의 부가적인 kwargs 인수에서 구체화된 어떠한 인수에 의해 제공되고, 오버라이드된
   경로 표현식에 의해 일치된 부분들로 구성되어 있음
5. URL 패턴과 일치하지 않을 시 또는 처리과정에서 예외가 발생할 시, django는 적절한 오류처리를 해야함. 
- 오류처리란? Django가 요청된 URL과 일치하는 항목을 찾을 수 없거나 예외가 발생하면 Django는 오류 처리 뷰를 호출
   - handler400 : django.conf.urls.handler400
   - handler403 : django.conf.urls.handler403
   - handler404 : django.conf.urls.handler404
   - handler500 : django.conf.urls.handler500

- polls 디렉토리에 URLconf(url 구성, 파이썬 모듈 : url 경로식과 파이썬 함수간의 매핑)를 만들기 위해서 urls.py를 아래와 같이 작성
- polls/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
- 다음 단계는 polls.urls 모듈에서 URLconf 루트 지점. mysite/urls.py에서, django.urls.include를 import하고 urlpatterns리스트에서
include()를 삽입
- mysite/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
- include()함수는 다른 URLconf들을 참조할 수 있게 해주는 함수, URL들을 바로 실행하기 쉽게 해줌.
- admin.site.urls를 제외하고, 다른 URL 패턴을 참조할때는 항상 include()함수를 사용해야 함음


    $ python manage.py runserver
- http://localhost:8000/polls/로 접속 시, URLconf를 통한 index view를 볼 수 있음

# part 2
데이터베이스 설정, 모델 생성, 장고의 자동생성 관리(admin) 사이트
### 데이터베이스 설정
- default 구성 : SQLite
- 향후 데이터베이스 전환 문제를 피하기 위해서, 확장가능한 데이터베이스 PostgreSQL 등을 사용
  - PostgreSQL : psycopg2 패키지
  - MySQL/MariaDB : mysqlclient
- 다른 데이터베이스를 원할 시, DATABASES 'default'값을 변경
  - ENGINE : django.db.backends.sqlite3, django.db.backends.postgresql, django.db.backends.mysql
  - NAME : default value-> BASE_DIR/'db.sqlite3'
  - USER, PASSWORD, HOST등과 같은 추가 세팅을 해줘야 함 
  - CREATE DATABASE database_name; 실행
  - mysite/settings.py 에서 데이터베이스 생성 권한이 있는지 확인 
- INSTALLED_APPS 포함 앱
  - django.contrib.admin : 관리사이트
  - django.contrib.auth : 인증 시스템
  - django.contrib.contenttypes : 콘텐츠 유형에 대한 프레임워크
  - django.contrib.sessions : 세션 프레임워크
  - django.contrib.messages : 메시징 프레임워크
  - django.contrib.staticfiles: static 파일 관리를 위한 프레임워크
- 애플리케이션 사용 전 데이터베이스에 테이블 생성을 해야 함(마이그레이트)
  - INSTALLED_APPS 설정 확인하고 mysite/settings.py파일의 데이터베이스 설정 및 앱과 함께 제공된 데이터베이스 마이그레이션에 따라 
  필요한 데이터베이스 테이블을 만듦


    $ python manage.py migrate
 
##### DATABASES 설정
- SQLite
    
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }
- 다른 데이터베이스(MySQL, PostgreSQL, MariaDB 등): 추가 연결 매개 변수 필요


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'mydatabaseuser',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
##### INSTALLED_APPS
- default : []
- 장고 설치에서 활성화된 모든 애플리케이션을 지정하는 문자열 목록, 각 문자열은 점으로 구분된 파이썬 경로여야 함
##### Psycopg 
- 가장 널리 사용되는 PostgreSQL 어댑터
- 파이썬 db API 2.0 사양 구현 

### 모델 생성
추가 메타 데이터를 사용하여 데이터베이스 레이아웃을 정의
- 장고는 DRY원칙을 따름(Don't Repeat Yourself), 한 곳에서 데이터 모델을 정의하고 자동으로 데이터 모델을 파생
  - 마이그레이션 포함
- polls 앱에서 두가지 모델 생성
  - Question : 질문지와 게시일자
  - Choice : 선택 텍스트와 투표 집계
- polls/models.py
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey Field를 포함하는 모델 인스턴스(row)도 같이 삭제
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
- 각 모델에는 여러 클래스 변수가 있으며, 각 변수는 모델의 데이터베이스 필드를 나타냄
- 각 필드는 Field 클래스의 인스턴스로 표현됨(각 필드에 어떤 유형의 데이터가 있는지 알려줌)
- 각 Field 인스턴스의 이름은 파이썬 코드와 데이터베이스의 열 이름으로 사용됨
- ex) Question.pub_date, Question.question_text, Choice.question, Choice.choice_text, Choice.votes
- 일부 Field 클래스에는 필수 arguments가 있음. ex) CharField : max_length
- 다양한 선택적 arguments도 가질 수 있음.
  - CharField
  - DateTimeField
  - ForeignKey
  - IntegerField
### 모델 활성화
- 이 앱의 데이터베이스 스키마 생성
- Question과 Choice 객체에 접근하기 위한 파이썬 데이터베이스 액세스 API를 생성
- PollsConfig 클래스의 경로를 INSTALLED_APPS에 추가
- mysite/settings.py
```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
- Django는 polls앱을 포함하게 됨


    $ python manage.py makemigrations polls
- 마이그레이션은 장고가 모델에 대한 변경 사항을 저장하는 방법
- 마이그레이션이 실행되는 SQL : sqlmigrate(마이그레이션 이름을 가져와서 해당 SQL을 반환)


    $ python manage.py sqlmigrate polls 0001
- 다시 migrate를 실행하여 데이터베이스의 해당 모델 테이블 생성
    
    
    $ python manage.py migrate
- 이 migrate 명령은 적용되지 않은 모든 마이그레이션을 가져와 데이터베이스에 있는 스키마와 함 모델의 변경 사항을 실행.
- 마이그레이션은 프로젝트 개발시 모델 변경 가능(테이블 삭제 후 새 테이블 만들 필요 없음), 데이터 손실없이 데이터베이스를 업데이트 하는데 특화 되어있음.
- 모델 변경 3단계
  - models.py에서 모델 변경
  - 변경 사항에 대한 마이그레이션 만들기 위해 $ python manage.py makemigrations 실행
  - 변경 사항을 데이터베이스에 적용하기 위해 $ python manage.py migrate 실행
### API
    
    
    $ python manage.py shell
    >>> from polls.models import Choice, Question
    >>> Question.objects.all()
    <QuerySet []>
    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())
    >>> q.save()
    >>> q.id
    1
    >>> q.question_text
    "What's new?"
    >>> q.pub_date
    datetime.datetime(2020, 12, 18, 7, 2, 24, 448288, tzinfo=<UTC>)
    >>> q.question_text = "What's up???"
    >>> q.save()
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>
- <Question: Question object (1)> : 유용하지 못한 표현
- polls/models.py의 Question 모델 수정 및 Question, Choice 클래스에 __ str__() 메소드 추가
- polls/models.py
```python
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```
- 대화형 프롬프트를 처리시 편리함 뿐만 아니라, 객체의 표현이 장고의 자동 생성 관리자를 통해 쓰이기 때문에 __ str__() 메소드 추가하는것이 중요
- 사용자 지정 메소드 추가
```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```
        
        
    >>> from polls.models import Choice, Question
    >>> Question.objects.all()
    <QuerySet [<Question: What's up???>]>
    >>> Question.objects.filter(id=1)
    <QuerySet [<Question: What's up???>]>
    >>> Question.objects.filter(question_text__startswith='What')
    <QuerySet [<Question: What's up???>]>
    
    >>> from django.utils import timezone
    >>> current_year = timezone.now().year
    >>> Question.objects.get(pub_date__year=current_year)
    <Question: What's up???>
    >>> Question.objects.get(id=2)
    Traceback (most recent call last):
        ...
    DoesNotExist: Question matching query does not exist.
    >>> Question.objects.get(pk=1)
    <Question: What's up???>
    >>> q = Question.objects.get(pk=1)
    >>> q.was_published_recently()
    True
    >>> q = Question.objects.get(pk=1)
    >>> q.choice_set.all()
    <QuerySet []>
    >>> q.choice_set.create(choice_text='Not much', votes=0)
    <Choice: Not much>
    >>> q.choice_set.create(choice_text='The sky', votes=0)
    <Choice: The sky>
    >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
    >>> c.question
    <Question: What's up???>
    >>> q.choice_set.all()
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    >>> q.choice_set.count()
    3
    >>> Choice.objects.filter(question__pub_date__year=current_year)
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
    >>> c.delete()
   
### Django Admin 소개
장고는 모델에 대한 admin 인터페이스 생성을 자동화
##### 관리자 생성
    
    
    $ python manage.py createsuperuser
##### 개발서버 시작
    
    
    $ python manage.py runserver
##### 관리자 사이트 입력
- 수퍼 유저 계정으로 로그인
  - 장고 관리자 색인 페이지가 표시되어야 함
##### admin에서 poll app을 수정가능하게 만들기 
- poll app은 admin 인덱스 페이지에 표지되지 않음
- Question 객체가 admin 인터페이스를 갖고 있음을 admin에게 알려야 함
- polls/admin.py
```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
# part 3
### 뷰 확장
- polls/views.py
```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
- polls/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='datail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
- 새로운 뷰 함수들을 urls 에서 경로연결
- 누군가 페이지를 요청하면, mysite.urls -> polls.urls -> polls.views -> detail()
- polls/views.py
```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```
- polls 디렉토리에 템플릿 디렉토리 생성
- polls/templates/polls/index.html
```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
- index 뷰 업데이트
- polls/views.py
```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))
```
- shortcuts: render()
- polls/views.py
```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```
- render()함수는 request 객체를 첫번째 argument, 템플릿 이름을 두번째 argument, context를 선택적 세번째 argument로 받음
### 404 오류
- detail view
- polls/views.py
```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```
- 요청된 ID가 존재하지 않으면, Http404가 발생함.
- polls/templates/polls/detail.html
```html
{{ question }}
```
- shortcut: get_object_or_404()
- polls/views.py
```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Qustion, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```
### 템플릿 시스템 사용
- polls/templates/polls/detail.html
```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
### 템플릿에서 하드 코딩 된 URL 제거
- polls/index.html
```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
### 네임스페이스 추가
- polls/urls.py
```python
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='datail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
- polls/templates/polls/index.html
```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
# part 4
### 최소한의 form 작성
- polls/templates/polls/detail.html
```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```
- polls/views.py
```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
```
- reverse()는 '/polls/3/results/'와 같은 문자열을 반환
- polls/views.py
```python
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```
- polls/templates/polls/results.html
```html
<h1>{{ question.question_text }}</h1>

<ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
    {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```
### 적은 코드
##### URLconf 수정
- polls/urls.py
```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
##### 뷰 수정
- polls/views.py
```python
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
           })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```
- ListView: 객체 목록 표시
- DetailView: 특정 유형의 객체에 대한 세부 정보 페이지 표시

# models
- 모델의 각 속성은 데이터베이스 필드를 나타냄
- 장고는 자동으로 생성된 데이터베이스 접근 API를 제공
- ex)
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
- first_name과 last_name은 모델의 필드들
- 각 필드는 클래스 속성으로 지정되고 각 속성은 데이터베이스 열에 매핑
```sql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```
- Person 모델의 데이터베이스 테이블 생성
- id 필드는 자동으로 추가 
### 모델 사용하기
- 모델 정의 후, 해당 모델을 사용할 것을 Django에 알려야 함.
- INSTALLED_APPS 설정 변경
```python
INSTALLED_APPS = [
    # ...
    'myapp',
    # ...
]
```
- manage.py migrate -> manage.py makemigrations
### 필드
- 모델에서 가장 중요한 부분과 모델의 유일한 필수부분
- 필드는 클래스 속성으로 지정
- models API의 이름과 겹치면 안됨
```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
##### 필드 유형
- 데이터베이스가 어떤데이터를 저장하는지 알려주는 컬럼 유형 : INTEGER, VARCHAR, TEXT
- 폼 필드를 렌더링할때 쓰이는 기본 HTML 위젯 : <input type="text">, <select>
- 장고의 관리자와 자동생성양식에 사용되는 최소한의 유효성 검사 요구 사항
- 수십 개의 기본 제공 필드 유형 참조
##### 필드 옵션
- 각 필드는 필드 별 arguments의 특정 집합
  - ex) CharField에는 데이터를 저장하는데 사용되는 VARCHAR 데이터베이스 필드의 크기를 지정하는 max_length argument 필요
- null : True이면 장고는 데이터베이스에서 NULL로 저장, 기본값은 False
- blank : True이면 필드는 ""로 저장, 기본값은 False
- choices : choices로서 
```python
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
```
- choices 변경 될 때마다 마다 새 마이그레이션이 생성
- 각 튜플의 첫 번째 요소는 데이터베이스에 저장될 값. 두 번째 요소는 필드의 form 위젯에 의해 표시됨
- 모델 인스턴스가 주어지면, choices 필드값의 표시는 get_FOO_display() 메소드를 사용하여 접근가능
```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),   
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
    
    
    >>> p = Person(name="Fred Flintstone", shirt_size="L")
    >>> p.save()
    >>> p.shirt_size
    'L'
    >>> p.get_shirt_size_display()
    'Large'
```python
from django.db import models

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
```
- primary_key : True이면, 이 필드는 모델의 기본키
- 모델에서 어떤 필드이건 primary_key=True를 설정하지 않으면, 장고는 자동으로 IntegerField를 primary키로 지정
- 기존 객체의 기본 키 값을 변경한 다음 저장하면 이전 객체와 함께 새 객체가 생성
```python
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
```
    
    
    >>> fruit = Fruit.objects.create(name='Apple')
    >>> fruit.name = 'Pear'
    >>> fruit.save()
    >>> Fruit.objects.values_list('name', flat=True)
    <QuerySet ['Apple', 'Pear']>
- unique : True이면, 이 필드는 테이블에서 고유해야한다
##### 자동 기본 키 필드
```python
id = models.AutoField(primary_key=True)
```
- 각 모델에서는 primary_key를 갖는 필드가 하나 필요(명시적으로 선언했든, 자동으로 추가되었든)
##### Verbose field names
##### 관계
- many-to-one 관계 : django.db.models.ForeignKey사용, 다른 필드와 마찬가지로 모델의 클래스 속성으로 포함하여 사용
    - ForeignKey는 모델 관련된 클래스인 위치 argument가 필요
```python
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    company_that_makes_it = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE, 
    )
    # ...
```
```python
from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
```
- 다음은 python API 기능을 사용하여 수행할 수 있는 작업의 예
    - 몇 명의 reporter 만들기
    
    
    >>> r = Reporter(first_name='John', last_name='Smith', email='john@example.com')
    >>> r.save()
    >>> r2 = Reporter(first_name='Paul', last_name='Jones', email='paul@example.com')
    >>> r2.save()
- article 작성
    
    
    >>> from datetime import date
    >>> a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
    >>> a.save()
    >>> a.reporter.id
    1
    >>> a.reporter
    <Reporter: John Smith>
- 외래키관계에 할당하려면 객체를 저장해야 함. 예를 들어 Reporter를 저장하지 않은 Article을 생성하면 ValueError 발생
    
    
    >>> r3 = Reporter(first_name='John', last_name='Smith', email='john@example.com')
    >>> Article.objects.create(headline="This is a test", pub_date=date(2005, 7, 27), reporter=r3)
    Traceback (most recent call last):
    ...
    ValueError: save() prohibited to prevent data loss due to unsaved related object 'reporter'.
- Article 객체는 관련된 Reporter 객체로 접근함
    
    
    >>> r = a.reporter
- Reporter 객체를 통해 Article을 생성
    
    
    >>> new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
    >>> new_article
    <Article: John's second story>
    >>> new_article.reporter
    <Reporter: John Smith>
    >>> new_article.reporter.id
    1
- 새 article 만들기


    >>> new_article2 = Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17), reporter=r)
    >>> new_article2.reporter
    <Reporter: John Smith>
    >>> new_article2.reporter.id
    1
    >>> r.article_set.all()
    <QuerySet [<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]>
- 잘못된 유형의 객체를 추가하면 TypeError 발생
    
    
    >>> r.article_set.add(r2)
    Traceback (most recent call last):
    ...
    TypeError: 'Article' instance expected, got <Reporter: Paul Jones>
    >>> r.article_set.all()
    <QuerySet [<Article: John's second story>, <Article: This is a test>]>
    >>> r2.article_set.all()
    <QuerySet [<Article: Paul's story>]>
    >>> r.article_set.count()
    2
    >>> r.article_set.count()
    1
- 관련 매니저는 필드 조회 지원. 관계 구분을 위해 __(이중밑줄)사용
    
    
    >>> r.article_set.filter(headline__startswith='This')
    <QuerySet [<Article: This is a test>]>
    >>> Article.objects.filter(reporter__first_name='John')
    <QuerySet [<Article: John's second story>, <Article: This is a test>]>
    
    