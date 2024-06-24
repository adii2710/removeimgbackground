# test_app.py
import streamlit as st

def main():
    st.title("Test ONNX Runtime")
    try:
        import onnxruntime as ort
        st.success("ONNX Runtime imported successfully!")
    except Exception as e:
        st.error(f"Failed to import ONNX Runtime: {e}")

if __name__ == "__main__":
    main()
