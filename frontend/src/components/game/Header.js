import { useState } from 'react';
import { useSelector } from "react-redux"

const RoomLinkButton = ({ roomID }) => {
  const [isCopied, setIsCopied] = useState(false);

  const copyLinkToClipboard = () => {
    const url = window.location.href + roomID + '/';
    navigator.clipboard.writeText(url);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 1000);
  }

  return (
    <button className="btn btn-outline-primary" style={{minWidth: '128px'}} onClick={copyLinkToClipboard}>
      <small>{isCopied ? 'Copied!' : 'Copy room URL'}</small>
    </button>
  )
}

const Header = () => {
  const {
    currentGame: {
      id,
      leader,
      round_number: roundNumber,
      round_end_time: roundEndTime,
      is_started: isStarted,
    } } = useSelector((state) => state.game);



  return (
    <div className="d-flex align-items-center justify-content-evenly">
      {!isStarted && (
        <>
          <p className="mb-0">Waiting for other players to join...</p>
          <div className="text-end"><RoomLinkButton {...{ roomID: id }} /></div>
        </>
      )}

      {isStarted && (
        <>
          <div>
            <p><small>Current leader:</small></p>
          </div>
          <div className="text-end"><RoomLinkButton {...{ roomID: id }} /></div>
        </>
      )}
    </div>
  )
}

export default Header;
