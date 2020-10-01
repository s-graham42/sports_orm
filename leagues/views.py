from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

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
		"all_time_tigerCats": Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats"),
		"past_vikings": Player.objects.filter(all_teams__location="Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings"),
		"jacobs_old_teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),
		"joshuas_in_afabp": Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players", first_name="Joshua"),
		"twelve_player_teams": Team.objects.annotate(num_players = Count('all_players')).filter(num_players__gte = 12),
		"players_by_num_teams": Player.objects.annotate(num_teams = Count('all_teams')).order_by('num_teams'),
		"leagues": league_list,
		"teams": teams_list,
		"players": player_list,
	}
	# print(context['twelve_player_teams'])
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")