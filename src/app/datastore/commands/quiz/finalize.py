from datetime import date, datetime, timedelta
from typing import Optional

from app.models.statistics import Statistics
from app.schemas.quiz import QuizFinalize
from sqlalchemy.orm.session import Session


class FinalizeCommand(object):
    def __init__(self, payload: QuizFinalize, db: Session):
        self.payload = payload
        self.db = db

    def finalize(self):
        statistics = self._get_statistics()
        if statistics:
            next_repetition = self._calculate_repetition(statistics=statistics)
            self._update_statistics(statistics=statistics, next_repetition=next_repetition)

    def _calculate_repetition(self, statistics: Statistics) -> date:
        repetitions = statistics.repetitions
        days = 2 ** repetitions
        next_repetition_datetime = datetime.now() + timedelta(days=days)
        return next_repetition_datetime.date()

    def _update_statistics(self, statistics: Statistics, next_repetition: date) -> None:
        statistics.repetitions += 1
        statistics.next_repetition = next_repetition
        statistics.last_viewed = datetime.now().date()
        self.db.commit()

    def _get_statistics(self) -> Optional[Statistics]:
        return self.db.query(Statistics).filter(Statistics.article_id == self.payload.article_id).first()
