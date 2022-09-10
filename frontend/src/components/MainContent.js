import { Outlet } from "react-router-dom";
import Header from './Header';

const MainContent = () => {
    return (
        <div className="container-fluid">
            <Header />
            <Outlet />
        </div>
    )
}

export default MainContent;
