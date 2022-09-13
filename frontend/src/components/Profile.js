import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUserRoomData, joinUserToRoom, userLeaveRoom } from '../store/reducers/apiRequests';
import { Navigate, Link } from 'react-router-dom';
import { Navigation } from '../constants';

const Profile = () => {
  const dispatch = useDispatch();
  const [redirect, setRedirect] = useState(false);

  const { currentGame: { id } } = useSelector((state) => state.game);

  const createRoom = () => {
    dispatch(joinUserToRoom());
    setRedirect(true)
  };

  const leaveRoom = () => {
    dispatch(userLeaveRoom({ room_uuid: id }))
  }

  useEffect(() => {
    dispatch(fetchUserRoomData());
  }, [dispatch])

  return (
    <div className="container">
      {redirect && id && <Navigate to={Navigation.game} />}
      <div className="row">
        <div className="col col-sm-12 col-lg-6">
          Profile status
        </div>
        <div className="col col-sm-12 col-lg-6">
          {
            id
            && (
              <div className="my-4 alert alert-warning">
                <p className="text-center"><b>You have unfinished game</b></p>
                <div className="d-flex justify-content-evenly">
                  <Link className="btn btn-outline-success" to={Navigation.game}>Continue playing</Link>
                  <button className="btn btn-outline-danger" onClick={leaveRoom}>Leave room</button>
                </div>
              </div>
            )
          }

          {!id
            && (
              <>
                <div className="d-flex justify-content-evenly mb-4">
                  <button className="btn btn-outline-primary" onClick={createRoom}>New room</button>
                  <button className="btn btn-outline-success">Join room</button>
                </div>

                <div className="d-flex justify-content-between">
                  <input type="text" name="room_id" placeholder="Enter room id" className="form-control w-75" />
                  <button className="btn btn-outline-warning">Join private room</button>
                </div>
              </>
            )}
        </div>
      </div>
    </div>
  )
}

export default Profile;
