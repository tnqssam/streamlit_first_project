import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSV 파일 불러오기
data = pd.read_csv('age2411.csv')

# Streamlit 앱 시작
st.title("우리 지역의 인구 구조를 알아봐요!")
st.write("아래에서 원하는 지역을 선택하면 해당 지역의 인구 구조를 확인할 수 있어요.")

# 데이터 전처리: 연령대만 추출
data = data.dropna()  # 결측치 제거
age_columns = [col for col in data.columns if '0세' in col or '세' in col or '100세 이상' in col]

# 지역 선택하기
regions = data['행정구역'].unique()
selected_region = st.selectbox("지역을 선택하세요:", regions)

# 선택된 지역 데이터 필터링
region_data = data[data['행정구역'] == selected_region][age_columns].transpose()
region_data.columns = ['Population']
region_data = region_data.reset_index()
region_data.rename(columns={'index': 'Age Group'}, inplace=True)

# 인구 구조 그래프 그리기
st.write(f"### {selected_region}의 인구 구조")
fig, ax = plt.subplots()
ax.bar(region_data['Age Group'], region_data['Population'])
plt.xticks(rotation=90)  # x축 라벨 회전
plt.xlabel("연령대")
plt.ylabel("인구 수")
plt.title(f"{selected_region}의 연령별 인구 구조")

st.pyplot(fig)

# 추가 설명
st.write("그래프를 통해 어떤 나이대의 인구가 많은지 확인할 수 있어요! 친구들과 다른 지역과 비교해보세요.")
