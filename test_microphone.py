import speech_recognition as sr

def test_microphone():
    recognizer = sr.Recognizer()
    
    # List available microphones
    print("Available microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone {index}: {name}")
    
    try:
        with sr.Microphone(device_index=YOUR_INDEX_HERE) as source:
            print("\nTesting microphone...")
            print("Please speak something...")
            
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Listen for audio
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            print("Processing speech...")
            
            # Recognize speech
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            
    except sr.WaitTimeoutError:
        print("No speech detected within timeout period")
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_microphone() 