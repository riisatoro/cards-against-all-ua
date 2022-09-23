import { useSelector } from 'react-redux';

const PlayerList = () => {
  const { roomData: { users } } = useSelector((state) => state.game)
  const { username } = useSelector((state) => state.auth);
  
  return (
    <div>
      <p>Players</p>
      <div>
        {
          users?.map((item) => (
            <p key={item.username}>{item.username === username ? "You: " : "Player: "} {item.username} | {item.score  }</p>
          ))
        }
      </div>
    </div>
  )
}

export default PlayerList;
