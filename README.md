# COSMAX AI CLASS 2022

(last-update:  Feb-15, 2022 chester)

COSMAX 에서 진행하는 AI CLASS 2022 관련한 자료들을 모아놓는 repository 입니다.

# Feb-15. 2022

두달전에 수업은 시작했습니다만, 리파지토리 관리는 깔끔하게 못했네요.. 이번달에는 RNN 의 기본구조, 기본구현에 대해서 집중적으로 배우고,
LSTM 을 이용한 seq2seq 구현, 그리고 여기에 attention 을 적용해보는 것을 통해서 attention 의 개념에 대해서 이해를 하는 것으로 하겠습니다. 
그 이후에 transformer 공부를 시작할지 아니면 이제 transformer 는 blackbox 로 덮어두고 fine-tuning 만 집중적으로 다루어볼지에 대해서 한번 생각해봅시다.


# Feb-14. 2021

Pytorch 에서 [Tensor 를 다루는 법](https://github.com/chesterroh/cosmax_ai_class/blob/master/04_pytorch_tutorial_basic_supplement_practice.ipynb)에 대해서 조금 자세하게 연습노트를 하나 더 만들어 두었습니다. 이제 Fully-Connected 부터 Convolution, RNN 을 넘어서서 Transformer 까지 한번 달려보도록 합시다 :)

# Feb-13. 2021

* pytorch tutorial 부터 다시 시작합니다. AI 의 기초개념들만 탑재를 했으니, 이제 조금씩 예제를 한번 풀어가 보도록 할까요. 

# Sep-10. 2020

* Losgistic Regression 의 numpy 구현에 대한 background theory 를 [여기](https://github.com/chesterroh/cosmax_ai_class/blob/master/03_logistic_regression_background_theory.pdf)에 업데이트 해두었습니다. 

# Sep-2.2020

pytorch 학습을 시작하기 위해서 두개의 학습교재 note 를 upload 했습니다. 오늘 업로딩한 교재는 9월 9일 수업에서 다루게 될 내용입니다. 

* __[PYTORCH tensor manipulation tutorial (04_pytorch_tutorial_basic_tensor)](https://github.com/chesterroh/cosmax_ai_class/blob/master/04_pytorch_tutorial_basic_tensor.ipynb)__

* __[PYTORCH MNIST fully connected network (05_pytorch_mnist_fully_connected)](https://github.com/chesterroh/cosmax_ai_class/blob/master/05_pytorch_mnist_fully_connected.ipynb)__


# Sep-1.2020

9월 1일입니다. python 수업으로 가볍게 시작한 수업이 2달이 넘는 시간이 흘렀습니다. 9월 2일 수업시간에는 00_python_numpy_matplotlib 노트에서 소개하고 있는 python, numpy, matplotlib 에 대해서 Google colab 위에서 실습을 할 예정이구요. linear regression, logistic regression 관련하여 sample code 를 실행해보는 시간을 갖도록 하겠습니다. logistic regression code 를 실행하기 전에는 머리아픈 이론복습을 한번 더 하면서 data 가 어떻게 matrix 로 표현되고, 연산이 되는지 dimension 들을 꼼꼼히 살펴보면서 개념탑재를 해보도록 하겠습니다. 

* __[오늘 올라간 예제는 mnist dataset 중에서 단 두개의 숫자만 추출해서 logistic regression 을 numpy 로 구현해보는 것입니다. (03_numpy_logistic_regression)](https://github.com/chesterroh/cosmax_ai_class/blob/master/03_numpy_logistic_regression.ipynb)__


# Aug-28.2020

* __[Numpy 를 이용해서 mnist dataset 을 다운로드하고 다루는 예제를 하나 추가했구요.(01_mnist_dataset_numpy)](https://github.com/chesterroh/cosmax_ai_class/blob/master/01_mnist_dataset_numpy.ipynb)__
* __[지난 수업에서 이론강연을 하고 간단하게 구현해보았던 Linear Regression 에 대해서 좀더 자세한 학습노트를 만들었습니다.(02_numpy_linear_regression)](https://github.com/chesterroh/cosmax_ai_class/blob/master/02_numpy_linear_regression.ipynb)__

다음주 9월 2일 수업에서 여러분들이 직접 따라서 코딩을 해보셔야 할 노트입니다. (제가 만든 노트 실행만 시켜보는게 아니라, 여러분의 notebook 에서 직접 손으로 타이핑하게 할 예정이니 미리 예습하실 분들은 예습하시기 바랍니다. ^^^) 

# Aug-27.2020

Aug-26 에 내어드린 숙제를 검사할 목적으로 제가 youtube 강연을 한번 훑어보았습니다만, 숙제의 양이 너무 적다는 느낌(?)이 들어서요. __[숙제를 하나 더 만들어보았습니다. 01_python_numpy_matplotlib_tutorial](https://github.com/chesterroh/cosmax_ai_class/blob/master/00_python_numpy_matplotlib_tutorial.ipynb)__ 해당 notebook file 을 google colab 으로 불러서 실행하실 수 있습니다. github 에 있는 Jupyter Notebook 을 불러오는 방법은 아래 소개드린 colab 설명 youtube 동영상에 소개되어 있습니다. 간단하게 link 로 알려드릴 수 있지만, 여러분의 학습을 위해서 설명드리지 않도록 하겠습니다.  다음주 수요일 수업시간 전에 얼마나 공부하셨는지 간략하게 나마 퀴즈세션을 갖도록 해볼께요. 재택근무기간동안 힘내시구요! 계속 앞으로 전진하십시다. numpy 가 좀 재밌어지실거에요.. numpy 연습을 위해서 주말에 간단한 연습용 notebook 을 하나 더 배포해드리도록 하겠습니다.

# Aug-26.2020

코로나로 인하여 오늘 강연이 연기되었습니다. pytorch 를 이용해서 기초부터 찬찬히 시작해서 테스트감성분석, 복잡한 이미지생성 등등 까지 앞으로 먼길을 걸어가게 될텐데요. 일단 pytorch 를 이용해서 본격적인 Deep Learning 세계에 뛰어들기 전에 간단하게 복습 겸 기본개념을 좀 짚고 넘어가도록 하겠습니다.  Youtube 에서 괜찮은 강연을 찾기 위해서 이것저것 둘러봤는데요. "딥러닝호형" 이라는 분이 만드신 강연이 일단 복습 및 기본개념 학습자료로 좋은 것 같아서 선정을 했습니다.

https://www.youtube.com/watch?v=N6iC_rBga3I&list=PLHOsBEAyYj3xf4i20sCA5o8MgVW5sIiHD&index=1

자, 이번주 숙제나갑니다!

여기 링크에 들어가시면 "머신러닝/딥러닝을 위해 반드시 알아야 할 파이썬" 강연이 1강에서 7강까지가 있습니다. 해당 강연을 수강하시면서 강연에서 가르쳐주는 코드를 이번주에 설정한 Google Colab 위에서 직접 한번씩 따라서 코딩을 해보시면 되겠습니다. Google Colab note 메뉴에 보시면 " ipynb 형식으로 다운로드하기" 라는 메뉴가 있습니다. 학습하신 자료를 2020년 9월 2일 수요일까지 본 강사의 이메일(예전에 html 숙제 보낸 이메일주소 기억하시죠?)로 보내주시는 것이 이번주의 숙제가 되겠습니다. 

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



