import streamlit as st

def main():
    st.title("Kaggle Notebook Viewer")

    # Hardcoded Kaggle notebook URL
    notebook_url = 'https://www.kaggle.com/code/tomergrossy/xml-firewall-cyber-attacks-classification'

    # Display the Kaggle notebook
    st.markdown(f"XML- Firewall: Cyber Attacks Classification")
    st.components.v1.html(f'<iframe src="{notebook_url}" width="800" height="600" frameborder="0"></iframe>', height=600)

if __name__ == '__main__':
    main()
