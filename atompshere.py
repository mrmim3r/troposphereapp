import streamlit as st 




col1, col3,col2 = st.columns([3,1,3])
with col1 : 
    st.header("troposphere charatrestique")
    st.slider("height from sea", max_value=11000, min_value=0, key="height")
    
with col2 :
    st.header("Result ")
    h=st.session_state.height

    dh = 0
    dt = 15.04
    dp = 101.40093090454886
    hkm = h/1000
    t  = dt-hkm*6.49
    p = 101.29*(((t + 273.1)/288.08)**5.256)
    

    st.metric(label = "Height", value=str(h)+" m ", delta=str(h-dh)+" m")

    st.metric(label = "Temparteur", value=str(t)+" c ", delta=str(t-dt)+" c")
    
    st.metric(label = "Presseur", value=str(p)+" Kp ", delta=str(p-dp)+" KP")
    
with col1 :
    st.slider("temprateur from sea", max_value=15.04, min_value=-56.35, key="temp", value=t,  disabled=True)
    st.slider("presseur from sea",disabled=True, max_value=101.40093090454886, min_value=22.707364717350817, key="pres", value=p)






