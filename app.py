from flask import Flask, render_template,request
from src.piplines.predition_pipline import Getdatafromuser, PredictPipeline
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/index')
def indexx():
   return render_template("index.html")



@app.route('/predict', methods=['POST'])
def prediction():
    if float(request.method == 'POST'):
        data = Getdatafromuser( 
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
            )

        # Now call the method for the create dataframe
        new_unseen_data = data.get_data_as_dataframe()

        # now call the predict pipeline for the getting the data 
        predic_result = PredictPipeline()
        prediction_for_unseen_data = predic_result.predict(new_unseen_data)



        return render_template('result.html', final_result = prediction_for_unseen_data)







if __name__ == "__main__":
    app.run(debug = True)
