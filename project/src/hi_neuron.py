import streamlit as st


# Introduction
st.markdown(
    """
    <div style="text-align:center; margin-top: 20px; margin-bottom: 20px;">
        <a href="https://git.io/typing-svg">
            <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&pause=1000&color=00C8FF&center=true&vCenter=true&width=600&lines=Exploring+deeper+into+neurons!;Try+it!" alt="Typing SVG">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


st.image("images/image.png")
st.title("Hi neuron!")

# Tabs
#----------------
tab1, tab2, tab3 = st.tabs(["One entry", "Two entries", "Three entries and bias"])



#----------------
# Page 1
#----------------
tab1_weight = tab1.slider("Weight: ", min_value=1.0, max_value=5.0)
tab1_entry = tab1.number_input("Enter the input value")
tab1_button = tab1.button("Calculate output", key="output_1")

if tab1_button:
    tab1.write(f"The output of the neuron is: {tab1_weight * tab1_entry:.2f}")




#-------
# Page 2
#-------

with tab2:
    col1, col2 = st.columns(2)
    
    tab2_weight_1 = col1.slider("Weight W0", min_value=1.0, max_value=5.0, key="tab2_weight_0")
    tab2_entry_1  = col1.number_input("Input X0", key="tab2_entry_0")

    tab2_weight_2 = col2.slider("Weight W1", min_value=1.0, max_value=5.0, key="tab2_weight_1")
    tab2_entry_2  = col2.number_input("Input X1", key="tab2_entry_1")

tab2_button = tab2.button("Calculate output", key="output_2")

if tab2_button:
    tab2.write(f"The output of the neuron is: {(tab2_weight_1 * tab2_entry_1) + (tab2_weight_2 * tab2_entry_2):.2f}")




#----------
# Page 3
#---------
with tab3:
    col1, col2, col3 = st.columns(3)

    # Weights, inputs and bias
    #------------------------
    tab3_weight_1 = col1.slider("Weight W0", min_value=1.0, max_value=5.0, key="tab3_weight_0")
    tab3_entry_1  = col1.number_input("Input X0", key="tab3_input_0")

    tab3_weight_2 = col2.slider("Weight W1", min_value=1.0, max_value=5.0, key="tab3_weight_1")
    tab3_entry_2  = col2.number_input("Input X1", key="tab3_input_1")

    tab3_weight_3 = col3.slider("Weight W2", min_value=1.0, max_value=5.0, key="tab3_weight_2")
    tab3_entry_3  = col3.number_input("Input X2", key="tab3_input_2")

    tab3_bias = tab3.number_input("Enter the bias value: ")



    # Calculation
    #----------
    tab3_button = tab3.button("Calculate output: ", key="output3")
    if tab3_button:
        tab3.write(f"The output of the neuron is: {(tab3_weight_1 * tab3_entry_1) + (tab3_weight_2 * tab3_entry_2) + (tab3_weight_3 * tab3_entry_3) + tab3_bias:.2f}")