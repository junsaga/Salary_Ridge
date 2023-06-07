import streamlit as st
import numpy as np
import joblib
import sklearn
def run_app_ml():
    st.subheader('연봉 금액 예측')

    # 성별,나이,연봉,카드빚,자산을
    # 유저한테 입력받는다
    gender = st.radio("성별 선택",['남자','여자'])
    if gender =='여자':
        gender =0
    else:
        gender =1
    
    EducationLevel = st.radio("학력 선택",['고졸','학사','석사','박사'])
    if EducationLevel =='고졸':
        EducationLevel =2
    elif EducationLevel =='학사':
        EducationLevel =0 or 1
    elif EducationLevel =='석사':
        EducationLevel =3 or 4
    elif EducationLevel =='박사':
        EducationLevel ==5

    YE=st.number_input('Years of Experience',0,35)
    age=st.number_input('age',0,100)