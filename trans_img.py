from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from datetime import datetime

client = genai.Client()

prompt = (
    "hello world, a cat playing with a ball of yarn in a cozy living room, "
)

image = Image.open("target_image.png")
image2 = Image.open("1920x1080-white.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    # contents=[prompt, image],
    contents=[prompt, image, image2],
)

print(response)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        now = datetime.now()
        image.save(f"generated_image_{now.strftime('%Y%m%d_%H%M%S')}.png")