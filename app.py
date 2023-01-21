import numpy as np
import gradio as gr
import requests
import json

def list_to_dict(data):
    results = {}

    for i in range(len(data)):
        # Access the i-th dictionary in the list using an integer index
        d = data[i]
        # Assign the value of the 'label' key to the 'score' value in the results dictionary
        results[d['label']] = d['score']

    # The results dictionary will now contain the label-score pairs from the data list
    return results

API_URL = "https://api-inference.huggingface.co/models/nateraw/food"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    output = json.loads(response.content.decode("utf-8"))
    return list_to_dict(output),json.dumps(output, indent=2, sort_keys=True)

def get_nutrition_info(food_name):
    #Make request to Nutritionix API
    response = requests.get(
        "https://trackapi.nutritionix.com/v2/search/instant",
        params={"query": food_name},
        headers={
            "x-app-id": "a3663db3",
            "x-app-key": "06eee2ab6e395eb02e4500d70f0fcdee"
        }
    )
    #Parse response and return relevant information
    data = response.json()
    response = data["branded"][0]["photo"]["thumb"]
    val = {
               "food_name": data["branded"][0]["food_name"],
               "calories": data["branded"][0]["nf_calories"],
               "serving_size": data["branded"][0]["serving_qty"],
               "serving_unit": data["branded"][0]["serving_unit"],
               #"images": data["branded"][0]["photo"]
           }
    # Open the image using PIL
    output = json.dumps(val, indent=2, sort_keys=True)
    return output,response

def volume_estimations(ali):
    return None

with gr.Blocks() as demo:
    gr.Markdown("Food-Classification-Calorie-Estimation and Volume-Estimation")
    with gr.Tab("Food Classification"):
        text_input = gr.Image(type="filepath",interactive=True,label="Upload the food Image and Zoom in to the item you want to get the calorie for")
        text_output = [gr.Label(num_top_classes=6),
                       gr.Textbox()
                       ]
        text_button = gr.Button("Food Classification")
    with gr.Tab("Food Calorie Estimation"):
        image_input = gr.Textbox(label="Please enter the name of the Food you want to get calorie")
        image_output = [gr.Textbox(),
                        gr.Image(type="filepath")
                        ]
        image_button = gr.Button("Estimate Calories!")
    with gr.Tab("Volume Estimation"):
        _image_input = gr.Textbox(label="Please Download the Photogrammetry File trained on APPLE AR KIT and follow the instruction mention below to generate the 3D Vortex of the object")
        _image_output = gr.Image()
        gr.Markdown("-----------------------------------------------------------------------------")
        gr.Markdown("Directory where HelloPhotogrammetry app Saved. Example:/Users/ali/Desktop/HelloPhotogrammetry")
        gr.Markdown("Directory where all the images are saved. Example:: ~/Desktop/Burger_Data_3")
        gr.Markdown("Directory where the usdz or obj file has to be saved.  Example: ~/Desktop/Burger_Data_3/Burger.usdz")
        gr.Markdown("File Quality that you want your 3D model to be. Example: --detail medium ")
        gr.Markdown("-----------------------------------------------------------------------------")
        gr.Markdown("/Users/ali/Desktop/HelloPhotogrammetry ~/Desktop/Burger_Data_3  ~/Desktop/Burger_Data_3/Burger.obj --detail medium")
        gr.Markdown("You can download the photogrammetry demo and files using this Google drive link")
        gr.Markdown("-----------------------------------------------------------------------------")
        gr.Markdown("https://drive.google.com/drive/folders/1QrL0Vhvw5GvIQ8fbHfb9EOsnOlPMmXLG?usp=share_link")
        gr.Markdown("-----------------------------------------------------------------------------")



        _image_button = gr.Button("Volume Calculation")
    with gr.Tab("Future Works"):
        gr.Markdown("Future work on Food Classification")
        gr.Markdown(
            "Currently the Model is trained on food-101 Dataset, which has 100 classes, In the future iteration of the project we would like to train the model on UNIMIB Dataset with 256 Food Classes")
        gr.Markdown("Future work on Volume Estimation")
        gr.Markdown(
        "The volume model has been trained on Apple AR Toolkit and thus can be executred only on Apple devices ie a iOS platform, In futur we would like to train the volume model such that it is Platform independent")
        gr.Markdown("Future work on Calorie Estimation")
        gr.Markdown(
    "The Calorie Estimation currently relies on Nutritionix API , In Future Iteration we would like to build our own Custom Database of Major Food Product across New York Restaurent")
        gr.Markdown("https://github.com/Ali-Maq/Food-Classification-Volume-Estimation-and-Calorie-Estimation/blob/main/README.md")

    text_button.click(query, inputs=text_input, outputs=text_output,scroll_to_output=True,show_progress=True)
    image_button.click(get_nutrition_info, inputs=image_input, outputs=image_output,scroll_to_output=True,show_progress=True)
    #_image_button.click(get_nutrition_info, inputs=_image_input, outputs=_image_output)
    with gr.Accordion("Open for More!"):
        gr.Markdown("🍎 Designed and built by Ali Under the Guidance of Professor Dennis Shasha")
        gr.Markdown("Contact me at ali.quidwai@nyu.edu 😊")

demo.launch()