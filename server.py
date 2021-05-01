from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) 

@app.route('/') 
def index():
	return render_template('index.html')


@app.route('/<string:page_name>') 
def html_page(page_name):
	return render_template(page_name)


def write_to_csv(data):
	'''function to write to database.csv'''
	with open('database.csv',newline='',mode='a') as database: 
		email = data['email']
		subject = data['subject']
		message =  data['message']

		csv_writer = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

		#write data to csv file
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST': 
    	try:
	    	data = request.form.to_dict() 
    		write_to_csv(data)
    		return redirect('/thankyou.html') 
    	except:
    		return 'did not save to database'
    else:
    	return 'something went wrong, try again'




