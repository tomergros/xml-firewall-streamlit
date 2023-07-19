import streamlit as st
import xmlschema

def validate_xml(xsd_content, xml_content):
    try:
        xsd = xmlschema.XMLSchema(xsd_content)
        if xsd.is_valid(xml_content):
            st.success("XML is valid")
        else:
            try:
                xsd.validate(xml_content)
            except Exception as e:
                st.error("XML is not valid: " + str(e))
    except Exception as r:
        st.error("An error occurred during XML validation: " + str(r))

def main():
    st.set_page_config(
        page_title="xml-firewall",
        page_icon=":Rocket:",
        layout="wide",
    )

    # Uncomment the CSS style to center the titles and button
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
        }
        .upload-title {
            font-size: 20px;
        }
        .center {
            display: flex;
            justify-content: center;
        # }
        # .validate-button {
        #     font-size: 24px;
        #     padding: 12px 30px;
        # }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # st.title("Kaggle Notebook Viewer and XML Firewall")
    st.markdown("<h1 style='color: #ffffff; text-align: center;'>Kaggle Notebook Viewer</h1>", unsafe_allow_html=True)

    # Kaggle Notebook Viewer
    st.markdown("<h1 style='color: #ff6347; text-align: center;'>Kaggle Notebook Viewer</h1>", unsafe_allow_html=True)
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
    # st.title("XML Firewall")
    st.markdown("<h1 style='color: #ffffff; text-align: center;'>XML Firewall</h1>", unsafe_allow_html=True)

    st.markdown("<p class='upload-title' style='text-align: center; font-size: 30px;'>Upload XSD File</p>", unsafe_allow_html=True)
    xsd_file = st.file_uploader("", type=["xsd"])

    st.markdown("<p class='upload-title' style='text-align: center; font-size: 30px;'>Upload XML File</p>", unsafe_allow_html=True)
    xml_file = st.file_uploader("", type=["xml"])

    # st.markdown("<div class='center' style='text-align: center; font-size: 30px;'><button class='validate-button'>Validate</button></div>", unsafe_allow_html=True)

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
