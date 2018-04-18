from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)
from sqlalchemy import create_engine, func , inspect, desc
engine = create_engine('sqlite:///hawaii.sqlite')

from sqlalchemy.ext.automap import automap_base
Base = automap_base()
Base.prepare(engine, reflect=True)
from sqlalchemy.orm import Session

session=Session(bind=engine)
Station = Base.classes.stations
Measurement = Base.classes.measurements
@app.route("/")
def welcome():
    return ("<h1>Hawaii Surf's Up API!</h1>" 
            "<i>Make sure your start and end dates are formatted (Year-Month-Day)</i>"
            "<h2>Available Routes</h2>" 
            "<li><a href ='/api/v1.0/precipitation'>precipitation</a></li>"
            "<li><a href ='/api/v1.0/stations'>stations</a></li>"
            "<li><a href ='/api/v1.0/tobs'>tobs</a></li>"
#            "<li><a href ='/api/v1.0/<date>'>date</a></li>>"
            "<li><a href = '/api/v1.0/calc_temps/<start>/<end>'>Calc Temps</a></li>");
#            "<li><a href ='/api/v1.0/query_dates'>query_datse</a></li>");
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date <= "2016-01-01", Measurement.date >= "2016-01-01").\
        all()

    precipitation_list = [results]

    return jsonify(precipitation_list)
@app.route('/api/v1.0/stations')
def stations():
 results = session.query(Station.name, Station.station, Station.elevation).all()

    
 station_list = []
 for result in results:
        row = {}
        row['name'] = result[0]
        row['station'] = result[1]
        row['elevation'] = result[2]
        station_list.append(row)
 return jsonify(station_list)
@app.route("/api/v1.0/tobs")
def temp_obs():
    
 results = session.query(Station.name, Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-01-01", Measurement.date <= "2017-01-01").\
        all()

    
 tobs_list = []
 for result in results:
        row = {}
        row["Date"] = result[1]
        row["Station"] = result[0]
        row["Temperature"] = int(result[2])
        tobs_list.append(row)

 return jsonify(tobs_list)
@app.route('/api/v1.0/<date>/')
def given_date(date):
 results = session.query(Measurement.date, func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
        filter(Measurement.date == date).all()


 data_list = []
 for result in results:
        row = {}
        row['Date'] = result[0]
        row['Average Temperature'] = str(result[1])
        row['Highest Temperature'] = str(result[2])
        row['Lowest Temperature'] = str(result[3])
        data_list.append(row)
 return jsonify(data_list)
@app.route("/api/v1.0/calc_temps/<start>")

def calc_temps(start='start_date'):
    start_date = datetime.strptime('2016-08-01', '%Y-%m-%d').date()
    start_results = session.query(func.max(Measurement.tobs), \
                            func.min(Measurement.tobs),\
                            func.avg(Measurement.tobs)).\
                            filter(Measurement.date >= start_date) 
    
    start_tobs = []
    for tobs in start_results:
        tobs_dict = {}
        tobs_dict["TAVG"] = float(tobs[2])
        tobs_dict["TMAX"] = float(tobs[0])
        tobs_dict["TMIN"] = float(tobs[1])
        
        start_tobs.append(tobs_dict)

    return jsonify(start_tobs)
@app.route("/api/v1.0/calc_temps/<start>/<end>")

def calc_temps_2(start='start_date', end='end_date'):      
    start_date = datetime.strptime('2016-01-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2017-01-01', '%Y-%m-%d').date()

    start_end_results=session.query(func.max(Measurement.tobs).label("max_tobs"), \
                      func.min(Measurement.tobs).label("min_tobs"),\
                      func.avg(Measurement.tobs).label("avg_tobs")).\
                      filter(Measurement.date.between(start_date , end_date))   

    start_end_tobs = []
    for tobs in start_end_results:
        tobs_dict = {}
        tobs_dict["TAVG"] = float(tobs[2])
        tobs_dict["TMAX"] = float(tobs[0])
        tobs_dict["TMIN"] = float(tobs[1])

        start_end_tobs.append(tobs_dict)
    
    return jsonify(start_end_tobs)

if __name__ == '__main__':
#    app.run(debug=True, use_reloader=False)
    app.run()
