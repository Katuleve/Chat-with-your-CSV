import streamlit as st
import pandas as pd
import os
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = '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' 

def chat_with_csv (df, prompt):
    llm = OpenAI(OPENAI_API_KEY)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(result)
    return result

st.set_page_config(layout= 'wide')

st.title ('Chat with CSV Powered by LLM')


input_csv = st.file_uploader ('Upload your csv file here', type= ['csv'])


if input_csv is not None:
    
    col1, col2 = st.columns([1,1])

    with col1:
        st.info('Your CSV File')
        data = pd.read_csv(input_csv)
        st.dataframe(data)
    with col2:
        st.info('Chat with your CSV file')

        input_text = st.text_area('Enter your query:')
        if input_text is not None:
            if st.button('Chat with CSV'):
                st.info('Your Query:' + input_text)
                result = chat_with_csv (data, input_text)
                st.success(result)
        