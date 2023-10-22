import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import json
from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image, ImageDraw
import io

col1, col2 = st.columns([1, 1])

with col1:
    # Load the trained model weights.
    model = YOLO("best.pt")

    # model.predict(source=0, show=True)

    camera = st.camera_input("Take a photo")
    data_in = []

    if camera is not None:
        # Specify the path where you want to save the captured photo
        photo_path = 'captured_photo.jpg'

        # Save the captured photo
        with open(photo_path, 'wb') as f:
            f.write(camera.getvalue())

        # Use the saved photo for prediction
        results = model.predict(photo_path, conf=0.50)

        photo = results[0]
        img = mpimg.imread(photo_path)
        fig, ax = plt.subplots(1)

        # Display predictions
        if results:
            result = results[0]
            img = Image.open(photo_path)
            draw = ImageDraw.Draw(img)

            for box in result.boxes:
                class_id = result.names[box.cls[0].item()]
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)

                # Draw a rectangle around the detected object
                draw.rectangle(cords, outline="red", width=2)

                # Add label for the object type and confidence
                label = f"{class_id}: {conf}"
                draw.text((cords[0], cords[1]), label, fill="red")

                data_in.append(class_id)
                # st.write("Object type:", class_id)
                # st.write("Confidence:", conf)
                # st.write("---")
            
            st.write("รูปที่เข้าโมเดลแล้ว")
            # Display the image with bounding boxes
            st.image(img, caption="Object Detection")
        else:
            st.write("No predictions found.")


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

