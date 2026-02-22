from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.set([ironman, batman])
        running.suggested_for.set([captain, superman])

        # Create activities
        Activity.objects.create(user=ironman, type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Running', duration=45, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=200, rank=1)
        Leaderboard.objects.create(user=batman, score=180, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
