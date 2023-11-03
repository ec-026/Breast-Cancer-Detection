**Breast Cancer Detection Model Deployment**

The breast cancer detection model is built using the XGBoost classifier for its efficiency and accuracy. Below are the steps we followed to train and serialize the model for deployment in a Flask application:

**Data Preparation**
- We loaded the breast cancer dataset from `sklearn.datasets`, performed necessary data preprocessing, and split it into train and test sets.

**Model Training**
- Using the XGBoost algorithm, we trained the model on the training set and evaluated its performance on the test set. The model was fine-tuned with hyperparameter optimization techniques.

**Serialization**
- The trained XGBoost model was serialized into a `.pickle` file, enabling it to be easily loaded into our Flask web service without retraining.

**Flask Integration**
- The `.pickle` model file is utilized in a Flask application to make predictions through a RESTful API. This allows for real-time, accurate cancer detection based on input features.

The final model offers a quick and reliable breast cancer diagnostic tool integrated within a web framework for ease of access and use.

[**Check the live website here**](https://notnormalcoder.pythonanywhere.com/)

[**Check out the training code here**](https://colab.research.google.com/drive/1ktIv4Ab2kjLqWWw4rQKa8bCl6_Qx2XcV?usp=sharing)


**Using This Repository**

To use this repository for running the breast cancer detection Flask application, follow the steps below:

**Prerequisites**
- Ensure that you have `git` and `Python` installed on your system. Python's package manager `pip` should also be installed to handle library installations.

**Cloning the Repository**
- Clone the repository to your local machine using the following command in your terminal or command prompt:

```sh
git clone https://github.com/ec-026/Breast-Cancer-Detection.git
cd breast-cancer-detection
```
**Installing Dependencies**
- Install the necessary Python libraries specified in requirements.txt with pip:
```sh
  pip install -r requirements.txt
```
**Running the Flask Application**
- Once the dependencies are installed, you can run the Flask application using the following command:
```sh
python app.py
```
- This command starts the Flask server, typically on http://127.0.0.1:5000, and you can navigate to this address in your web browser to interact with the application.

## Contact

If you have any questions or comments about this project, please feel free to contact us.

- **Project Maintainer**: [Tejas Singh](mailto:notnormalcoder@gmail.com)
- **Issue Tracker**: Please report any issues on the [GitHub issues page](https://github.com/ec-026/Breast-Cancer-Detection/issues).

Thank you for using or contributing to the Breast Cancer Detection model.

---
