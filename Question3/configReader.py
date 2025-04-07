'''
    Q3. 
    The program should read a configuration file (you can provide them with a sample configuration file).
      
    It should extract specific key-value pairs from the configuration file.
     
    The program should store the extracted information in a data structure (e.g., dictionary or list).
      
    It should handle errors gracefully in case the configuration file is not found or cannot be read.
      
    Finally save the output file data as JSON data in the database.
      
    Create a GET request to fetch this information.
'''
#****************************************************************************************************************************
# Importing the required libraries
#****************************************************************************************************************************
from configparser import ConfigParser
import os
from flask import Flask, jsonify, request
import sqlite3
from collections import defaultdict

#****************************************************************************************************************************
# Function to connect to the SQLite database
#****************************************************************************************************************************
def connect_to_db():    
    conn = sqlite3.connect('C:/WorkRelated/Learning/DB/sampleDB.db')   
    return conn
#****************************************************************************************************************************
# Function to save the extracted data to the database
#   1. Connect to the database
#   2. Create a table if it doesn't exist
#   3. Clear the table before inserting new data
#   4. Insert the extracted data into the table
#****************************************************************************************************************************
def save_to_db(data):
    connection = connect_to_db()
    cursor = connection.cursor()    
    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS config_data (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    clear_db() # Clear the table before inserting new data

    for key, value in data.items():
        cursor.execute('''
        INSERT OR REPLACE INTO config_data (key, value)
        VALUES (?, ?)
        ''', (key, value))
        connection.commit()
    connection.close()
#****************************************************************************************************************************
# Function to read data from the database
#   1. Connect to the database
#   2. Fetch all data from the config_data table
#   3. Close the connection
#   4. Return the fetched data
#****************************************************************************************************************************
def read_from_db():
    connection = connect_to_db()
    result = connection.execute("SELECT * FROM config_data").fetchall()
    connection.close()
    return result
#****************************************************************************************************************************
# Function to read the configuration file and extract key-value pairs   
#   1. Create a ConfigParser object
#   2. Read the configuration file
#   3. Initialize an empty dictionary to store the configuration data
#   4. Loop through each section in the configuration file
#   5. For each section, loop through each key-value pair and store it in the dictionary
#   6. Return the configuration data as a dictionary
#****************************************************************************************************************************
def read_config_data(file_path):
    config = ConfigParser()
    config.read(file_path)
    config_data = {}
    for section in config.sections():
        config_data[section] = {key: value for key, value in config.items(section)}
    return config_data
#****************************************************************************************************************************
# Function to clear the database table before inserting new data
#   clear the DB data from the config_data table
#*****************************************************************************************************************************   
def clear_db():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM config_data")
    connection.commit()
    connection.close()
#*******************************************************************************************************************************
# Initializing the Flask application 
app= Flask(__name__)

#*******************************************************************************************************************************
# Route to handle GET requests for reading the configuration file
#   1. Get the file path from the request arguments (default is 'config.ini')
#   2. Check if the file exists; if not, return an error message
#   3. Read the configuration file using the read_config_data function
#   4. Save the extracted data to the database using the save_to_db function
#   5. Read the data back from the database to verify if it was saved correctly
#   6. If successful, format the data and return it in HTML format
#*******************************************************************************************************************************
@app.route('/config', methods=['GET'])
def read_config_ini(): 

    file_path = request.args.get('file_path', 'config.ini')     # Default file path is set as config.ini, if not provided in the request
    
    #Check if the file exists, if not return error message
    if not os.path.exists(file_path):
        return (f"<html><h1 style='color:red'>ERROR:</h1> <h3>Configuration file '{file_path}' not found.</br> Kindly provide a valid file path.</h3></html>")
    else:
        print(f"Configuration file '{file_path}' found.")
    #****************************************************************************************************************************
    #Reading the configuration file using the function
    #If the error in readingfile , return error message
    #****************************************************************************************************************************
    try:
       config_details= read_config_data(file_path)                  # Read the configuration file using the function
    except Exception as e:
        return (f"<html><h1 style='color:red'>ERROR:</h1> <h3>OOPS!!!Error reading configuration file: {e}</h3></html>")
    #************************************************************************************************************************
    #data fetched from the config file is stored in the database
    #If the error in saving data to database, return error message  
    #***********************************************************************************************************************
    try:
        config_details = {f"{section}.{key}": value for section, section_data in config_details.items() for key, value in section_data.items()}
        save_to_db(config_details)        # Save the extracted data to the database
    except Exception as e:
        return (f"<html><h1 style='color:red'>ERROR:</h1> <h3>OOPS!!!Error saving data to database: {e}</h3></html>")
    #************************************************************************************************************************
    #Reading the data from the database to verify if the data is saved correctly
    #If the error in reading data from database, return error message
    #else return the formatted data in HTML format
    #***********************************************************************************************************************
    config_data_from_db = read_from_db()                # Read the data back from the database
    if not config_data_from_db:
        return (f"<html><h1 style='color:red'>ERROR:</h1> <h3>OOPS!!!Error reading data from database.</h3></html>")
    else:                                               #formatting the data from DB and returning the output in HTML format
        formatted_details = defaultdict(dict)
        for key, value in config_data_from_db:
            section, key = key.split('.', 1)
            formatted_details[section][key] = value

        output = "<html><body>Configuration File Parser Results:</br>"
        for section, section_data in formatted_details.items():
            output += f"<br/>{section.capitalize()}:</br>"
            for key, value in section_data.items():
                output += f" - {key}: {value}</br>"
        output += "</body></html>"
        return output

   
#*******************************************************************************************************************************
# Main function to run the Flask application
#******************************************************************************************************************************  
if __name__ == "__main__":
    
    app.run(debug=True,port=5000)                    # Run the Flask app on port 5000
    config = read_config_ini()                       # Call the function to read the config file , save data to DB and 
                                                     #function return the data read from DB in HTML format 
    
    