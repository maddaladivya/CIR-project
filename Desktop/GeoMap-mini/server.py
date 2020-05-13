import flask
from flask import request, url_for, render_template, redirect

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_CONFIG_FILE', silent=True)

MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

@app.route('/', methods=['GET','POST'])
def map_main():
  return render_template('new.html',
    mapbox_access_token=MAPBOX_ACCESS_KEY)

@app.route('/test', methods=['GET','POST'])
def test():
  if flask.request.method == 'POST':
    select = flask.request.form.get('layer_type')
    cluster_select = flask.request.form.get('cluster_layer_type')
    if(select=='2'):
      return flask.render_template('k2_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)      
    elif(select=='3'):
      return flask.render_template('k3_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(select=='4'):
      return flask.render_template('k4_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(select=='5'):
      return flask.render_template('k5_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)

    if(cluster_select=='1'):
        return flask.render_template('k2_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='2'):
        return flask.render_template('k2_c2.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='3'):
        return flask.render_template('k3_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='4'):
        return flask.render_template('k3_c2.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='5'):
        return flask.render_template('k3_c3.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='6'):
        return flask.render_template('k4_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='7'):
        return flask.render_template('k4_c2.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='8'):
        return flask.render_template('k4_c3.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='9'):
        return flask.render_template('k4_c4.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='10'):
        return flask.render_template('k5_c1.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='11'):
        return flask.render_template('k5_c2.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='12'):
        return flask.render_template('k5_c3.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='13'):
        return flask.render_template('k5_c4.html', mapbox_access_token=MAPBOX_ACCESS_KEY)
    elif(cluster_select=='14'):
        return flask.render_template('k5_c5.html', mapbox_access_token=MAPBOX_ACCESS_KEY)

if __name__ == '__main__':
  app.run(debug=True)
