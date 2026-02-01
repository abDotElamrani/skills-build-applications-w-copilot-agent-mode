from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-02-01')
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, date='2026-02-01')
        Activity.objects.create(user=batman, type='Swimming', duration=60, date='2026-02-01')
        Activity.objects.create(user=superman, type='Yoga', duration=20, date='2026-02-01')

        # Create workouts
        cardio = Workout.objects.create(name='Cardio', description='Cardio session')
        strength = Workout.objects.create(name='Strength', description='Strength training')
        cardio.suggested_for.add(ironman, batman)
        strength.suggested_for.add(spiderman, superman)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
