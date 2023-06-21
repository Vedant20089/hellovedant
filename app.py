import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Eq Solution", page_icon=":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_e27xvycf.json")

with st.container():
    st.subheader("Hi, I am Vedant :wave:")
    st.title("A Data Analyst From India")
    st.write("I am passionate about findings ways to use Python and VBA to be more efficient and effective in business settings. ")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I create programs using python which helps students to solve caculations or maths problems easily.")

    with right_column:
        st_lottie(lottie_coding, height = 300 , key="Maths")

    with st.container():
        st.write("---")
        st.header("Get in touch with me!")
        st.write("##")

        contact_form = """<form action="https://formsubmit.co/arunsinghvedant@gmail.com" method="POST">
     <input type ="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()



