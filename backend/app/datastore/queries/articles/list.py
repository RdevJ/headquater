from app.schemas.article import Article
from app.schemas.tags import Tag


class ArticlesQuery(object):
    def get_articles(self):
        return [
            Article(
                title='First Article',
                title_slug='first-article',
                content='Content of the amazing article',
                tags=[
                    Tag(label='Star'),
                    Tag(label='Top10'),
                ],
            ),
            Article(
                title='Second Article',
                title_slug='second-article',
                content='Poor writer',
                tags=[]
            )
        ]
