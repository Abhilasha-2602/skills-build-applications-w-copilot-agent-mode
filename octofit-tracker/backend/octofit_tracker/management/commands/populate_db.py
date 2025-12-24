from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, LeaderboardEntry, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        with transaction.atomic():
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            LeaderboardEntry.objects.all().delete()
            UserProfile.objects.all().delete()
            Team.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Old data deleted. Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            UserProfile.objects.create(email='tony@stark.com', first_name='Tony', last_name='Stark', team=marvel),
            UserProfile.objects.create(email='steve@rogers.com', first_name='Steve', last_name='Rogers', team=marvel),
            UserProfile.objects.create(email='bruce@wayne.com', first_name='Bruce', last_name='Wayne', team=dc),
            UserProfile.objects.create(email='clark@kent.com', first_name='Clark', last_name='Kent', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], activity_type='Iron Man Suit Training', duration_minutes=60, distance_km=0)
        Activity.objects.create(user=users[1], activity_type='Shield Throwing', duration_minutes=45, distance_km=2)
        Activity.objects.create(user=users[2], activity_type='Batmobile Chase', duration_minutes=30, distance_km=10)
        Activity.objects.create(user=users[3], activity_type='Flight', duration_minutes=20, distance_km=50)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(user=users[0], name='Chest Day', description='Bench press and more', date='2025-12-24', duration_minutes=90)
        Workout.objects.create(user=users[2], name='Gadget Training', description='Batcave session', date='2025-12-23', duration_minutes=60)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        LeaderboardEntry.objects.create(user=users[0], points=100, rank=1)
        LeaderboardEntry.objects.create(user=users[1], points=80, rank=2)
        LeaderboardEntry.objects.create(user=users[2], points=120, rank=1)
        LeaderboardEntry.objects.create(user=users[3], points=90, rank=2)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
