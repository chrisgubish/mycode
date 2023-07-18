from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_tdee():
    if request.method == 'POST':
        weight_cm = float(request.form.get('weight')) * 0.454   # converts from lbs to kg
        height_kg = float(request.form.get('height')) * 2.54    # converts from inches to cm
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        activity_level = request.form.get("activity_level")

    # Revised Harris-Benedict Equations
        if sex == 'male':
            bmr = 88.382 + (13.397 * weight_cm) + (4.799 * height_kg) - (5.677 * age)

        elif sex == 'female':
            bmr = 447.593 + (9.247 * weight_cm) + (3.098 * height_kg) - (4.330 * age)
        else:
            return 'Please select your sex.' 
        
        if activity_level == 'sedentary':
            tdee = bmr * 1.2
            
        elif activity_level == 'lightly active':
            tdee = bmr * 1.375
        elif activity_level == 'active':
            tdee = bmr * 1.55
        elif activity_level == 'very active':
            tdee = bmr * 1.725
        elif activity_level == 'extremely active':
            tdee = bmr * 1.9
        else:
            return "Please select your average activity level"

        return redirect(url_for('calculate_results', tdee=tdee, bmr=bmr))       
           
    return render_template("testlink.html")

@app.route('/calculate_results', methods=['GET'])
def calculate_results():
        tdee_result = request.args.get('tdee')
        bmr_result = request.args.get('bmr')
        
        if tdee_result and bmr_result:
            tdee = tdee_result
            bmr = bmr_result
            return render_template('results.html', tdee=tdee, bmr=bmr)
    
        return redirect(url_for('calculate_tdee'))
    
    
if __name__ == "__main__":
    app.run(debug=True)      #runs on local host ip 127.0.0.0 , port 5000