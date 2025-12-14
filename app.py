import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Banana Slides", layout="centered")
st.title("🍌 Banana Slides - 一键 PPT 生成器")
st.markdown("---")

uploaded = st.file_uploader("上传 PDF / DOCX / TXT", type=["pdf", "docx", "txt"])
if uploaded and st.button("生成 PPT"):
    with st.spinner("正在生成，请稍候..."):
        # 调用后端可执行文件（相对路径）
        cmd = ["./backend/banana-slides", "-i", uploaded.name, "-o", "output.pptx"]
        subprocess.run(cmd, check=True)
    st.success("完成！")
    with open("output.pptx", "rb") as f:
        st.download_button("下载 PPT", f, file_name="banana_slides.pptx")
