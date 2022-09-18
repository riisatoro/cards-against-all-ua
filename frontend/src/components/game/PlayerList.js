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
            <p key={item.user.username}>{item.user.username === username ? "You: " : "Player: "} {item.user.username} | {item.score  }</p>
          ))
        }
      </div>
    </div>
  )
}

export default PlayerList;
