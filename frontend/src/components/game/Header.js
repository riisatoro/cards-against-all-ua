import { useSelector, useDispatch } from "react-redux";
import { Navigate } from 'react-router-dom';
import { Navigation } from "../../constants";
import { userLeaveRoom } from '../../store/reducers/apiRequests';
import RoomLinkButton from "./RoomLinkButton";


const Header = () => {
  const dispatch = useDispatch();

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
      {!id && <Navigate to={Navigation.profile} />}

      {!isStarted && (
        <p className="mb-0">Waiting for other players to join...</p>
      )}

      {isStarted && (
        <div>
          <p><small>Current leader: {leader?.user?.username}</small></p>
        </div>
      )}

      <div className="text-end"><RoomLinkButton {...{ roomID: id }} /></div>
      <button className="btn btn-outline-danger" onClick={() => dispatch(userLeaveRoom({ room_id: id }))}>LeaveRoom</button>
    </div>
  )
}

export default Header;
