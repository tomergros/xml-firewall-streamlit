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
        div.stButton > button:first-child {
        background-color: #ce1126;
        color: white;
        height: 3em;
        width: 12em;
        border-radius:10px;
        border:3px solid #000000;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
        }
    
        div.stButton > button:hover {
    	background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
    	background-color:#ce1126;
        }
    
        div.stButton > button:active {
    	position:relative;
    	top:3px;
        }

        .title {
            text-align: center;
        }
        .upload-title {
            font-size: 20px;
        }
        .validate-button {
            display: flex;
            font-size: 24px;
            justify-content: center;
        }
        .stButton button {
            font-size: 24px;
            width: 250px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # st.title("Kaggle Notebook Viewer and XML Firewall")
    st.markdown("<h1 style='color: #ffffff; text-align: center;'>Kaggle Notebook Viewer</h1>", unsafe_allow_html=True)

    # Insert the image below the title
    image_path = "xml-firewall-logo.jpg"
    st.image(image_path, use_column_width=True)

    # Replace the URL below with the URL you want to embed
    iframe_url = "https://www.kaggle.com/embed/tomergrossy/xml-firewall-cyber-attacks-classification"
    iframe_code = f'<iframe src="{iframe_url}" height="2000" style="margin: 0 auto; width: 100%; max-width: 2000px;" frameborder="0" scrolling="auto" title="XML- Firewall: Cyber Attacks Classification"></iframe>'

    # Kaggle Notebook Viewer
    st.markdown("<h1 style='color: #ff6347; text-align: center;'>Kaggle Notebook Viewer</h1>", unsafe_allow_html=True)
    st.write(iframe_code, unsafe_allow_html=True)    

    # html_file_path = r"xml-firewall-cyber-attacks-classification.html"
    # try:
    #     with open(html_file_path, "r", encoding="utf-8") as file:
    #         html_content = file.read()
    #     st.components.v1.html(html_content, height=800, scrolling=True)
    # except FileNotFoundError:
    #     st.error("HTML file not found. Please provide the correct file path.")
    # except Exception as e:
    #     st.error("An error occurred while loading the Kaggle notebook HTML content.")

    # XML Firewall
    # st.title("XML Firewall")
    st.markdown("<h1 style='color: #ffffff; text-align: center;'>XML Firewall</h1>", unsafe_allow_html=True)

    st.markdown("<p class='upload-title' style='text-align: center; font-size: 30px;'>Upload XSD File</p>", unsafe_allow_html=True)
    xsd_file = st.file_uploader("", type=["xsd"])

    st.markdown("<p class='upload-title' style='text-align: center; font-size: 30px;'>Upload XML File</p>", unsafe_allow_html=True)
    xml_file = st.file_uploader("", type=["xml"])

    # st.markdown("<div class='center' style='text-align: center; font-size: 30px;'><button class='validate-button'>Validate</button></div>", unsafe_allow_html=True)
    
    # Center the "Validate" button
    # st.markdown("<div class='center'><button class='validate-button'>Validate</button></div>", unsafe_allow_html=True)
    if st.button("Validate", key="validate-button"):
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
