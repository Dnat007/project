from flask import Flask ,render_template , request
import joblib 
from keras.preprocessing import image
import numpy as np

app  = Flask(__name__)

model = joblib.load('rf_model1.pkl')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    return render_template("page2.html")
  
@app.route('/prediction',methods=["GET",'POST'])
def prediction():
    if request.method =="POST":
        f = request.files['img']
        f.save('img.jpg')
        
    img = image.load_img('img.jpg', target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array_reshaped = img_array.reshape(1, -1)

    class_index = model.predict(img_array_reshaped)[0]
    print(class_index)
    class_names = ['Building', 'Forest', 'Glacier', 'Mountains', 'Sea', 'Streets']
    predicted_class = class_names[class_index]
    return render_template('prediction.html', data=predicted_class, name='img.jpg')

if __name__ == "__main__":
    app.run(debug=True)