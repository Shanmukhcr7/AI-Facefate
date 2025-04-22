import google.generativeai as genai
from PIL import Image
import io
import re

# Configure Gemini
genai.configure(api_key="AIzaSyBNcuvyE3rT0KyXRYZvx5M6tMSQv4IMBdU")

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_responses(name, img_bytes):
    # Open image from bytes
    image = Image.open(io.BytesIO(img_bytes))

    # Create a single prompt for all responses
    prompt = f"""
    You are a hilarious AI with mystical and judging powers.

    Here's what you must do for {name}, based on the image provided:
    1. Rate their fabulous face on a scale of 1 (sassy disaster) to 10 (divine beauty). Just say the number.
    2. Roast them like a stand-up comedian. Keep it funny and 3-4 lines only.
    3. Tell them their funny fate for today (2 lines only).
    4. Guess their age. Just a number.

    Clearly label each section like this:
    Ugly Score: <number>
    Roast: <text>
    Fortune: <text>
    Age Guess: <number>
    """

    response = model.generate_content([prompt, image])
    text = response.text.strip()

    # Extract each part using regex
    ugly_score = re.search(r"Ugly Score:\s*(.*)", text)
    roast = re.search(r"Roast:\s*(.*?)(?=Fortune:)", text, re.DOTALL)
    fortune = re.search(r"Fortune:\s*(.*?)(?=Age Guess:)", text, re.DOTALL)
    age_guess = re.search(r"Age Guess:\s*(.*)", text)

    return (
        ugly_score.group(1).strip() if ugly_score else "N/A",
        roast.group(1).strip() if roast else "N/A",
        fortune.group(1).strip() if fortune else "N/A",
        age_guess.group(1).strip() if age_guess else "N/A"
    )