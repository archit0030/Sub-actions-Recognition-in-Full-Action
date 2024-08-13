# Sub-actions-Recognition-in-Full-Action


# Video Capture and Gemini API Integration

This project captures a video, uploads it to the Gemini API, and generates a sequence of subtasks based on the video content. The generated subtasks are designed for a robotic manipulator to operate upon.

## Requirements

- Python 3.9 or above
- OpenCV
- Google Generative AI Client Library
- IPython (for Jupyter Notebook integration)
- Time

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/archit0030/Sub-actions-Recognition-in-Full-Action.git
   cd your-repo-name

2. Install the required packages:
   ```bash
   pip install opencv-python google-generativeai ipython

## Usage

1. Capture and Save Video:
   The script captures video from a default webcam or a specified video file and saves it to 'pro.mp4'.
2. Configure and Use Gemini API:
   Upload the captured video and generate a sequence of subtasks using the Gemini API
3. Replace "YOUR_API_KEY" with the actual Gemini API key.


![Screenshot 2024-08-12 184701](https://github.com/user-attachments/assets/7738105f-333e-4750-a1e3-0f09d82daa5d)
# Results


 ![Input_video](https://github.com/user-attachments/assets/a90af8b0-81bc-40a7-965e-923743641c6a)
  


   *Prediction:*
   A hand reaches into the frame and places an empty yellow bottle in the center of a white surface. 

   Here's a possible breakdown of subactions based on your provided list and the description:
   
   1. **Reach:** The hand initially extends towards the bottle.
   2. **Grasp:** The hand closes around the bottle to get a firm hold.
   3. **Pick-Up:**  The hand lifts the bottle from its original location. 
   4. **Move:** The hand carrying the bottle travels towards the white surface.
   5. **Place-Down:**  The hand sets the bottle onto the white surface.
   6. **Release:** The hand opens, letting go of the bottle.
   7. **Retract:** The hand moves back out of the frame. 
   





