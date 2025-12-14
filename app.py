import streamlit as st, requests, time

st.set_page_config(page_title="Banana Slides", layout="centered")
st.title("🍌 Banana Slides - 一键 PPT 生成器")

uploaded = st.file_uploader("上传 PDF / DOCX / TXT", type=["pdf", "docx", "txt"])
if uploaded and st.button("生成 PPT"):
    with st.spinner("正在生成，请稍候..."):
        # 调后端
        res = requests.post(
            "http://localhost:8000/generate",
            files={"upload": ("file", uploaded.getvalue(), uploaded.type)},
        )
    if res.status_code == 200:
        st.download_button("📥 下载 PPT", res.content, "banana_slides.pptx")
    else:
        st.error("生成失败，请检查日志")
