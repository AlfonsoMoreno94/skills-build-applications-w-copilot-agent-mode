from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data (delete individually for Djongo compatibility)
        for obj in User.objects.filter(id__isnull=False):
            obj.delete()
        for obj in Team.objects.filter(id__isnull=False):
            obj.delete()
        for obj in Activity.objects.filter(id__isnull=False):
            obj.delete()
        for obj in Leaderboard.objects.filter(id__isnull=False):
            obj.delete()
        for obj in Workout.objects.filter(id__isnull=False):
            obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30),
            Activity.objects.create(user=users[1], type='cycle', duration=45),
            Activity.objects.create(user=users[2], type='swim', duration=60),
            Activity.objects.create(user=users[3], type='walk', duration=20),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout'),
            Workout.objects.create(name='Strength Training', description='Full body strength routine'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
