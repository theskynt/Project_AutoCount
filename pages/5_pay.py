import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
import cv2
import numpy as np

st.markdown("<h1 style='text-align: center; color: white;'>Detr Model</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    model = DetrForObjectDetection.from_pretrained("Komet/my-fruit-detection-2", ignore_mismatched_sizes=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    processor = DetrImageProcessor.from_pretrained("Komet/my-fruit-detection-2", ignore_mismatched_sizes=True)

    camera = st.camera_input("Take a photo")
    data_in = []
    
    if camera is not None:
        # Specify the path where you want to save the captured photo
        photo_path = 'captured_photo.jpg'

        # Save the captured photo
        with open(photo_path, 'wb') as f:
            f.write(camera.getvalue())

        image = cv2.imread(photo_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (640, 480))

        def plot_results(pil_img, scores, labels, boxes):

            label2class = {
                1: "apple",
                2: "banana",
                3: "orange"
            }

            plt.figure(figsize=(16, 10))
            plt.imshow(pil_img)
            ax = plt.gca()
            colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()
            for score, label, (xmin, ymin, xmax, ymax), color in zip(scores.tolist(), labels.tolist(), boxes.tolist(), colors):
                ax.add_patch(patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                            fill=False, color=color, linewidth=2))
                class_name = label2class.get(label, f'Class {label}')
                data_in.append(class_name)
                text = f'{class_name}: {score:.2f}'
                ax.text(xmin, ymin, text, fontsize=12,
                        bbox=dict(facecolor='white', alpha=0.5))
            st.write("รูปที่เข้าโมเดลแล้ว")
            plt.axis('off')
            st.pyplot(plt)
            

        with torch.no_grad():
            inputs = processor(images=image, return_tensors="pt").to(device)
            outputs = model(**inputs)
            postprocessed_outputs = processor.post_process_object_detection(outputs, target_sizes=[(480, 640)], threshold=0.7)
            results = postprocessed_outputs[0]

            pil_image = Image.fromarray(image)
            plot_results(pil_image, results["scores"], results["labels"], results["boxes"])
            


# col1, col2 = st.columns([1, 1])
with col2:
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
        
    name_list = []
    price_list = []
    for item in data_in:
        if item in data['pice']:
            name_list.append(item)
            price_list.append(data['pice'][item])

    df = pd.DataFrame({'Name': name_list, 'Price': price_list})
    st.dataframe(df)

    total_price = df['Price'].sum()

    st.write(
        f'<div style="font-size: 20px;">Total Price: {total_price}</div>',
        unsafe_allow_html=True
    )

with col2:
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                width: 150px; 
            }
            """,
    ):
        if st.button("Pay"):
            st.session_state.total_price = total_price
            switch_page("QR")

    with stylable_container(
        key="red_button",
        css_styles="""
            button {
                background-color: red;
                color: white;
                width: 150px; 
            }
            """,
    ):
        if st.button("Cancel"):
            switch_page("main")

