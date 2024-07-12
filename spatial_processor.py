import numpy as np
import soundfile as sf
import spaudiopy as spa

def stereo_to_spatial(input_file, output_file, hrir_file_left, hrir_file_right):
    # Load stereo audio file
    stereo_signal, fs = sf.read(input_file)

    # Load HRIRs
    hrirs = spa.io.load_hrirs(fs, filename=hrir_file_left)

    # Apply HRIRs to stereo signal
    spatial_signal_left = spa.processing.apply_hrirs(stereo_signal[:, 0], hrirs.left)
    hrirs = spa.io.load_hrirs(fs, filename=hrir_file_right)
    spatial_signal_right = spa.processing.apply_hrirs(stereo_signal[:, 1], hrirs.right)

    # Combine spatial signals
    spatial_signal = np.column_stack((spatial_signal_left, spatial_signal_right))

    # Save spatial audio
    sf.write(output_file, spatial_signal, fs)

if __name__ == "__main__":
    input_file = "input_audio.wav"
    output_file = "spatial_audio.wav"
    hrir_file_left = "hrir_left.wav"
    hrir_file_right = "hrir_right.wav"

    stereo_to_spatial(input_file, output_file, hrir_file_left, hrir_file_right)
