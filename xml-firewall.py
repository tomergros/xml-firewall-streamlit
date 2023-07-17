import streamlit as st
import requests

def fetch_kaggle_notebook(username, notebook_slug):
    url = f"https://www.kaggle.com/{username}/{notebook_slug}/download"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.decode("utf-8")
    return None

def main():
    st.title("Kaggle Notebook Viewer")

    # Hardcoded Kaggle username and notebook slug
    username = 'tomergrossy'
    notebook_slug = 'xml-firewall-cyber-attacks-classification'

    # Fetch the Kaggle notebook content
    notebook_content = fetch_kaggle_notebook(username, notebook_slug)

    if notebook_content:
        # Display the notebook content
        st.code(notebook_content, language="python")
    else:
        st.error("Notebook not found. Please check the Kaggle username and notebook slug.")

if __name__ == '__main__':
    main()
