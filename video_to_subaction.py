import cv2
import base64
import google.generativeai as genai
import google.generativeai as genai
from IPython.display import Markdown
import time

def capture_and_save_video(video_path):
    cap = cv2.VideoCapture(1)  # Use the default webcam (change to the appropriate index if you have multiple webcams)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

        # Display the captured frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to stop capturing
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Path to save the captured video
video_path = 'Pro.mp4'

# Capture and save the video
capture_and_save_video(video_path)

# Upload the video and print a confirmation.
video_file_name = "Pro.mp4"



genai.configure(api_key="AIzaSyA0T_PSpejfaSi5Z8Gefke1zMoKm5ucb7s")
# Choose a Gemini API model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")


print(f"Uploading file...")
video_file = genai.upload_file(path=video_file_name)
print(f"Completed upload: {video_file.uri}")



# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(10)
    video_file = genai.get_file(video_file.name)

if video_file.state.name == "FAILED":
  raise ValueError(video_file.state.name)


# Define the message format correctly
messages = [
    {
        "text": "read the video and write a video captioning what human has performed in an input video"},
]

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")#gemini-1.5-pro-latest #gemini-1.5-flash
# Start a chat session
chat_session = model.start_chat()
# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file] + messages,
                                                                request_options={"timeout": 700})

# Print the response, rendering any Markdown
Markdown(response.text)

print(response.text)


messages2 = [
    {"text": response.text},
    {"text": "according the the caption above explain the possible subtasks human has performed"},
    {"text": "The possible set of subactions that you can perform are: [Reach, Tilt, Retract, Grasp, Release, Stir, Wipe, Press, Pick-Up, Place-Down, Move, Reach_2], do not add other subaction based on only given these predict the subactions"},
    {"text": "make sure that the subaction will not repeat and retract will always come at the end of the sequence"},
]

response2 = chat_session.send_message(messages2)
print(response2.text)
