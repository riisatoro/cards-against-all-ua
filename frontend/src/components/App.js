import {
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import { useSelector } from "react-redux";

import MainContent from './MainContent';
import Login from "./Login";
import Registration from "./Registration";
import Profile from "./Profile";
import Navigation from "../constants/navigation";
import { useEffect } from "react";

const ProtectedRoute = ({ children }) => {
  const { accessToken } = useSelector((state) => state.auth);
  if (!accessToken) return <Navigate to={Navigation.login} />
  return children;
}

const App = () => {
  return (
    <div className="container-fluid">
      <Routes>
        <Route path={Navigation.root} element={<MainContent />}>
          <Route path={Navigation.login} element={<Login />} />
          <Route path={Navigation.registration} element={<Registration />} />
          <Route path={Navigation.profile} element={<ProtectedRoute><Profile /></ProtectedRoute>} />
        </Route>
      </Routes>
    </div>
  )
}

export default App;
