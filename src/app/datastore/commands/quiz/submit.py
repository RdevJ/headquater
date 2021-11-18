from datetime import date
from typing import List, Optional

from app.models.answer import Answer
from app.models.question import Question
from app.models.statistics import Statistics
from app.schemas.quiz import QuizSubmitBase
from sqlalchemy import select
from sqlalchemy.orm.session import Session


class SubmitAnswerCommand(object):
    def __init__(self, payload: QuizSubmitBase, db: Session) -> None:
        self.payload = payload
        self.db = db

    def submit_answer(self) -> None:
        correct_answers = self._get_correct_answers(question_id=self.payload.question_id)

        are_answers_correct = self._verify_answers(answers=correct_answers)

        if are_answers_correct:
            self._update_statistics()

    def _get_correct_answers(self, question_id: int) -> List[int]:
        return [row[0] for row in self.db.execute(
            select(Answer.id).
            join(Question.answers).
            where(Answer.is_correct == True, Question.id == question_id)
        )]

    def _verify_answers(self, answers: List[int]) -> bool:
        return set(answers).issubset(self.payload.answers)

    def _update_statistics(self) -> None:
        questions_number = self._get_all_questions_for_article()
        statistics = self._get_statistics_for_article()
        statistics.knowledge_level = self._calculate_knowledge_level(
            old_knowledge_level=statistics.knowledge_level,
            questions_number=questions_number,
        )
        self.db.commit()

    def _get_all_questions_for_article(self) -> int:
        return (
            self.db.query(Question).
            filter(Question.article_id == self.payload.article_id).
            count()
        )

    def _get_statistics_for_article(self) -> Optional[Statistics]:
        return (
            self.db.query(Statistics).
            filter(Statistics.article_id == self.payload.article_id).
            first()
        )

    def _calculate_knowledge_level(self, old_knowledge_level, questions_number) -> float:
        increment_value = (1.0 - old_knowledge_level) / questions_number
        return min(old_knowledge_level + increment_value, 1.0)
