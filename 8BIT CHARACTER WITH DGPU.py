import torch
from torchvision.utils import save_image
from your_gan_model import PixelArtGAN  # Assume you have a pre-trained model

# Ensure GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the pre-trained GAN model
model = PixelArtGAN().to(device)
model.eval()

# Convert prompt to a latent vector (e.g., using a simple text-to-vector mapping)
prompt = "hero"
latent_vector = torch.randn(1, 100).to(device)  # Replace with actual prompt encoding logic

# Generate an 8-bit character
with torch.no_grad():
    generated_image = model(latent_vector)

# Save the result
save_image(generated_image, "8bit_character.png")
print("8-bit character generated and saved as 8bit_character.png")