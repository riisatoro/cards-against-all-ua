import { Header, CardField, PlayerList } from './game';

const GameBase = () => {
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
