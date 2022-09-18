import { Header, CardField, PlayerList } from './game';
import { useSelector } from 'react-redux';
import { useEffect } from 'react';

const GameBase = () => {
  const { accessToken } = useSelector((state) => state.auth);
  const { roomID } = useSelector((state) => state.game);

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
