const socket = new WebSocket(`ws://${process.env.REACT_APP_PROXY}/game/`)

const connectSocket = () => {
  socket.onopen = (e) => {
    console.log('open', e)
  }

  socket.onmessage = (e) => {
    console.log('message', e);
  }

  socket.onerror = (e) => {
    console.log('error', e);
  }

  socket.onclose = (e) => {
    console.log('closed', e);
  }
}

export { connectSocket, socket };
