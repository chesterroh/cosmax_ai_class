# COSMAX AI CLASS 2020

COSMAX 에서 진행하는 AI CLASS 2020 관련한 자료들을 모아놓는 repository 입니다.  

# Aug-26.2020

코로나로 인하여 오늘 강연이 연기되었습니다. pytorch 를 이용해서 기초부터 찬찬히 시작해서 테스트감성분석, 복잡한 이미지생성 등등 까지 앞으로 먼길을 걸어가게 될텐데요. 일단 pytorch 를 이용해서 본격적인 Deep Learning 세계에 뛰어들기 전에 간단하게 복습 겸 기본개념을 좀 짚고 넘어가도록 하겠습니다.  Youtube 에서 괜찮은 강연을 찾기 위해서 이것저것 둘러봤는데요. "딥러닝호형" 이라는 분이 만드신 강연이 일단 복습 및 기본개념 학습자료로 좋은 것 같아서 선정을 했습니다.

https://www.youtube.com/watch?v=N6iC_rBga3I&list=PLHOsBEAyYj3xf4i20sCA5o8MgVW5sIiHD&index=1

자, 이번주 숙제나갑니다!

여기 링크에 들어가시면 "머신러닝/딥러닝을 위해 반드시 알아야 할 파이썬" 강연이 1강에서 7강까지가 있습니다. 해당 강연을 수강하시면서 강연에서 가르쳐주는 코드를 이번주에 설정한 Google Colab 위에서 직접 한번씩 따라서 코딩을 해보시면 되겠습니다. Google Colab note 메뉴에 보시면 " ipynb 형식으로 다운로드하기" 라는 메뉴가 있습니다. 학습하신 자료를 2020년 9월 2일 수요일까지 본 강사의 이메일로 보내주시는 것이 이번주의 숙제가 되겠습니다. 

기초로 숨을 고르고 이제 pytorch 로 본격적으로 달려나가 보겠습니다. 기초와 실습부분을 제가 여러분들의 코드를 직접 살펴보면서 필요하다면 난이도를 조절해서 계속해서 반복학습을 시켜드릴테니까요, 걱정마시고 하나도 모르겠더라도 최대한 반복하면서 따라와 주시면 감사하겠습니다.

* Google Colab 역시 youtube 에 "구글 콜랩 기초" 라고 검색해보시면 많은 자료들이 있으니 참고 바라구요. 저는 https://www.youtube.com/watch?v=v19SzGMOd2c 이 자료를 참고하였습니다. 

# Aug-19.2020

지난 2주에 걸쳐서 Deep Learning 이란 무엇인가에 대해서 간략한 이론을 배웠습니다. Data 가 가지고 있는 어떠한 규칙(Rule)을 학습하기 위해서 수학적 Model 을 만들고, 그 Model 에 적절한 목적함수(Objective Function)을 설정한 이후에, Data 를 갈아 넣으면서 최대한 Data 를 잘 표현(represent)할 수 있는 (Model 의 Parameter 값)을 update 해나가는 과정을 학습(train)한다라고도 말씀을 드렸지요. 제가 말하고도 무슨 말인가 싶을 정도네요 ㅎㅎㅎ 

개념도 쉽게 와닿지가 않는데 Matrix(행렬)의 연산, 그리고 Gradient Back Propagation 과정에서 사용된 미적분은 도대체 왜 사용하는 것인지 등에 대한 많은 궁금점이 있으시라고 봅니다. 

* 행렬에 대해서 궁금하신 분들은 youtube 에서 '딥러닝 행렬' 이렇게 검색해보시면 굉장히 많은 동영상을 접하실 수 있습니다. 그중에 몇개를 보시면 될 것 같아요. 

제가 좋아하는 이상엽 선생님의 행렬수업입니다.
https://www.youtube.com/watch?v=83UnOz6HiOY

* 딥러닝에서 필요한 간단한 미적분관련한 지식은 youtube 에서 "딥러닝 미적분" 이렇게 검색해보시면 필요한 정보를 얻으실 수 있습니다.

저희가 지난 2주동안 매우 간단한 Linear Regression, 그리고 Logistic Regression 에 대해서 배웠는데요. 해당 강연은 그 유명한 Andrew Ng 교수님의 deeplearning.ai specialization course 1 수업에 최대한 가깝게 진행을 했습니다.

해당수업은 http://deeplearning.ai 에서 제공하는 유료수업이긴 합니다만, 친절한 Andrew Ng 교수님께서 초반부분은 모두 youtube 에 공개를 해두셨습니다. 한국어자막 설정을 하시고 이해될때까지 계속해서 보고 또 보겠다는 마음가짐으로 임하시다보면 이해하는 날이 올것이라고 믿습니다.

https://www.youtube.com/watch?v=CS4cs9xVecg&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0


