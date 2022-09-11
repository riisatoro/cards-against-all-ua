import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useLocation } from 'react-router-dom';
import Navigation from '../constants/navigation';
import { fetchUserData } from '../store/reducers/apiRequests';

function Header() {
  const dispatch = useDispatch()
  const { accessToken, username } = useSelector((state) => state.auth);
  const { pathname } = useLocation();

  useEffect(() => {
    if (accessToken) dispatch(fetchUserData());
  }, [accessToken])

  if (!accessToken) {
    return (
      <div className="container-fluid">
        <Link
          to={pathname === Navigation.login ? Navigation.registration : Navigation.login}
          className="btn btn-outline-primary"
        >
          {pathname === Navigation.login ? 'Registration' : 'Login'}
        </Link>
      </div>
    )
  }

  return (
    <div className="container-fluid">
      <p>Welcome, {username}</p>
    </div>
  )
}

export default Header;
