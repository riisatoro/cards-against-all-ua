import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { Link, useLocation } from 'react-router-dom';
import Navigation from '../constants/navigation';

function Header() {
  const { accessToken } = useSelector((state) => state.auth);
  const { pathname } = useLocation();
  const username = 'Anon';

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
