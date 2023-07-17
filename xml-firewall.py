import streamlit as st
import urllib.request
import json

def fetch_kaggle_notebook_content(kaggle_notebook_url):
    try:
        with urllib.request.urlopen(kaggle_notebook_url) as response:
            notebook_content = json.load(response)
        return notebook_content
    except Exception as e:
        raise ValueError("Failed to fetch Kaggle notebook content") from e

def display_kaggle_notebook_content(cells):
    for cell in cells:
        cell_type = cell["cell_type"]

        if cell_type == "code":
            # Display code cells
            code = cell["source"]
            st.code("\n".join(code))

        elif cell_type == "markdown":
            # Display markdown cells
            markdown = cell["source"]
            st.markdown("\n".join(markdown))

        elif cell_type == "output":
            # Display output cells
            output = cell["output_type"]
            st.write(output)

        # Add additional logic for other cell types if needed

def main():
    st.title("Kaggle Notebook Viewer")

    # Hard coded Kaggle notebook URL
    kaggle_notebook_url = "https://www.kaggle.com/code/tomergrossy/xml-firewall-cyber-attacks-classification/"

    try:
        notebook_content = fetch_kaggle_notebook_content(kaggle_notebook_url)
        cells = notebook_content["cells"]
        display_kaggle_notebook_content(cells)
    except ValueError as ve:
        st.error(str(ve))
    except Exception as e:
        st.error("An unexpected error occurred.")

if __name__ == "__main__":
    main()
