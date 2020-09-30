from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	league_list = League.objects.all()
	teams_list = Team.objects.all()
	player_list = Player.objects.all()
	context = {
		"asc": League.objects.get(name = "Atlantic Soccer Conference"),
		"bos_penguins": Team.objects.get(location = 'Boston', team_name = 'Penguins'),
		"icbc": League.objects.get(name="International Collegiate Baseball Conference"),
		"lopezes": Player.objects.filter(last_name="Lopez", curr_team.league.name == "American Conference of Amateur Football"),

		"leagues": league_list,
		
		"teams": teams_list,

		"players": player_list,
	}
	print(context['lopezes'])
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")