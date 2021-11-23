#Imports

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#Database Set-up

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

#Set up Flask
app = Flask(__name__)


#Create Flask Routes

#Homepage - List all routes that are available
@app.route("/")
def welcome():
    return (
        f"Here are all the routes that are available:<br/>"
        f"Precipitation data:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"List of stations:<br/>"
        f"/api/v1.0/stations<br/>"
        f"Dates and temperatures from our most active station from this year:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Min., avg., and max. temperatures for all dates greater and equal to a given date:<br/>"
        f"/api/v1.0/<start><br/>"
        f"Min., avg., and max. temperatures for all dates in between two given dates:<br/>"
        f"/api/v1.0/<start>/<end>"

@app.route("/api/v1.0/precipitation/")
def precripitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
 
    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

	"""Convert the query results to a dictionary using date as the key and prcp as the value"""
	"""Return a list of date and pcrp"""
	date_prcp_recepticle = []
	for date, prcp in results:
		date_prcp_dictionary = {}
		date_prcp_dictionary['date'] = date
		date_prcp_dictionary['prcp'] = prcp
		date_prcp_recepticle.append(date_prcp_dictionary)

	return jsonify(date_prcp_recepticle)



@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset."""
    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Return all

    return jsonify(results)


@app.route("/api/v1.0/tobs/")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
     """Return a JSON list of temps and dates from the dataset."""
    # Query all dates
   	results = session.query(Measurement.date, Measurement.tobs).\
   		filter(Measurement.date >= '2016-08-23').order_by(Measurement.date).all()

	return jsonify(results)


	@app.route("/api/v1.0/<start>")
def starting(start):
	# Create our session (link) from Python to the DB
    session = Session(engine)

     # Query all dates
   """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start"""
   	results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
   		filter(Measurement.date >= '2010-01-01').all()   

tobs_min = func.min(Measurement.tobs)
tobs_max = func.max(Measurement.tobs)
tobs_avg = func.avg(Measurement.tobs)

   	tobs_recepticle = []
	for result in results:
		tobs_dictionary = {}
		tobs_dictionary[tobs_min] = date
		tobs_dictionary[tobs_max] = prcp
		tobs_dictionary[tobs_avg] = prcp
		tobs_recepticle.append(tobs_dictionary)

	return jsonify(start, tobs_recepticle)	



	@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
	# Create our session (link) from Python to the DB
    session = Session(engine)

     # Query all dates
     """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range"""
   	results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
   		filter(Measurement.date >= '2010-01-01').\
   		filter(Measurement.date <= '2017-08-23').all()   

tobs_min = func.min(Measurement.tobs)
tobs_max = func.max(Measurement.tobs)
tobs_avg = func.avg(Measurement.tobs)

   	tobs_recepticle = []
	for result in results:
		tobs_dictionary = {}
		tobs_dictionary[tobs_min] = date
		tobs_dictionary[tobs_max] = prcp
		tobs_dictionary[tobs_avg] = prcp
		tobs_recepticle.append(tobs_dictionary)

	return jsonify(start, end, tobs_recepticle)	

 






