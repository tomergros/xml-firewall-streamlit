import streamlit as st
import nbformat
from nbconvert import MarkdownExporter
import os
import kaggle

def convert_ipynb_to_md(notebook_path):
    nb = nbformat.read(notebook_path, as_version=4)
    exporter = MarkdownExporter()
    md, _ = exporter.from_notebook_node(nb)
    return md

def download_kaggle_notebook(username, notebook_id):
    os.makedirs('kaggle_notebooks', exist_ok=True)
    kaggle.api.dataset_download_files(f'{username}/kaggle-notebook-{notebook_id}', path='kaggle_notebooks', unzip=True)
    files = os.listdir('kaggle_notebooks')
    for file in files:
        if file.endswith('.ipynb'):
            return f'kaggle_notebooks/{file}'
    return None

def main():
    st.title("Kaggle Notebook Viewer")

    # Hardcoded Kaggle username and notebook ID
    username = 'tomergrossy'
    notebook_id = 'xml-firewall-cyber-attacks-classification'
    # Download the Kaggle notebook
    notebook_path = download_kaggle_notebook(username, notebook_id)

    if notebook_path:
        # Convert the notebook to Markdown
        md_content = convert_ipynb_to_md(notebook_path)

        # Render the Markdown content
        st.markdown(md_content)
    else:
        st.error("Notebook not found. Please check your Kaggle username and notebook ID.")

if __name__ == '__main__':
    main()
