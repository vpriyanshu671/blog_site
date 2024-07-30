import markdown
from .models import Post
from django.urls import reverse_lazy
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html


class LatestPostsFeed(Feed):
    title = 'WanderWrite'
    link = reverse_lazy('WanderWrite:post_list')
    description = 'New posts of my WanderWrite.'
    def items(self):
        return Post.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)
    def item_pubdate(self, item):
        return item.publish

