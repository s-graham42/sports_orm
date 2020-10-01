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
		"acaf": League.objects.get(name = "American Conference of Amateur Football"),
		"football_leagues": League.objects.filter(sport = "Football"),
		"teams_with_sophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"leagues_with_sophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"floreses_not_roughriders": Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington", curr_team__team_name="Roughriders"),
		"sam_evans_teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),

		"leagues": league_list,
		"teams": teams_list,
		"players": player_list,
	}
	#print(context['leagues_with_sophia'])
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")