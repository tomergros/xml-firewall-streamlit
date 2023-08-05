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

    # CSS style to center the titles and button
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

    st.sidebar.title("Menu")
    selected_section = st.sidebar.radio(
        "Go to:",
        ["Section 1", "Section 2", "Section 3"]
    )

    # Insert the image below the title
    image_path = "pics/top.jpg"
    st.image(image_path, use_column_width=True)

    image_path = "xml-firewall-logo.jpg"
    st.image(image_path, use_column_width=True)

    
    # st.title("XML Firewall Project")
    st.markdown("<h1 style='color: #ffffff; text-align: center;'>XML Firewall Project</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Preseted by: Tomer Grossman & Oriel Somech</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Academic Advisor: Dr. Guy Leshem</h5>", unsafe_allow_html=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/what_is_xml_firewall.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/what_is_xml_firewall2.png"

    # Center the image using st.container
    col1, col2, col3 = st.columns(3)
    
    # The first and last columns act as spacers, while the middle column centers the image
    with col1:
        pass
    
    with col2:
        st.image(image_path, caption="XML Firewall Example")
    
    with col3:
        pass

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/purpose.png"
    st.image(image_path, use_column_width=True)

    # # Section 1
    # st.markdown('<h2 style="text-align:center;">רקע</h2>', unsafe_allow_html=True)
    
    # background_text = """
    # בשנים האחרונות פלטפורמת הרשתות החברתיות תפסה תאוצה וכיום היא תופסת מקום משמעותי בחיים של כמעט כל אחד מאיתנו. 
    # הרשתות החברתיות מספקות דרך קלה ונוחה ליצירת קשר ושיתוף עם הסביבה שלנו וגם עם אנשים זרים מכל רחבי העולם. 
    # למעשה, כיום התקשורת המרכזית עם הסביבה שלנו מנוהלת דרך הרשתות החברתיות.
    
    # עם זאת, ולמרות היתרונות שבדבר, קיים גם חיסרון לא מבוטל- בריונות. בריונות ברשת היא הטרדה או העלבת אדם על ידי שליחת הודעה, 
    # פרסום פוסט, תמונה או סירטון בעלי אופי פוגע או מאיים. תופעה זו משפיעה על כל המשתמשים ברשתות. 
    # ועלולה לגרום לנזק לבריאות הנפשית והפיזית של הקורבנות.
    # """
    
    # st.markdown(f'<p style="text-align:center;" dir="rtl">{background_text}</p>', unsafe_allow_html=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/basic_terms1.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/basic_terms2.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    # Video URL or local file path
    video_url = "pics/sqli.mp4"  # Replace this with your video URL or local file path
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>SQL Injection Example</h5>", unsafe_allow_html=True)
    st.video(video_url)

    image_path = "pics/basic_terms3png.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    # Video URL or local file path
    video_url = "pics/DDOS attack on the VideoLAN downloads infrastructure.mp4"  # Replace this with your video URL or local file path

    # Display the video
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>DOS Example</h5>", unsafe_allow_html=True)
    st.video(video_url, format="video/mp4")

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/basic_terms4.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/acdemic_research.png"
    st.image(image_path, use_column_width=True)
    
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    # Replace the URL below with the URL you want to embed
    iframe_url = "https://www.kaggle.com/embed/tomergrossy/xml-firewall-cyber-attacks-classification"
    iframe_code = f'<iframe src="{iframe_url}" height="2000" style="margin: 0 auto; width: 100%; max-width: 2000px;" frameborder="0" scrolling="auto" title="XML- Firewall: Cyber Attacks Classification"></iframe>'

    # Kaggle Notebook Viewer
    st.markdown("<h1 style='color: #ff6347; text-align: center;'>Kaggle Notebook:</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #ff6347; text-align: center;'>Cyber Attacks Classification using DistilBERT</h1>", unsafe_allow_html=True)
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
    
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/basic_instructions.png"
    st.image(image_path, use_column_width=True) 
    
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    # st.markdown('<h1 style="text-align: center; font-weight: bold; font-size: 48px;">Basic Instructions</h1>', unsafe_allow_html=True)
    # st.markdown('<div style="text-align: center; font-weight: bold;">1. Click on the arrow to start the app.</div>', unsafe_allow_html=True)
    # st.markdown('<div style="text-align: center; font-weight: bold;">2. Browse an XSD file.</div>', unsafe_allow_html=True)
    # st.markdown('<div style="text-align: center; font-weight: bold;">3. Browse an XML file.</div>', unsafe_allow_html=True)
    # st.markdown('<div style="text-align: center; font-weight: bold;">4. Click on \'Validate\'.</div>', unsafe_allow_html=True)
    # st.markdown('<div style="text-align: center; font-weight: bold;">That\'s it! You are ready to go!</div>', unsafe_allow_html=True)
    
    # st.title("XML Firewall")
    st.markdown("<h1 style='color: #ff6347; text-align: center;'>XML Firewall - Validation System</h1>", unsafe_allow_html=True)

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
    
    st.markdown("<p class='upload-title' style='text-align: center; font-size: 30px;'></p>", unsafe_allow_html=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/results1.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/results2.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/results3.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/results4.png"
    st.image(image_path, use_column_width=True)

    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    
    image_path = "pics/meet_the_team.jpg"
    st.image(image_path, use_column_width=True)
    
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Special Thanks:</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Our Academic Advisor: Dr. Guy Leshem</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Dr. Avi Yosipof</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Dr. Johnny Alon</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'>Emeritus Prof. Nathan Netanyahu</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: #ffffff; text-align: center;'></h5>", unsafe_allow_html=True)


    image_path = "pics/bottom.png"
    st.image(image_path, use_column_width=True)

if __name__ == "__main__":
    main()
