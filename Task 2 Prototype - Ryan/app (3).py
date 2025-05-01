#----------------------------------------------------------------------------------------------------------------
#Imports necessary extensions
#----------------------------------------------------------------------------------------------------------------
import os
import csv
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#----------------------------------------------------------------------------------------------------------------
# -- Index Page python routing --
#----------------------------------------------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/index")
def Home_page():
    return render_template("index.html")

#----------------------------------------------------------------------------------------------------------------
# -- Educational Resource Pages
#----------------------------------------------------------------------------------------------------------------

@app.route("/EducationalResourcesP1")
def Education_page1():
    return render_template("EducationalResourcesP1.html")

@app.route("/EducationalResourcesP2")
def Education_page2():
    return render_template("EducationalResourcesP2.html")

@app.route("/EducationalResourcesP3")
def Education_page3():
    return render_template("EducationalResourcesP3.html")

@app.route("/EducationalResourcesP4")
def Education_page4():
    return render_template("EducationalResourcesP4.html")

@app.route("/EducationalResourcesP5")
def Education_page5():
    return render_template("EducationalResourcesP5.html")

@app.route("/EducationalResourcesP6")
def Education_page6():
    return render_template("EducationalResourcesP6.html")

#----------------------------------------------------------------------------------------------------------------
# -- Carbon Footprint Calculator python code --
#----------------------------------------------------------------------------------------------------------------

@app.route('/CarbFootprint')
def CarbFootprint_Calc():
    return render_template("CarbFootprint.html")

#----------------------------------------------------------------------------------------------------------------
# -- Energy usage tracker python code --
#----------------------------------------------------------------------------------------------------------------

@app.route('/EnergyTracker')
def EnergyTracker():
    return render_template("EnergyTracker.html")

#----------------------------------------------------------------------------------------------------------------
# -- Booking System python code --
#----------------------------------------------------------------------------------------------------------------

@app.route('/Bookings_ProductSelection')
def bookings_Products():
    return render_template("Bookings_ProductSelection.html")

@app.route('/Bookings_Forms', methods = ['GET', 'POST'])
def bookings_Forms():
    if request.method == 'POST':
        # Get form data
        FirstName = request.form.get("FirstName")
        LastName = request.form.get("LastName")
        DoB = request.form.get("DOB")
        Booking_Email = request.form.get("Email")
        Phone = request.form.get("PhoneNumber")
        Address = request.form.get("Address")
        date_of_service = request.form.get("BookingDate")

        # Save data to CSV
        file_exists = os.path.isfile("Bookings.csv")
        with open("Bookings.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    "Firstname", "LastName", "DOB", "Email", 
                    "Phone", "Address", "date of service"
                ])
            writer.writerow([
                FirstName, LastName, DoB, Booking_Email, 
                Phone, Address, date_of_service
            ])

        # Return confirmation message
        return render_template(
            "Bookings_Confirmation.html",
        )
    return render_template("Bookings_Forms.html")

#----------------------------------------------------------------------------------------------------------------
# -- Log_In & Sign_Up python code --
#----------------------------------------------------------------------------------------------------------------

@app.route("/Log_in", methods = ['GET', 'POST'])
# ^ Routes to the linked page (Log_in), methods "get" & "Post" are utilised here to grant the page permission to--
#--send and retrieve data between the front end form and backend database.
def LogIn_page():
    data = request.form
    print(data)
    # ^ Requests the data input by the user and prints it inside the terminal, used for testing purposes
    return render_template("Log_in.html")
#   ^ renders the UI template for the log-in page
@app.route("/Sign_Up", methods = ['GET', 'POST'])
def SignUp_Page():
    if request.method == 'POST':
        # Get form data
        Email = request.form.get('Email')
        Username = request.form.get('Username')
        password1 = request.form.get('Password')
        password2 = request.form.get('Repeat_Password')

        #Validation handling - Ensures all inputs meet necessary specifications/requirements
        if len(Email) < 4:
            flash('Email must be greater than 3 characters', category='error')
            
        elif len(Username) < 2:
            flash('name must be greater than 1 characters', category='error')
            
        elif password1 != password2:
            flash('passwords do not match', category='error')
            
        elif len(password1) < 7:
            flash('password must be greater than 6 characters', category='error')
            
        else:
            flash('account created!', category='success')

        #CSV filing - saves all new account registrations to User databse
        file_exists = os.path.isfile("Users.csv")
        with open("Users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    "Username", "Email", "password"
                ])
            writer.writerow([
                Username, Email, password1 
            ])
        return render_template("Sign_Up_Confirmation.html")
    return render_template("Sign_Up.html")

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)

