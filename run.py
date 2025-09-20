import subprocess
import sys

# Name of your Streamlit script
script_name = "omr_streamlit_app.py"

# Run Streamlit
subprocess.run([sys.executable, "-m", "streamlit", "run", script_name])

