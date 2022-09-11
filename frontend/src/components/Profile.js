import { useEffect } from 'react';
import { useDispatch, useState, useSelector } from 'react-redux';
import { fetchAvailableGames } from '../store/reducers/apiRequests';
import { FETCH_GAME_LIST_TIMEOUT } from '../constants';

const Profile = () => {
    const dispatch = useDispatch();

    useEffect(() => {
        setInterval(
            () => dispatch(fetchAvailableGames()),
            FETCH_GAME_LIST_TIMEOUT,
        )
    }, [])

    return (
        <div className="container">
            <div className="row">
                <div className="col col-sm-12 col-lg-6">
                    Profile status
                </div>
                <div className="col col-sm-12 col-lg-6">
                    Game list
                </div>
            </div>
        </div>
    )
}

export default Profile;
