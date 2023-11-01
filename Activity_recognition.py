# activity_recognition.py
"""
This module recognizes human activities in frames.
"""

import os
import requests
from PIL import Image
import datetime
from transformers import BlipProcessor, BlipForConditionalGeneration
import logging
import pandas as pd
import datetime



logging.basicConfig(
    filename='activity_recognition.log',  # Set the log file
    level=logging.DEBUG,   # Set the minimum log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('activity_recognition')

#load the model
processor = BlipProcessor.from_pretrained(r"C:\Users\HP\Desktop\lokesh\salesforce_blip\blip-image-captioning-large") #location
model = BlipForConditionalGeneration.from_pretrained(r"C:\Users\HP\Desktop\lokesh\salesforce_blip\blip-image-captioning-large") #location
logger.info(f"All the model files have been loaded.")

#folder path
folder_path =  r'C:\Users\HP\Desktop\lokesh\frame_captured'


data = {'timestamp': [], 'response': []}
df = pd.DataFrame(data)
def add_row(response_data):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_row = {'timestamp': timestamp, 'response': response_data}
    df.loc[len(df)] = new_row


def recognize_activity():
    if not os.path.exists(folder_path):
        logger.error(f"The folder '{folder_path}' does not exist.")
            #print(f"The folder '{folder_path}' does not exist.")
    else:
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        if not image_files:
            logger.error("No image files found in the folder.")
        else:
            for image_file in image_files:
                image_path = os.path.join(folder_path, image_file)
                print(f"processing {image_path}")
                raw_image = Image.open(image_path).convert('RGB')
                inputs = processor(raw_image, return_tensors="pt")
                out = model.generate(**inputs)
                response_data = processor.decode(out[0], skip_special_tokens=True)
                add_row(response_data)
    return df
activity_df = recognize_activity()
activity_df.to_csv(r'C:\Users\HP\Desktop\lokesh\frame_captured\activity_datafile')