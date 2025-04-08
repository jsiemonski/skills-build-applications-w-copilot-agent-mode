from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        # Manually add members to the team
        team1.members.set([user1, user2])  # Use .set() instead of .add()

        # Create test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30)
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session to start the day.")
        Workout.objects.create(name="HIIT", description="High-intensity interval training for fat burning.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))