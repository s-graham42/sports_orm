from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	league_list = League.objects.all()
	teams_list = Team.objects.all()
	player_list = Player.objects.all()
	context = {
		"baseball_leagues": league_list.filter(sport = "Baseball"),
		"womens_leagues": league_list.filter(name__icontains = "women"),
		"hockey_leagues": league_list.filter(sport__icontains = "hockey"),
		"non_football": league_list.exclude(sport = "Football"),
		"conferences": league_list.filter(name__icontains = "conference"),
		"atlantic_leagues": league_list.filter(name__icontains = "atlantic"),
		"leagues": league_list,
		"dallas_teams": teams_list.filter(location = "Dallas"),
		"raptors": teams_list.filter(team_name = "Raptors"),
		"city_teams": teams_list.filter(location__icontains = "city"),
		"t_teams": teams_list.filter(team_name__startswith = "T"),
		"location_order": teams_list.order_by("location"),
		"rev_name_order": teams_list.order_by("-team_name"),
		"teams": teams_list,
		"players": player_list,
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")