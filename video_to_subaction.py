import cv2
import base64
import google.generativeai as genai
import google.generativeai as genai
from IPython.display import Markdown
import time

def capture_and_save_video(video_path):
    cap = cv2.VideoCapture("combined_task - Made with Clipchamp.mp4")  # Use the default webcam (change to the appropriate index if you have multiple webcams)
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



genai.configure(api_key="Your API KEY")
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
                                  {"text": "You are a robotic manipulator whose task is to generate a sequence of subtasks along with the object to be operated upon."},
                                  {"text": "The possible set of subactions that you can perform are: [Reach, Tilt, Retract, Grasp, Release, Stir, Wipe, Press, Rotate, pick, place, open, close, insert, remove, move, Reach_2]"},
                                  {"text": "do not add tilt in pick and place task and always use reach first"},
                                  {"text": "use retract only at the end of subtasks"},
                                  {"text": "make sure that the subaction will not repeat and retract will always come at the end of the sequence"}
]

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file] + messages,
                                                                request_options={"timeout": 600})

# Print the response, rendering any Markdown
Markdown(response.text)

print(response.text)
