import streamlit as st
import kaggle

def download_kaggle_notebook(username, notebook_slug):
    kaggle.api.dataset_download_files(f'{username}/{notebook_slug}', path='.', unzip=True)
    files = os.listdir('.')
    for file in files:
        if file.endswith('.ipynb'):
            return file
    return None

def main():
    st.title("Kaggle Notebook Viewer")

    # Hardcoded Kaggle username and notebook slug
    username = 'tomergrossy'
    notebook_slug = 'xml-firewall-cyber-attacks-classification'

    # Download the Kaggle notebook
    notebook_file = download_kaggle_notebook(username, notebook_slug)

    if notebook_file:
        # Read the notebook file
        with open(notebook_file, 'r', encoding='utf-8') as file:
            notebook_content = file.read()

        # Display the notebook content
        st.code(notebook_content, language="python")
    else:
        st.error("Notebook not found. Please check the Kaggle username and notebook slug.")

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()
