import streamlit as st

def main():
    st.title('xml-firewall-cyber-attacks-classification')
    
    # Add an iframe to display the Kaggle notebook
    st.components.v1.iframe("xml-firewall-cyber-attacks-classification.html", height=1000)
    
if __name__ == '__main__':
    main()
