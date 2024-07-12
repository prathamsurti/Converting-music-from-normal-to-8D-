import streamlit as st
import numpy as np
from scipy.signal import convolve
from scipy.io import wavfile
from Lo_fi import apply_reverb, process_audio, generate_impulse_response




def main():
    st.title("AudioAura Convertor")
    uploaded_file = st.file_uploader("Upload an audio file (.wav)", type=["wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')

        if st.button("Process"):
            with st.spinner("Processing..."):
                # Save uploaded audio file
                with open("input_audio.wav", "wb") as f:
                    f.write(uploaded_file.getvalue())

                # Process audio
                reverb_audio, fs = process_audio("input_audio.wav")

                # Save processed audio
                wavfile.write("output_audio_reverb.wav", fs, (reverb_audio * 32767).astype(np.int16))

            st.success("Processing complete!")

            # Provide download link for processed audio
            st.audio("output_audio_reverb.wav", format='audio/wav')
            st.download_button(label="Download Processed Audio", data=open("output_audio_reverb.wav", "rb").read(), file_name="output_audio_reverb.wav")

if __name__ == "__main__":
    main()
