import json
from flask import Flask, render_template

import localsettings

app = Flask(__name__)
app.debug = localsettings.DEBUG


WEEKS = 2
f = open('api_payload.json')
API_DATA = json.load(f)

@app.route('/')
def index():
	return render_template('index.html', api_data=API_DATA)

def add_points(obj, mode='actualValue'):
	total = 0
	point_factors = {
		'assists': 1.5,
		'deaths': -0.5,
		'doubleKills': 0.0,
		'killOrAssistBonus': 2.0,
		'kills': 2.0,
		'minionKills': .01,
		'pentaKills': 5.0,
		'quadraKills': 3.0,
		'tripleKills': 2.0
	}
	for i in xrange(WEEKS):
		for k, v in obj[str(i+1)].iteritems():
			if k != 'week':
				total += v[mode] * point_factors[k]
	return total

@app.context_processor
def utility_processor():
	return dict(add_points=add_points)

@app.template_filter('get_team')
def get_team(player_obj):
	return API_DATA['proTeams'][str(player_obj['proTeamId'])]['shortName'] 

@app.template_filter('get_expr')
def get_expr(player_obj):
	player_team = API_DATA['proTeams'][str(player_obj['proTeamId'])]
	total_wins = 0
	total_losses = 0
	total_kills = 0
	total_assists = 0
	total_deaths = 0

	for i in xrange(WEEKS):
		total_wins += player_team['statsByWeek'][str(i+1)]['matchVictory']['actualValue']
		total_losses += player_team['statsByWeek'][str(i+1)]['matchDefeat']['actualValue']
		total_kills += player_obj['statsByWeek'][str(i+1)]['kills']['actualValue']
		total_assists += player_obj['statsByWeek'][str(i+1)]['assists']['actualValue']
		total_deaths += player_obj['statsByWeek'][str(i+1)]['deaths']['actualValue']

	KDA = (float(total_deaths) / (total_kills + total_assists)) + 1.0

	return round(((1.0 - float(total_wins) / (total_losses + total_wins)) * add_points(player_obj['statsByWeek'])) / KDA, 2)

@app.template_filter('get_winloss')
def get_winloss(player_obj):
	player_team = API_DATA['proTeams'][str(player_obj['proTeamId'])]
	total_wins = 0
	total_losses = 0

	for i in xrange(WEEKS):
		total_wins += player_team['statsByWeek'][str(i+1)]['matchVictory']['actualValue']
		total_losses += player_team['statsByWeek'][str(i+1)]['matchDefeat']['actualValue']

	return "{0}W - {1}L".format(total_wins, total_losses)

@app.context_processor
def inject_debug():
	return dict(debug=localsettings.DEBUG)

if __name__ == '__main__':
    app.run()
