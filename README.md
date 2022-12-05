# Food-Classification-Volume-Estimation-and-Calorie-Estimation
Food Classification and Calorie Estimation using Fine-Tuned VIT-Base-Patch16-224-in21k

This project aims to classify food images and estimate their calorie content using a fine-tuned version of the VIT-Base-Patch16-224-in21k model trained on the Food101 dataset. The model uses Apple AR Photogrammetry to obtain an accurate 3D representation of the food, using a 360-degree view of the food uploaded by the user for 30 seconds. The calorie content of the identified food is then obtained using the Nutrionix API.


Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

Prerequisites
Apple AR Photogrammetry Library
Nutrionix API Key

Installation

Clone the repository:
git clone https://github.com/Ali-Maq/Food-Classification-Volume-Estimation-and-Calorie-Estimation

Install the required packages:
pip install -r requirements.txt


Add your Nutrionix API key to the config.py file:
NUTRIONIX_API_KEY = "[YOUR_API_KEY]"

Usage
To classify and estimate the calorie content of a food image, run the following command:
python classify_and_estimate.py --image [IMAGE_PATH]


Built With
VIT-Base-Patch16-224-in21k - The base model for food image classification
Food101 Dataset - The dataset used for fine-tuning the model
Apple AR Photogrammetry - Used for obtaining a 3D representation of the food
Nutrionix API - Used for obtaining the calorie content of the identified food



Contributing
Contributions are welcome. To contribute, follow these steps:

Fork the repository.
Create a new branch: git checkout -b my-new-feature
Commit your changes: git commit -am 'Add some feature'
Push to the branch: git push origin my-new-feature
Submit a pull request.


License
This project is licensed under the MIT License - see the LICENSE file for details.





