import streamlit as st
import os
from datetime import datetime
from PIL import Image

st.title('메모장')
# 메모를 저장할 디렉토리 생성
if not os.path.exists('memos'):
    os.makedirs('memos')

# 새 메모 추가
new_memo = st.text_area('이곳에 입력하세요', height=150)
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])
save_button = st.button('저장')

if save_button:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    with open(f'memos/memo_{timestamp}.txt', 'w', encoding="UTF-8") as f:
        f.write(new_memo)
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image.save(f'memos/image_{timestamp}.png')
    st.success('메모가 추가되었습니다.')

# 저장된 메모 보기
st.subheader('저장된 메모')

memo_files = sorted(os.listdir('memos'), reverse=False)

for file in memo_files:
    if file.endswith('.txt'):
        with open(f'memos/{file}', 'r', encoding="UTF-8") as f:
            memo = f.read()
        st.write(memo)
        delete_button = st.button('삭제', key=file)
        if delete_button:
            os.remove(f'memos/{file}')
            st.warning(f'메모가 삭제되었습니다.')
            st.rerun()
            st.download_button('내 컴퓨터에 저장', new_memo, key = new_memo)
    elif file.endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(f'memos/{file}')
        st.image(image, caption=file)
        delete_button = st.button('삭제', key=file)
        if delete_button:
            os.remove(f'memos/{file}')
            st.warning('이미지가 삭제되었습니다.')
            st.rerun()