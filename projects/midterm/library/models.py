from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

class Genre(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a media topic")
	def __str__(self):
		return self.name

class Media(models.Model):
	title = models.CharField(max_length=200)
	isbn = models.CharField('ISBN', max_length=13, help_text="13 character ISBN number", blank=True)
	topic = models.ManyToOneField(Genre, help_text="Select a topic for this book")
	subtopic = models.ManyToManyField(Genre, help_text="Select the subtopics for this book")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('media-detail', args=[str(self.id)])

class MediaInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this media")
	media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)
	due_date = models.DateField(null=True, blank=True)
	rental_history = models.OneToManyField(UserProfile, help_text="Select the past renters")
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


	AVAILABILITY = (
		('a', 'Available'),
		('o', 'On Loan'),
	)

	status = models.CharField(max_length=1, choices=AVAILABILITY, blank=True, default='a', help_text="Media availability")

	class Meta:
		ordering = ["due_date"]

	def __str__(self):
		return '%s (%s)' % (self.id, self.book.title)

class UserProfile(models.model):
	user = models.OneToOneField(User)
	rentals = models.OneToManyField(MediaInstance, help_text="Select the currently rented books")