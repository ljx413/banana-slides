import streamlit as st, requests
st.title("Banana Slides")
f = st.file_uploader("上传文档")
if f and st.button("生成"):
    with st.spinner("生成中..."):
        res = requests.post("http://localhost:8000/generate",
                            files={"upload": f})
    st.download_button("下载 PPT", res.content, "slides.pptx")
