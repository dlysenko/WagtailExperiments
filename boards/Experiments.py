from django.urls import resolve
from django.core.urlresolvers import reverse

url = reverse('board_topics', kwargs={'pk': 1})
print(url)