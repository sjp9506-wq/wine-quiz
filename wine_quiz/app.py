import streamlit as st
import random

wines = [
    {"name": "진판델", "image": "images/001.jpg"},
    {"name": "울팩", "image": "images/002.jpg"},
    {"name": "브리송", "image": "images/003.jpg"},
    {"name": "피오레 모스카토 다스티", "image": "images/004.jpg"},
    {"name": "스트로베리 스파클링", "image": "images/005.jpg"},
    {"name": "스파클링 티", "image": "images/006.jpg"},
    {"name": "오스틴 까베르네 소비뇽", "image": "images/007.jpg"},
    {"name": "비! 레드와인", "image": "images/008.jpg"}

]
# 문제 생성 함수
def make_question():
    q = random.choice(wines)
    correct = q["name"]

    options = [w["name"] for w in wines]
    options.remove(correct)

    wrong = random.sample(options, 3)
    choices = wrong + [correct]
    random.shuffle(choices)

    return q, correct, choices

# 최초 문제 생성
if "question" not in st.session_state:
    q, correct, choices = make_question()
    st.session_state.question = q
    st.session_state.correct = correct
    st.session_state.choices = choices
    st.session_state.checked = False
    st.session_state.answer = None

q = st.session_state.question
correct = st.session_state.correct
choices = st.session_state.choices

st.image(q["image"])

# 선택
st.session_state.answer = st.radio(
    "이 와인은?",
    choices,
    key="radio"
)

# 정답 확인
if st.button("정답 확인"):
    st.session_state.checked = True

if st.session_state.checked:
    if st.session_state.answer == correct:
        st.success("정답!")
    else:
        st.error(f"오답! 정답은 {correct}")

# 👉 핵심: 다음 문제 버튼
if st.session_state.checked:
    if st.button("다음 문제"):
        q, correct, choices = make_question()

        st.session_state.question = q
        st.session_state.correct = correct
        st.session_state.choices = choices

        # 상태 초기화
        st.session_state.checked = False
        st.session_state.answer = None

        st.rerun()