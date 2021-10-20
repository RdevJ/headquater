from app.schemas.article import Article

fake_data = {
    'first-article': Article(
        title='First Article',
        title_slug='first-article',
        content='Content of the amazing article'
    ),
    'second-article': Article(
        title='Second Article',
        title_slug='second-article',
        content='Poor writer'
    )
}


class ArticleQuery(object):
    def __init__(self, article_slug):
        self.article_slug = article_slug

    def get_article(self):
        return fake_data.get(self.article_slug, None)
