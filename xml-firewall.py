import streamlit as st

def main():
    st.title('xml-firewall-cyber-attacks-classification')
    
    # Add an iframe to display the Kaggle notebook
    st.components.v1.iframe("ttps://www.kaggle.com/code/tomergrossy/xml-firewall-cyber-attacks-classification", height=1000)
    
if __name__ == '__main__':
    main()
