from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(email='ironman@marvel.com', username='IronMan', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2024-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')
    def test_workout(self):
        self.assertEqual(self.workout.name, 'Pushups')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
