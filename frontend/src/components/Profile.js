import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUserRoomData, createUserRoom, joinUserRoom, userLeaveRoom } from '../store/reducers/apiRequests';
import { Navigate, Link } from 'react-router-dom';
import { Navigation } from '../constants';

const Profile = () => {
  const dispatch = useDispatch();
  const { roomID } = useSelector((state) => state.game);

  const createRoom = () => {
    dispatch(createUserRoom());
  };

  const joinRoom = () => {
    dispatch(joinUserRoom());
  }

  useEffect(() => {
    dispatch(fetchUserRoomData());
  }, [dispatch])

  return (
    <div className="container">
      {roomID && <Navigate to={Navigation.game} />}
      <div className="row">
        <div className="col col-sm-12 col-lg-6">
          Profile status
        </div>
        <div className="d-flex justify-content-evenly mb-4">
          <button className="btn btn-outline-primary" onClick={createRoom}>New room</button>
          <button className="btn btn-outline-success" onClick={joinRoom}>Join room</button>
        </div>

        <div className="d-flex justify-content-between">
          <input type="text" name="room_id" placeholder="Enter room id" className="form-control w-75" />
          <button className="btn btn-outline-warning">Join private room</button>
        </div>
      </div>
    </div>
  )
}

export default Profile;
