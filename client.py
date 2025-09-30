import streamlit as st
import requests
import mimetypes

# FastAPI server URL (update this if server runs elsewhere)
SERVER_URL = "http://192.1.1.1:8000/process_video/"

st.title("🎥 Video Processing Client")
st.write("Upload a video and get the grayscale version back.")

# File uploader
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    if st.button("Process Video"):
        with st.spinner("Processing... Please wait..."):
            # Detect MIME type dynamically
            mime_type, _ = mimetypes.guess_type(uploaded_file.name)
            mime_type = mime_type or "application/octet-stream"

            files = {"file": (uploaded_file.name, uploaded_file, mime_type)}

            try:
                response = requests.post(SERVER_URL, files=files)

                if response.status_code == 200:
                    # Save the processed video
                    output_filename = f"gray_{uploaded_file.name}"
                    with open(output_filename, "wb") as f:
                        f.write(response.content)

                    st.success("✅ Video processed successfully!")

                    # Show processed video preview
                    st.video(output_filename)

                    # Detect correct MIME for download button
                    out_mime, _ = mimetypes.guess_type(output_filename)

                    st.download_button(
                        label="📥 Download Processed Video",
                        data=response.content,
                        file_name=output_filename,
                        mime=out_mime or "application/octet-stream"
                    )
                else:
                    st.error(f"❌ Error: {response.status_code}")
            except Exception as e:
                st.error(f"⚠️ Request failed: {e}")
