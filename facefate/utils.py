import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini API key
genai.configure(api_key="AIzaSyC0lY3dWDTRsi-lrf4vhS79VcYsAgii3Zw")  # Replace with environment variable for production

# Load Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_responses(name, img_bytes):
    image = Image.open(io.BytesIO(img_bytes))

    prompt = f"""
    This is {name}. Based on their image:

    1. Rate their face from 1 to 10 (just give the number, no extra text).
    2. Roast them like a stand-up comedian in just 2 or 3 lines.
    3. As a funny fortune teller, tell them their fate in 2 or 3 lines.
    4. Guess their age (just a number only).

    Be brief, funny, and to the point.
    """

    response = model.generate_content([prompt, image])
    output = response.text.strip().split("\n")

    # Extract responses
    ugly_score = output[0].strip()
    roast_lines = []
    fate_lines = []
    age_guess = ""

    # Classify the lines into roast/fate/age
    for line in output[1:]:
        line = line.strip()
        if line.isdigit() and not age_guess:
            age_guess = line
        elif len(roast_lines) < 3:
            roast_lines.append(line)
        elif len(fate_lines) < 3:
            fate_lines.append(line)

    roast = "\n".join(roast_lines).strip()
    fortune = "\n".join(fate_lines).strip()

    return ugly_score, roast, fortune, age_guess