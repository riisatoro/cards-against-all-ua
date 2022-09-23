import { useSelector } from 'react-redux';
import Card from './Card';

const CardField = () => {
  const { username } = useSelector(state => state.auth);
  const { users } = useSelector(state => state.game.roomData);
  const { answer_cards: answerCards, cards } = users.filter((user) => user.username === username)[0];

  const { question_card: questionCard } = useSelector(state => state.game.roomData);

  return (
    <div className="container my-3">
      <div className="d-flex justify-content-between">
        <Card {...questionCard} />
        {answerCards?.map((card) => <Card {...card} key={card.id} />)}
      </div>
      <div className="d-flex my-3 flex-wrap justify-content-between">
        {cards?.map((card) => <Card {...card} key={card.id}/>)}
      </div>
    </div>
  )
}

export default CardField;
