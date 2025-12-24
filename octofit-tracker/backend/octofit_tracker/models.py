from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='members')

    def __str__(self):
        return self.email


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.FloatField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity_type} @ {self.timestamp}"


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return f"{self.user.email}: {self.points} points"


class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration_minutes = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.email})"
