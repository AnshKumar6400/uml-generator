import streamlit as st
from parser import parse_code
from uml_generator import generate_uml, render_uml
import io

st.title("UML Generator")

code_input = st.text_area("Enter your Python code:")

uploaded_files = st.file_uploader("Upload Python files", type="py", accept_multiple_files=True)

if uploaded_files:
    combined_code = ""
    for uploaded_file in uploaded_files:
        code = uploaded_file.read().decode("utf-8")
        combined_code += code + "\n"
    code_input = combined_code
    st.text_area("Combined Python code from files:", code_input, height=300)

if st.button("Generate UML"):
    if code_input.strip():
        try:
            classes = parse_code(code_input)
            uml_code = generate_uml(classes)

            # Save UML to a PNG file in memory
            output_path = 'uml_diagram.png'
            render_uml(uml_code, output_path)

            # Provide download button
            with open(output_path, "rb") as file:
                st.download_button(label="Download UML as PNG",
                                   data=file,
                                   file_name="uml_diagram.png",
                                   mime="image/png")

            st.success("UML diagram generated successfully.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter code or upload files.")
