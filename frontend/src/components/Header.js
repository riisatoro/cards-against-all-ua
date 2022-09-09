import { useSelector, useDispatch } from 'react-redux';
import Navigation from '../constants/navigation';
import { setLocation } from '../store/reducers/navigationReducer';

function Header() {
    const dispatch = useDispatch();
    const { accessToken } = useSelector((state) => state.auth);
    const { location } = useSelector((state) => state.navigation);
    const username = 'Anon';
    const buttonText = location === Navigation.registration.name ? 'Login' : 'Registration';

    const switchAuthPage = () => {
        location === Navigation.registration.name
            ? dispatch(setLocation({ location: Navigation.login.name }))
            : dispatch(setLocation({ location: Navigation.registration.name }))
    }

    return (
        <div className="container-fluid">
            {
                accessToken
                    ? <p>Welcome, {username}</p>
                    : <button className="btn btn-primary" onClick={switchAuthPage}>{buttonText}</button>
            }
        </div>
    )
}

export default Header;
