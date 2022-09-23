import { useSelector, useDispatch } from "react-redux";
import { Navigate } from 'react-router-dom';
import { Navigation } from "../../constants";
import { userLeaveRoom } from '../../store/reducers/apiRequests';
import RoomLinkButton from "./RoomLinkButton";


const Header = () => {
  const dispatch = useDispatch();

  const {
    roomID,
    roomData
  } = useSelector((state) => state.game);

  return (
    <div className="d-flex align-items-center justify-content-evenly">
      {!roomID && <Navigate to={Navigation.profile} />}

      {!roomData?.is_started && (
        <p className="mb-0">Waiting for other players to join...</p>
      )}
      
      {roomData?.is_started && !roomData?.question_card?.id && (
        <p className="mb-0">Game will be starting soon...</p>
      )}

      <div className="text-end"><RoomLinkButton {...{ roomID }} /></div>
      <button className="btn btn-outline-danger" onClick={() => dispatch(userLeaveRoom({ room_id: roomID }))}>LeaveRoom</button>
    </div>
  )
}

export default Header;
