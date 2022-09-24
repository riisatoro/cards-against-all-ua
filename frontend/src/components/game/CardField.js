import { useSelector } from 'react-redux';
import Card from './Card';

const CardField = () => {
  const { username } = useSelector(state => state.auth);
  const { users } = useSelector(state => state.game.roomData);
  const { answer_cards: answerCards, cards } = users?.filter((user) => user.username === username)[0] || {};

  const { question_card: questionCard } = useSelector(state => state.game.roomData);
  const allowRequest = (questionCard.answers_amount - (answerCards?.length || 0)) > 0;

  return (
    <div className="container my-3">
      <div className="d-flex justify-content-evenly align-items-center">
        {questionCard?.id && <Card {...{ ...questionCard, allowRequest: false }} />}
        <div>
          {answerCards[0]?.id && <p className="h2">&amp;</p>}
        </div>
        {answerCards?.map((card) => <Card {...{ ...card, className: 'card-selected', allowRequest: false }} key={card.id} />)}
      </div>
      <div className="d-flex my-3 flex-wrap justify-content-between">
        {cards?.map((card) => <Card {...{ ...card, allowRequest }} key={card.id} />)}
      </div>
    </div>
  )
}

export default CardField;
