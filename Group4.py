import streamlit as st
import numpy as np

st.set_page_config(page_title = "ACE Toiletz", page_icon = ":poop:", layout = "centered", initial_sidebar_state = "auto")

st.title("ACE Toiletz")

st.subheader("User Report")

st.sidebar.title("Input features")

st.sidebar.subheader("Size")

unit = st.sidebar.radio("Choose unit of measurement", ("inches", "cm"))

if unit == "inches":
	diameter = st.sidebar.slider("Input Diameter", 	0.1, 3.0)
	length = st.sidebar.slider("Input Length", 5, 20)
	area = np.pi * (diameter/2)**2 * length
	area_min = np.pi * (1/2)**2 * 12
	area_max = np.pi * (2/2)**2 * 18
elif unit == "cm":
	diameter = st.sidebar.slider("Input Diameter", 	0.25, 7.5)
	length = st.sidebar.slider("Input Length", 12.5, 50.0)
	area = np.pi * (diameter/2)**2 * length
	area_min = np.pi * (1/2)**2 * 12
	area_max = np.pi * (2/2)**2 * 18

st.sidebar.subheader("Color")
color = st.sidebar.radio("Input Color", ("Brown", "Green", "Yellow", "Black", "Red"))

@st.cache()
def size_report(size):
	if size < area_min:
		return "The sample's size indicates a possibility of fibre deficiency, dehydration, or constipation. If you are consuming enough fibre and fluids, please consult a doctor for a more accurate medical diagnosis."
	elif size > area_max:
		return "The sample's size indicates that your diet is rich in fibre, which is essential to prevent constipation. Keep it up!"
	else:
		return "The sample's size indicates no abnormalities. However, you may benefit from consuming more fibre."

@st.cache()
def color_report(color):
	if (color == "Green") or (color == "Yellow"):
		return "The sample's color indicates that it may be passing through the digestive system too fast. Please consult a doctor for a more accurate medical diagnosis."
	elif color == "Black":
		return "The sample's color indicates a possibility of bleeding in your upper gastrointestinal track. Please consult a doctor for a more accurate medical diagnosis."
	elif color == "Red":
		return "The sample's color indicates a possibility of bleeding in your lower gastrointestinal track. Please consult a doctor for a more accurate medical diagnosis."
	else:
		return "The sample's color indicates no abnormalities. Good job!"

if st.sidebar.button("Generate Report"):
	st.write(size_report(area))
	st.write(color_report(color))
