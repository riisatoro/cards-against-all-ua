import { useDispatch } from 'react-redux';
import { selectAnswerCard } from '../../store/reducers/apiRequests';

import '../../styles/card.css';

const Card = ({ id, text, card_type: cardType, className, allowRequest }) => {

  const dispatch = useDispatch();
  const selectCard = () => {
    if (allowRequest) dispatch(selectAnswerCard({ card_id: id }));
  }

  return (
    <div className={`card card-${cardType} my-2 ${className || ''}`} onClick={selectCard}>
      <div className="card-body">
        <p className="card-text text-center">{text}</p>
      </div>
    </div>
  )
}

export default Card;