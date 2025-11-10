#자신이 만든 레포지토리(저장소)에 streamlit_app.py 만들고 다음 내용 복붙해서 집어넣기

import streamlit as st
import pandas as pd

# --- 1. 페이지 기본 설정 ---
st.set_page_config(
    page_title="Streamlit 현수의 첫번째 페이지",
    page_icon="🔮",
    layout="wide"
)

# --- 2. 페이지 타이틀 ---
st.title("Streamlit 마법 교실 🔮")
st.subheader("HTML/CSS를 활용해 멋진 효과를 만들어 봐요!")
st.markdown("---") # 구분선

# --- 3. 모든 커스텀 CSS ---
# st.markdown 내부에 <style> 태그를 사용하여 CSS를 전역으로 주입합니다.
# 학생들에게 각 CSS 클래스가 어떤 효과를 주는지 설명하기 좋습니다.
st.markdown("""
<style>
/* 섹션 1: 움직이는 그라데이션 텍스트
  - background: 4가지 색상의 선형 그라데이션을 만듭니다.
  - background-size: 배경을 4배 키워서 움직일 공간을 만듭니다.
  - background-clip: text; : 배경을 텍스트 모양으로 잘라냅니다.
  - text-fill-color: transparent; : 텍스트 색을 투명하게 만들어 배경 그라데이션이 보이게 합니다.
  - animation: 'gradient' 애니메이션을 5초 동안 무한 반복합니다.
*/
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.gradient-text {
    font-size: 40px;
    font-weight: bold;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient 5s ease infinite;
    text-align: center;
    padding: 10px;
}

/* 섹션 2: 인터랙티브 카드 (마우스 호버)
  - transition: 0.3초 동안 부드럽게 변하도록 설정합니다.
  - box-shadow: 카드에 입체감을 주는 그림자입니다.
  - :hover (가상 클래스): 마우스를 올렸을 때 적용될 스타일입니다.
  - transform: scale(1.05); : 마우스를 올리면 1.05배 커집니다.
*/
.interactive-card {
    background-color: #f0f8ff; /* AliceBlue */
    border: 1px solid #d6eaff;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.interactive-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    cursor: pointer;
}

/* 섹션 3: Flexbox를 이용한 카드 레이아웃
  - display: flex; : 내부 아이템들을 가로로 정렬합니다.
  - justify-content: space-around; : 아이템들 사이에 균등한 간격을 줍니다.
  - flex-wrap: wrap; : 화면이 좁아지면 아이템이 다음 줄로 넘어갑니다. (반응형)
*/
.flex-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    padding: 10px;
    background-color: #fafafa;
    border-radius: 10px;
}

.flex-card {
    width: 30%;
    min-width: 250px; /* 최소 너비 */
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    padding: 15px;
    margin: 10px;
    border-top: 5px solid #23a6d5; /* 상단에 포인트 컬러 */
}

/* 섹션 4: 애니메이션이 있는 버튼
  - ::before (가상 요소): 버튼 뒤에 빛나는 효과를 위한 추가 레이어입니다.
  - filter: blur(15px); : 빛이 번지는 효과를 줍니다.
  - animation: 'glowing' 애니메이션을 20초 동안 선형으로 무한 반복합니다.
*/
@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}

.glowing-button {
    position: relative;
    padding: 15px 30px;
    font-size: 18px;
    font-weight: bold;
    color: white;
    background-color: #313131;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    overflow: hidden; /* 가상 요소가 버튼 밖으로 나가지 않도록 */
}

.glowing-button::before {
    content: '';
    position: absolute;
    top: -5px; left: -5px; right: -5px; bottom: -5px;
    z-index: -1;
    background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
    background-size: 400%;
    border-radius: 15px;
    filter: blur(15px);
    animation: glowing 20s linear infinite;
}

</style>
""", unsafe_allow_html=True)

# --- 4. 섹션 1: 움직이는 그라데이션 텍스트 ---
st.header("1. HTML/CSS: ✨ 움직이는 그라데이션 텍스트")
st.markdown('<div class="gradient-text">이 텍스트는 CSS 애니메이션으로 움직여요!</div>', unsafe_allow_html=True)
st.markdown("---")

# --- 5. 섹션 2: 인터랙티브 카드 (마우스 호버) ---
st.header("2. HTML/CSS: 🖱️ 인터랙티브 카드 (마우스 올려보기)")
st.markdown("""
<div class="interactive-card">
    <h3>마우스를 올려보세요!</h3>
    <p><code>:hover</code> 가상 클래스와 <code>transform: scale()</code>을 사용하면<br>
    이렇게 재미있는 효과를 만들 수 있습니다.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# --- 6. 섹션 3: Flexbox를 이용한 카드 레이아웃 ---
st.header("3. HTML/CSS: 🎨 Flexbox로 카드 정렬하기")
st.markdown("""
<div class="flex-container">
    <div class="flex-card">
        <h4>카드 1: HTML</h4>
        <p>웹 페이지의 뼈대를 만듭니다. (<code>div</code>, <code>p</code>, <code>h4</code>...)</p>
    </div>
    <div class="flex-card">
        <h4>카드 2: CSS</h4>
        <p>웹 페이지를 예쁘게 꾸며줍니다. (<code>color</code>, <code>background</code>...)</p>
    </div>
    <div class="flex-card">
        <h4>카드 3: Streamlit</h4>
        <p>파이썬만으로 이 모든 것을 쉽게 만들 수 있게 해줍니다.</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# --- 7. 섹션 4: 애니메이션이 있는 버튼 ---
st.header("4. HTML/CSS: 🚀 빛나는 애니메이션 버튼")
st.markdown('<div style="text-align: center; padding: 20px;"><button class="glowing-button">✨ 마법 버튼 ✨</button></div>', unsafe_allow_html=True)
st.markdown("---")

# --- 8. 섹션 5: Streamlit 기본 기능 (데이터프레임) ---
st.header("5. Streamlit 기본 기능: 📊 데이터프레임")
st.write("Streamlit은 Pandas 데이터프레임을 표로 멋지게 보여줍니다.")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 29],
    "Country": ["Korea", "USA", "UK"]
})
st.dataframe(df)
st.markdown("---")

# --- 9. 섹션 6: Streamlit 기본 기능 (이미지 및 비디오) ---
st.header("6. Streamlit 기본 기능: 🖼️ 이미지와 🎬 비디오")

# 컬럼을 사용해 좌우로 배치
col1, col2 = st.columns(2)

with col1:
    st.write("이미지 표시 예제")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit 로고")

with col2:
    st.write("유튜브 동영상 예제")
    st.video("https://www.youtube.com/watch?v=qrqHlgqNTHo")

# --- 10. 마무리 ---
st.markdown("---")
st.subheader("모두 멋진 웹 앱을 만들어 보세요! 🚀")
st.balloons() # 학생들을 위한 작은 이벤트!
