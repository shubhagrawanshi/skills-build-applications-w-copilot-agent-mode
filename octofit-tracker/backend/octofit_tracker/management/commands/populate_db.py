from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data for each model separately to avoid FK/cascade issues
        for model in [Leaderboard, Activity, Workout, User, Team]:
            for obj in model.objects.all():
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=date(2025, 12, 25))
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date(2025, 12, 24))
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=date(2025, 12, 23))
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=date(2025, 12, 22))

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength training for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
