import React, { createContext, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateGameData } from '../store/reducers/gameReducer';

const WebsocketContext = createContext(null);

export default ({ children }) => {
  let socket = null;

  const dispatch = useDispatch();
  const { roomID } = useSelector((state) => state.game)

  useEffect(() => {
    if (roomID) {
      socket = new WebSocket(`ws://${process.env.REACT_APP_PROXY}/game/${roomID}/`);
      socket.onmessage  = (e) => dispatch(updateGameData(JSON.parse(e.data)))
    } else {
      socket = null;
    }
  }, [roomID])

  return (
    <WebsocketContext.Provider value={socket}>
      {children}
    </WebsocketContext.Provider>
  )
}