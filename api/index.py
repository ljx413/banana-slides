from streamlit.web.bootstrap import run
import os

if __name__ == "__main__":
    run(
        main_script_path="app.py",
        command_line="",
        args=[],
        flag_options={"server.port": 3000, "server.headless": True},
    )
