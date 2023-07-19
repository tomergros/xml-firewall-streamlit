import streamlit as st
import xmlschema

# Customizing Streamlit app settings
st.set_page_config(
    page_title="xml-firewall",
    page_icon=":smiley:",
    layout="wide",  # You can use 'centered', 'wide', or 'dashboard'
)


def validate_xml(xsd_path, xml_path):
    try:
        xsd = xmlschema.XMLSchema(xsd_path)
        if xsd.is_valid(xml_path):
            st.success("XML is valid")
        else:
            try:
                xsd.validate(xml_path)
            except Exception as e:
                st.error("XML is not valid: " + str(e))
    except Exception as r:
        st.error("An error occurred during XML validation: " + str(r))

def main():
    st.title("Kaggle Notebook Viewer and XML Firewall")

    # Kaggle Notebook Viewer
    st.markdown("<h1 style='color: #ff6347;'>Kaggle Notebook Viewer</h1>", unsafe_allow_html=True)
    html_file_path = r"xml-firewall-cyber-attacks-classification.html"
    try:
        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("HTML file not found. Please provide the correct file path.")
    except Exception as e:
        st.error("An error occurred while loading the Kaggle notebook HTML content.")

    # XML Firewall
    st.title("XML Firewall")

    xsd_file = st.file_uploader("Upload XSD File", type=["xsd"])
    xml_file = st.file_uploader("Upload XML File", type=["xml"])

    if st.button("Validate"):
        if not xsd_file or not xml_file:
            st.warning("Please upload both XSD and XML files.")
        else:
            try:
                xsd_content = xsd_file.read()
                xml_content = xml_file.read()

                validate_xml(xsd_content, xml_content)
            except Exception as e:
                st.error("An error occurred during XML validation: " + str(e))

if __name__ == "__main__":
    main()
