import { Header, CardField, PlayerList } from './game';
import { connectSocket } from '../socket';
import { useSelector } from 'react-redux';

const GameBase = () => {
  const { accessToken } = useSelector((state) => state.auth);
  const { currentGame: { id } } = useSelector((state) => state.game);
  if (accessToken && id) connectSocket(id, accessToken);

  return (
    <div className="container">
      <Header />
      <div className="row">
        <div className="col col-4">
          <PlayerList />
        </div>
        <div className="col col-8">
          <CardField />
        </div>
      </div>
    </div>
  )
}

export default GameBase;
