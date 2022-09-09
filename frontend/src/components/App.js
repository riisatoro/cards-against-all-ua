import { useSelector, useDispatch } from 'react-redux';
import { setLocation } from '../store/reducers/navigationReducer';
import Navigation from '../constants/navigation';
import Header from './Header';

function App() {
  const dispatch = useDispatch();
  const { accessToken } = useSelector((state) => state.auth);
  const { location } = useSelector((state) => state.navigation);

  if (!accessToken && ![Navigation.login.name, Navigation.registration.name].includes(location)) {
    dispatch(setLocation({ location: Navigation.login.name }));
  }

  return (
    <>
      <Header />
      {Navigation[location]?.component()}
    </>
  )
}

export default App;
