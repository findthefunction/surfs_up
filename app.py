# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import psycopg2

# Set up engine to access database and reflect tables

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

# Save references to tables

Measurement = Base.classes.measurement
Station = Base.classes.station 

# Create a session link from Python to database

session = Session(engine)

# Create new Flask intance

app = Flask(__name__)

# Create first route. (The forward slash denote the root of routes)

@app.route('/')

# Create function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/temp/start/end
    ''')
    
# Second route

@app.route("/api/v1.0/precipitation")

# Create precipitation() function

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp)\
    .filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# stations route

@app.route("/api/v1.0/stations")

# Create stations() function

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# tobs route

@app.route("/api/v1.0/tobs")

# Create temp_monthly function

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs)\
        .filter(Measurement.station == 'USC00519281')\
            .filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))    
    return jsonify(temps=temps)

# start / end routes

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create stats function

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel)\
            .filter(Measurement.date >= start)\
                .filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel)\
        .filter(Measurement.date >= start)\
            .filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

                