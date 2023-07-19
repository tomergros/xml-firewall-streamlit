import streamlit as st
import codecs

def main():
    st.title("Kaggle Notebook Viewer")

    # Path to the downloaded HTML file
    html_file_path = r"xml-firewall-cyber-attacks-classification.html"

    try:
        with codecs.open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("HTML file not found. Please provide the correct file path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
