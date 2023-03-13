import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

if "model" not in st.session_state:
    st.session_state['model'] = AutoModelForSeq2SeqLM.from_pretrained('/wangcan/T5/model-t5-base/checkpoint-74500/')
if "tokenizer" not in st.session_state:
    st.session_state['tokenizer'] = AutoTokenizer.from_pretrained('/wangcan/T5/model-t5-base/checkpoint-74500/')

st.set_page_config(
    page_title="My_services",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("View, manage, and edit your services!")
with st.sidebar:
    c1,c2 = st.columns(2)
    with c1:
        st.button("Create")
    with c2:
        st.button("Manage")
    
def gen(abstract):
    temperature = 0.9
    num_beams = 2
    max_gen_length = 512
    inputs = st.session_state['tokenizer']([abstract], max_length=512, return_tensors='pt')
    title_ids = st.session_state['model'].generate(
        inputs['input_ids'], 
        num_beams=num_beams, 
        temperature=temperature, 
        max_length=max_gen_length, 
        early_stopping=True
    )
    title = st.session_state['tokenizer'].decode(title_ids[0].tolist(), skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return title

req_df = pd.DataFrame(
[
    {"name": "resourceGroupName", "type": "string", "required": True, "format":None, "desc":None},
    {"name": "id", "type": "interger", "required": True, "format":None, "desc":None},
    # {"name": "st.selectbox", "type": "interger", "required": True, "format":None, "desc":None},
    # {"name": "st.selectbox", "type": "interger", "required": True, "format":None, "desc":None},
]
)
rep_df = pd.DataFrame(
[
    # {"name": "id", "type": "interger", "required": True, "format":None, "desc":None},
    # {"name": "st.selectbox", "type": "interger", "required": True, "format":None, "desc":None},
    # {"name": "st.selectbox", "type": "interger", "required": True, "format":None, "desc":None},
]
)
if "req_df" not in st.session_state:
    st.session_state["req_df"] = req_df
if "rep_df" not in st.session_state:
    st.session_state["rep_df"] = rep_df

st.write("## Demo API")

l_co, input_col, emtpy_col = st.columns([2,8,5])
with l_co:
    st.write('<font size="4.5">api-id:</font>', unsafe_allow_html =True)
    st.write('<font size="0.5">         </font>', unsafe_allow_html =True)
    st.write('<font size="4.5">api-path:</font>', unsafe_allow_html =True)
    st.write('<font size="0.5">         </font>', unsafe_allow_html =True)
    st.write('<font size="4.5">api-type:</font>', unsafe_allow_html =True)
    st.write('<font size="0.5">         </font>', unsafe_allow_html =True)
    st.write('<font size="4.5">api-desc:</font>', unsafe_allow_html =True)
with input_col:
    st.write("  27462")
    # st.write("["+ apipath + "]("+apipath+")")
    st.write('<font size="0.5">         </font>', unsafe_allow_html =True)
    apipath = st.text_input(label="", value="netstore.www/network/gateway",placeholder = "please enter your api path here.",label_visibility ='collapsed')
    apitype = st.selectbox(label="", options=["GET","PUSH","DELETE"],label_visibility ='collapsed')
    apidesc = st.text_input(label="", value="Deletes the specified local network gateway",placeholder = "please enter your api descriptions here.",label_visibility ='collapsed')

st.write('<font size="0.5">           </font>', unsafe_allow_html =True)
st.write("### Request-param")
reqed_df = st.experimental_data_editor(st.session_state["req_df"], num_rows="dynamic",use_container_width=True)

st.write('<font size="0.5">           </font>', unsafe_allow_html =True)
st.write("### Response-param")
reped_df = st.experimental_data_editor(st.session_state.rep_df, num_rows="dynamic",use_container_width=True)

if st.button('Automatically generate parameter descriptions'):
    abstracts = []
    for i in range(len(reqed_df)):
        abstracts.append("desc:"+apidesc+"#name:"+str(reqed_df.loc[i,'name'])+"#type"+str(reqed_df.loc[i,'type']))
    for i in range(len(reqed_df)):
        reqed_df.loc[i,'desc'] = gen(abstracts[i])
    st.session_state["req_df"] = reqed_df.copy()
    st.experimental_rerun()
    
# st.write(req_df.loc[0]['desc'])
# submitted = st.form_submit_button("Submit")

