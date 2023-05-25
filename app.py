import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

genders = ["FEMALE", "MALE"]
stages = ["I", "II", "III"]
histologies = ["Infiltrating Ductal Carinoma", "Infiltrating Lobular Carcinoma", "Mucinous  Carcinoma"]
ers = ["Positive"]
prs = ["Positive"]
hers = ["Negative", "Positive"]
types = ["Lumpectomy", "Modified Radical Mastectomy", "Other", "Simple Mastectomy"]

age = st.number_input("Age")
gender = st.selectbox("Gender", genders)
p1 = st.number_input("Protein 1")
p2 = st.number_input("Protein 2")
p3 = st.number_input("Protein 3")
p4 = st.number_input("Protein 4")
stage = st.selectbox("Tumour Stage", stages)
histology = st.selectbox("Histology", histologies)
er = st.selectbox("ER Status", ers)
pr = st.selectbox("PR Status", prs)
her = st.selectbox("HER2 Status", hers)
surgery = st.selectbox("Surgery Type", types)

if st.button("Predict"):
	gender = genders.index(gender)
	stage = stages.index(stage)
	histology = histologies.index(histology)
	er = ers.index(er)
	pr = prs.index(pr)
	her = hers.index(her)
	surgery = types.index(surgery)
	test = np.array([[age, gender, p1, p2, p3, p4, stage, histology, er, pr, her, surgery]])
	res = model.predict(test)
	print(res)
	st.success("Prediction: " + str(res[0]))
