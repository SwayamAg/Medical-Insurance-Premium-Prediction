
# 🏥 Medical Insurance Premium Prediction App  

This repository contains an interactive Streamlit-based web application designed to predict medical insurance premiums using Machine Learning models. The project leverages multiple ML algorithms and provides insights into model performance through comparison graphs. Users can input relevant details (such as age, BMI, and more) and get real-time premium predictions based on the trained model.  

---

## 🌟 Features  
- **User-Friendly Interface**:  
  Built with Streamlit, the app offers a simple and interactive UI for seamless user experience.  

- **📈 Model Comparison**:  
  Includes a comprehensive comparison of ML models (Random Forest, Gradient Boosting, XGBoost, etc.) to showcase performance metrics like R² scores.  

- **Interactive Visualizations**:  
  Graphs and charts comparing untuned and tuned model performances to highlight improvements.  

  ### Model Performance Comparison:  
  ![Model Performance Graph](graph.png)  

- **Real-Time Predictions**:  
  Users can input their details and instantly get personalized medical insurance premium predictions.  

---

## 🧩 How It Works  
The app takes user input (like age, BMI, etc.) and uses the selected machine learning model to predict the insurance premium based on trained patterns from the dataset. The ML models were trained on historical insurance data to learn the relationship between user features and insurance costs.  

---

## 🧰 Technologies Used  
- **Machine Learning Libraries**:  
  - Scikit-Learn  
  - XGBoost  

- **Data Handling & Visualization**:  
  - Pandas, NumPy  
  - Altair, Matplotlib  

- **Web Framework**:  
  - Streamlit  

---

## 🎯 How to Run the App Locally  
1. **Clone the Repository:**  
   ```bash  
   git clone https://github.com/yourusername/medical-insurance-premium-prediction.git  
   cd medical-insurance-premium-prediction  
   ```  
2. **Install the Required Packages:**  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. **Run the Streamlit App:**  
   ```bash  
   streamlit run app.py  
   ```  

---

## 🎥 Demo Video  
A detailed walkthrough and demonstration of the app’s features, user interface, and real-time prediction functionality can be found in the demo video below:  

[Watch the Demo Video](link-to-demo-video)

---

## 📜 License  
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  

---

## 💡 Call-to-Action  
Feel free to fork this repository, open issues, and submit pull requests! We welcome feedback, suggestions, and contributions to improve the app and expand its functionality.  
