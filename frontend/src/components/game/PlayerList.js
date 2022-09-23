import { useSelector } from 'react-redux';

const PlayerList = () => {
  const { roomData: { users } } = useSelector((state) => state.game)

  return (
    <div>
      <p>Players</p>
      <div>
        {
          users?.map((item) => (
            <p key={item.username}><small>{item.username.substring(0, 20)} | {item.score}</small></p>
          ))
        }
      </div>
    </div>
  )
}

export default PlayerList;
