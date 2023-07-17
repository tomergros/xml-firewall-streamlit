import streamlit as st
import requests

def fetch_kaggle_notebook(notebook_id):
    url = f"https://www.kaggleusercontent.com/api/notebooks/{notebook_id}/export?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def main():
    st.title("XML- Firewall: Cyber Attacks Classification")

    # Hardcoded Kaggle notebook ID
    notebook_id = '136941707'

    # Fetch the Kaggle notebook content
    notebook_data = fetch_kaggle_notebook(notebook_id)

    if notebook_data:
        # Display the notebook code
        code_blocks = notebook_data["cells"]
        for code_block in code_blocks:
            if code_block["cell_type"] == "code":
                code_lines = code_block["source"]
                code = "\n".join(code_lines)
                st.code(code, language="python")
    else:
        st.error("Notebook not found. Please check the notebook ID.")

if __name__ == '__main__':
    main()
