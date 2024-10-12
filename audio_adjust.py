import librosa
import soundfile as sf

def change_playback_speed(input_file, output_file, speed_factor):
    """
    Changes the playback speed of an MP3 audio file without affecting its pitch or quality.

    Args:
        input_file (str): Path to the input MP3 file.
        output_file (str): Path to the output MP3 file.
        speed_factor (float): Desired speed factor (e.g., 1.2 for 20% faster, 0.8 for 20% slower).
    """

    # Load the audio file
    y, sr = librosa.load(input_file)

    # Check if the audio data is valid
    if len(y) == 0:
        print(f"Error: The audio file '{input_file}' is empty or corrupted.")
        return

    # Change the playback speed using time stretching
    y_stretched = librosa.effects.time_stretch(y, rate=speed_factor)

    # Save the modified audio
    sf.write(output_file, y_stretched, sr)

def main():
    # Example usage
    input_file = "/Users/chrisrhodes/Documents/YouTube_Shorts/mysterious_knock/audio/mysterious_knock_audio.mp3"
    output_file = "/Users/chrisrhodes/Documents/YouTube_Shorts/mysterious_knock/audio/mysterious_knock_audio_1.1.mp3"
    speed_factor = 1.1  # Increase speed by 20%

    change_playback_speed(input_file, output_file, speed_factor)

if __name__ == "__main__":
    main()
