from django.contrib import admin
from .models import Team, UserProfile, Activity, LeaderboardEntry, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'team')
    search_fields = ('email', 'first_name', 'last_name')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'timestamp')
    list_filter = ('activity_type',)


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'rank')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date')
