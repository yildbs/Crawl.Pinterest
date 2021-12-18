# Crawl.Pinterest

# Pinterest의 이미지를 크롤링하고 저장합니다

- 2021.12.18에는 동작합니다. Pinterest 웹사이트의 정책에 따라 동작하지 않을 수 있습니다. 

# 사용법
- conf.py를 수정합니다
 > search_word : 검색할 단어
 > target_num_images : 저장할 이미지의 개수 (보장은 못함)
 
- login_info.py.default를 복사하고 login_info.py로 이름을 바꿉니다
 > Pinterest에 접속할 아이디와 비밀번호를 입력
 
# Run command
python3 main.py
