from flask import Flask, render_template, jsonify, request
import config1
from utils import MedicalInsurence
import traceback
app = Flask(__name__,template_folder="template")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    try:
        if request.method == 'POST':
            data = request.form.get

            print("User Data is :",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = eval(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            medical_ins = MedicalInsurence(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_predicted_price()

            # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
            return  render_template('index.html',prediction = charges)

        else:
            data = request.args.get

            print("User Data is ::::",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = eval(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            medical_ins = MedicalInsurence(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_predicted_price()

            # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
            return  render_template('index.html',prediction = charges)
            
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config1.PORT_NUMBER,debug=True)