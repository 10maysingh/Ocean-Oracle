# Ocean-Oracle


🌟 **Overview**
---------------

This website leverages Machine Learning (ML) to predict whether a whale is present at a given location and time based on the following input parameters:

-   **Latitude**
-   **Longitude**
-   **Date (Day, Month, Year)**

It provides a simple and intuitive interface where users can input these parameters, and the model will output a prediction of whether a whale is likely to be present.

* * * * *

🎯 **Purpose of the Website**
-----------------------------

The website aims to assist researchers, conservationists, and marine enthusiasts in identifying potential whale presence in specific geographical locations and times. By using historical and environmental data, it predicts the probability of whale occurrence, which can be useful in:

-   **Marine Conservation:** Planning safe shipping routes to avoid harming marine life.
-   **Research:** Assisting marine biologists in studying whale migration patterns and behaviors.
-   **Ecotourism:** Guiding operators to organize whale-watching tours more efficiently.
-   **Environmental Impact Analysis:** Understanding whale habitats to mitigate environmental damage.

* * * * *

🛠️ **How It Works**
--------------------

1.  **User Input:**\
    Enter latitude, longitude, and a specific date (day, month, year) into the form.

2.  **ML Model Prediction:**

    -   The backend processes the input data using a trained ML model.
    -   The model uses pre-processed historical whale sightings, oceanographic data, and time-series analysis to determine the likelihood of whale presence.
3.  **Result Display:**\
    The website outputs either:

    -   **Whale Present**
    -   **Whale Not Present**\
        (Along with confidence scores for the prediction.)

* * * * *

📦 **Technical Details**
------------------------

-   **Frontend:** Built with modern web technologies (e.g., React, HTML/CSS).
-   **Backend:** Powered by Python/Flask for API handling.
-   **ML Model:** A supervised learning model trained on a dataset of historical whale sightings and environmental features.
-   **Database:** Includes a curated dataset of latitude, longitude, and temporal whale observation data.

* * * * *

🚀 **How to Use the Website**
-----------------------------

1.  Open the website in any modern browser.
2.  Fill in the required fields:
    -   Latitude (e.g., `34.0522`)
    -   Longitude (e.g., `-118.2437`)
    -   Date (e.g., `15`, `August`, `2024`)
3.  Click **Predict**.
4.  View the prediction result instantly!

* * * * *

🧑‍💻 **For Developers**
------------------------

Clone the repository and set up the environment to run the website locally.

### **Installation Steps:**

1.  Clone the repository:

    bash

    Copy code

    `git clone https://github.com/your-username/whale-prediction-website.git
    cd whale-prediction-website`

2.  Install dependencies:

    bash

    Copy code

    `pip install -r requirements.txt

3.  Run the application:

    bash

    Copy code

    `python app.py

4.  Open the browser and navigate to:

    arduino

    Copy code

    `http://localhost:5000`

* * * * *

📊 **Future Enhancements**
--------------------------

-   Integrating real-time oceanographic data (e.g., temperature, salinity, chlorophyll levels).
-   Expanding the prediction model to account for seasonal whale migration patterns.
-   Adding visualizations, such as heatmaps, for whale density predictions.
-   Building an API for developers to integrate predictions into other applications.

* * * * *



🙌 **Acknowledgments**
----------------------

Thanks to the researchers, conservationists, and developers who contributed to the datasets and the machine learning model that powers this website.

* * * * *

**Demo:** [Ocean-Oracle](https://ocean-oracle.vercel.app/)\
**Dataset used:** [[Whale sightings Dataset](https://catalog.data.gov/dataset/right-whale-sightings-advisory-system-rwsas1)]\
**Screenshot:**![image](https://github.com/user-attachments/assets/f3d2f72c-84b7-4f4e-9d6d-18f8e696e7a4)![image](https://github.com/user-attachments/assets/b02cb03b-ad13-4775-b3c3-3cab127f96b7)




* * * * *

Enjoy predicting whale presence and helping conserve marine life! 🐋
