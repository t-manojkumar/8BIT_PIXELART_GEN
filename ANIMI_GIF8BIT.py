from PIL import Image, ImageDraw, ImageFont
import imageio # type: ignore
import os

# Configuration
character_text = "Manoj"
frame_size = (64, 64)
font_size = 16
num_frames = 8
output_gif = "C:/Users/Manoj/Documents/PROJECTS/8bit_character.gif"
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Create a temporary folder for frames
os.makedirs("frames", exist_ok=True)

# Load a pixel font
font = ImageFont.load_default()  # Use default font as placeholder

# Create frames
for i in range(num_frames):
    img = Image.new("RGB", frame_size, (0, 0, 0))
    draw = ImageDraw.Draw(img)
    color = colors[i % len(colors)]
    
    # Draw character text
    text_position = (frame_size[0] // 4, frame_size[1] // 3)
    draw.text(text_position, character_text, font=font, fill=color)
    
    # Save frame
    frame_path = os.path.join("frames", f"frame_{i}.png")
    img.save(frame_path)

# Create GIF
import imageio.v2 as imageio
frames = [imageio.imread(os.path.join("frames", f"frame_{i}.png")) for i in range(num_frames)]
imageio.mimsave(output_gif, frames, duration=0.2)

# Cleanup temporary frames
for frame_file in os.listdir("frames"):
    os.remove(os.path.join("frames", frame_file))
os.rmdir("frames")

print(f"Animated GIF saved as {output_gif}")
