import streamlit as st

# MBTI 정보 딕셔너리
mbti_data = {
    "ISTJ": {
        "job": "📊 조직적이고 책임감이 강해 관리직이나 회계사, 엔지니어가 잘 맞아요.",
        "partner": "❤️ ISTJ는 신뢰를 중요시하므로 INFJ나 ESFJ와 좋은 조화를 이룰 수 있어요."
    },
    "ISFJ": {
        "job": "🧑‍⚕️ 헌신적이고 배려심이 깊어 간호사, 교사, 사회복지사로 빛을 발해요.",
        "partner": "💞 ISFJ는 믿음직한 ESTJ나 따뜻한 ENFP와 잘 어울려요."
    },
    "INFJ": {
        "job": "📖 통찰력과 비전을 갖춘 INFJ는 심리학자, 작가, 상담사가 어울려요.",
        "partner": "🌟 INTJ나 ENTP와 함께하면 창의력이 불꽃 튀길 거예요!"
    },
    "INTJ": {
        "job": "🧠 분석적이고 전략적인 INTJ는 연구원, 전략기획자, 개발자 역할이 적합해요.",
        "partner": "✨ ENFP와 ENTP와의 관계는 서로를 자극하며 성장하게 해줘요."
    },
    "ISTP": {
        "job": "🔧 실용적이고 논리적인 ISTP는 엔지니어, 파일럿, 수리 기술자로 잘 맞아요.",
        "partner": "🤝 ISFP나 ESTP와 편안하고 자유로운 관계를 만들 수 있어요."
    },
    "ISFP": {
        "job": "🎨 감성적이고 예술적인 ISFP는 디자이너, 음악가, 플로리스트에 잘 어울려요.",
        "partner": "💓 ESFP나 ISTP와 감성적으로 공감하는 관계를 만들어요."
    },
    "INFP": {
        "job": "✍️ 창의적이고 이상적인 INFP는 작가, 예술가, 심리상담사가 좋아요.",
        "partner": "🌼 ENFJ나 INTJ와 함께라면 꿈을 현실로 만들 수 있어요."
    },
    "INTP": {
        "job": "🧩 분석적이고 창의적인 INTP는 연구원, 개발자, 발명가로 활약해요.",
        "partner": "🔍 ENTP나 INFJ와 깊은 대화를 나누며 시너지를 낼 수 있어요."
    },
    "ESTP": {
        "job": "⚡ 도전적이고 활동적인 ESTP는 영업직, 스포츠 선수, 기업가가 잘 어울려요.",
        "partner": "🎉 ISTP나 ESFP와 함께하면 즐거운 모험이 계속될 거예요!"
    },
    "ESFP": {
        "job": "🎭 사교적이고 에너지가 넘치는 ESFP는 배우, 이벤트 기획자, 홍보직에 어울려요.",
        "partner": "💃 ISFP나 ESTP와 함께 즐거운 시간을 보낼 수 있어요."
    },
    "ENFP": {
        "job": "🌈 창의적이고 열정적인 ENFP는 마케터, 카운슬러, 이벤트 플래너가 어울려요.",
        "partner": "🔥 INTJ나 INFJ와 함께하면 서로에게 영감을 줄 수 있어요."
    },
    "ENTP": {
        "job": "💡 아이디어 뱅크인 ENTP는 창업가, 컨설턴트, 변호사로 두각을 나타내요.",
        "partner": "🌟 INFJ나 INTJ와의 만남은 큰 시너지를 만들어낼 거예요."
    },
    "ESTJ": {
        "job": "🛠️ 리더십과 실용성을 가진 ESTJ는 관리자, 공무원, 기업 임원에 어울려요.",
        "partner": "🤝 ISFJ나 ESFJ와 신뢰를 바탕으로 든든한 관계를 만들어요."
    },
    "ESFJ": {
        "job": "🌟 따뜻하고 친절한 ESFJ는 교사, 간호사, 서비스직에서 빛나요.",
        "partner": "💖 ISTJ나 ESTJ와 함께할 때 안정적이고 행복해져요."
    },
    "ENFJ": {
        "job": "🤝 사람을 이끄는 ENFJ는 리더, 상담사, 코치로 잘 어울려요.",
        "partner": "💞 INFP나 INTJ와 깊은 유대감을 형성할 수 있어요."
    },
    "ENTJ": {
        "job": "👑 타고난 리더 ENTJ는 경영자, 전략 컨설턴트, 기업 임원에 어울려요.",
        "partner": "⚡ ENFP나 INTP와 함께라면 목표를 향해 멋지게 나아갈 수 있어요."
    }
}

# 스트림릿 앱
st.title("✨ 나의 MBTI와 찰떡 직업/궁합 찾기! ✨")

# 드롭다운 메뉴로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요 😊", list(mbti_data.keys()))

# 결과 보여주기
if selected_mbti:
    st.subheader("🔍 결과 확인!")
    st.write(f"**직업 추천:** {mbti_data[selected_mbti]['job']}")
    st.write(f"**잘 맞는 사람:** {mbti_data[selected_mbti]['partner']}")
    st
