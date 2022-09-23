import '../../styles/card.css';

const Card = ({ id, text, card_type: cardType }) => {
  
  const selectCard = () => {
    console.log('card selected');
  }

  return (
    <div className={`card card-${cardType} my-2`} onClick={selectCard}>
      <div className="card-body">
        <p className="card-text text-center">{text}</p>
      </div>
    </div>
  )
}

export default Card;