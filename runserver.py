import json
from flask import Flask, render_template

import localsettings

app = Flask(__name__)
app.debug = localsettings.DEBUG

@app.route('/')
def index():
	f = open('api_payload.json')
	json_data = json.load(f)
	return render_template('index.html', api_data=json_data)

@app.context_processor
def utility_processor():
	def add_points(obj, mode='actualValue'):
		weeks = 1
		total = 0
		point_factors = {
			'assists': 1.5,
			'deaths': -0.5,
			'doubleKills': 0.0,
			'killOrAssistBonus': 2,
			'kills': 2,
			'minionKills': .01,
			'pentaKills': 10,
			'quadraKills': 5,
			'tripleKills': 2
		}
		for i in xrange(weeks):
			for k, v in obj[str(i+1)].iteritems():
				if k != 'week':
					total += v[mode] * point_factors[k]
		return total
	return dict(add_points=add_points)

if __name__ == '__main__':
    app.run()
