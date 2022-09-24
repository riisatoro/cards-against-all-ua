import { useSelector } from 'react-redux';
import Card from './Card';

const CardField = () => {
  const { username } = useSelector(state => state.auth);
  const { users, leader } = useSelector(state => state.game.roomData);
  const isLeader = leader.username === username;

  const { answer_cards: answerCards, cards } = users?.filter((user) => user.username === username)[0] || {};
  const suggestedCards = users?.filter((user) => user.username !== username).map((item) => item.answer_cards)

  const { question_card: questionCard } = useSelector(state => state.game.roomData);
  const allowRequest = (questionCard.answers_amount - (answerCards?.length || 0)) > 0;

  const selectBestAnswer = () => {  };

  return (
    <div className="container my-3">
      <div className="d-flex justify-content-evenly align-items-center">
        {questionCard?.id && <Card {...{ ...questionCard, allowRequest: false }} />}
        <div>
          {!isLeader && answerCards[0]?.id && <p className="h2">&amp;</p>}
        </div>
        {!isLeader && answerCards?.map((card) => <Card {...{ ...card, className: 'card-selected', allowRequest: false }} key={card.id} />)}
      </div>
      <div className="d-flex my-3 flex-wrap justify-content-between">
        {!isLeader && cards?.map((card) => <Card {...{ ...card, allowRequest }} key={card.id} />)}
      </div>
      <div className="my-3">
        {isLeader && suggestedCards.map((userCard, index) => (
          <div key={`user-block-${index}`} className="user-card-block d-flex" onClick={selectBestAnswer}>
            {userCard.map((card) => (
              <div key={card.id} className="mx-1"><Card {...card} /></div>
            ))}
          </div>
        ))}
      </div>
    </div>
  )
}

export default CardField;
