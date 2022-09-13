import { useState } from 'react';

const RoomLinkButton = ({ roomID }) => {
  const [isCopied, setIsCopied] = useState(false);

  const copyLinkToClipboard = () => {
    const url = window.location.href + roomID + '/';
    navigator.clipboard.writeText(url);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 1000);
  }

  return (
    <button className="btn btn-outline-primary" style={{ minWidth: '128px' }} onClick={copyLinkToClipboard}>
      <small>{isCopied ? 'Copied!' : 'Copy room URL'}</small>
    </button>
  )
}

export default RoomLinkButton;