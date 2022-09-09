import Login from '../components/Login';
import Registration from '../components/Registration';

const Navigation = {
    login: {
        name: 'login',
        component: Login,
    },
    registration: {
        name: 'registration',
        component: Registration,
    },
    availableRooms: {
        name: 'availableRooms',
        component: () => {},
    },
}

export default Navigation;
