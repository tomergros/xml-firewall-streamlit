import streamlit as st
from IPython.display import IFrame

def main():
    st.title("Kaggle Notebook Viewer")

    # Hardcoded Kaggle notebook URL
    notebook_url = 'https://www.kaggle.com/code/tomergrossy/xml-firewall-cyber-attacks-classification'

    # Display the Kaggle notebook
    st.markdown(f"XML- Firewall: Cyber Attacks Classification")
    st.markdown(
        f'<iframe src="{notebook_url}" width="800" height="600" frameborder="0"></iframe>',
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
