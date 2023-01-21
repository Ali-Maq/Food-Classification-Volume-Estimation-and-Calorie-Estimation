# Food Classification, Volume Estimation, and Calorie Estimation

This project aims to classify food images, estimate their volume, and estimate their calorie content using a fine-tuned version of the VIT-Base-Patch16-224-in21k model trained on the Food101 dataset. The model uses Apple AR Photogrammetry to obtain an accurate 3D representation of the food, using a 360-degree view of the food uploaded by the user for 30 seconds. The calorie content of the identified food is then obtained using the Nutrionix API.<br>

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.<br>

### &emsp;Prerequisites
&emsp; - Apple AR Photogrammetry Library<br>
&emsp; - Nutrionix API Key (sign up here [https://developer.nutritionix.com/signup] to get your API ID and key)<br>
&emsp; - Any IDE with python installed.<br>

### &emsp;Installation
&emsp; - Open the IDE and clone the repository: git clone https://github.com/Ali-Maq/Food-Classification-Volume-Estimation-and-Calorie-Estimation<br>
&emsp; - Install the required packages: pip install -r requirements.txt<br>
&emsp; - Add your Nutrionix API ID and key to following lines in app.py file:<br>
&emsp;&emsp;"x-app-id": "[YOUR API ID]"<br>
&emsp;&emsp;"x-app-key": "[YOUR NUTRITIONIX API KEY]"<br>

### &emsp;Usage
&emsp; - Run the following command in the terminal: python app.py --image<br>
&emsp; - A local URL will be generated. You can then copy-paste this link in your web browser to run the app.<br>
&emsp; - Upload the food image you want to classify.<br>

## Built With
&emsp; - VIT-Base-Patch16-224-in21k - The base model for food image classification<br>
&emsp; - Food101 Dataset - The dataset used for fine-tuning the model<br>
&emsp; - Apple AR Photogrammetry - Used for obtaining a 3D representation of the food<br>
&emsp; - Nutrionix API - Used for obtaining the calorie content of the identified food<br>

## Contributing
&emsp;Contributions are welcome. To contribute, follow these steps:<br>

&emsp; - Fork the repository.<br>
&emsp; - Create a new branch: git checkout -b my-new-feature<br>
&emsp; - Commit your changes: git commit -am 'Add some feature'<br>
&emsp; - Push to the branch: git push origin my-new-feature<br>
&emsp; - Submit a pull request.<br>

## License
&emsp;This project is licensed under the MIT License - see the LICENSE file for details.





