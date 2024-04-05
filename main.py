import streamlit as st
import pandas as pd

def main():
    st.title("CSV Query App")

    # File upload section
    st.subheader("Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Query section
        st.subheader("Query Data")
        query = st.text_input("Enter your query:", "")

        # Apply query and display results
        if query:
            try:
                result_df = df.query(f"`{query}`")
                st.write("### Query Result:")
                st.write(result_df)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()