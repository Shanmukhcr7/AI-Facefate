import google.generativeai as genai
from PIL import Image
import io

# Configure Gemini
genai.configure(api_key="AIzaSyC0lY3dWDTRsi-lrf4vhS79VcYsAgii3Zw")  # Replace with your actual key
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_responses(name, img_bytes):
    # Open and resize image
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    image.thumbnail((512, 512))  # Resize image for speed

    # Prompt 1: Ugly face rating (only a number)
    resp1 = model.generate_content([
        f"Rate {name}'s beauty from 1 (worst) to 10 (best). Be funny but only return a number, no explanation.", image
    ])
    ugly_score = resp1.text.strip()

    # Prompt 2: Roast (2-3 lines)
    resp2 = model.generate_content([
        f"Roast {name} like a stand-up comedian in 2-3 lines. Make it funny!", image
    ])
    roast = resp2.text.strip()

    # Prompt 3: Funny fate (2-3 lines)
    resp3 = model.generate_content([
        f"As a fortune teller, tell {name}'s funny fate in 2-3 lines."
    ])
    fortune = resp3.text.strip()

    # Prompt 4: Age guessing (just number)
    resp4 = model.generate_content([
        f"Guess the age of {name} from the image. Return only a number.", image
    ])
    age_guess = resp4.text.strip()

    return ugly_score, roast, fortune, age_guess