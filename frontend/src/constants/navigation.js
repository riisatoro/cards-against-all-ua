import Login from '../components/Login';
import Profile from '../components/Profile';
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
    profile: {
        name: 'profile',
        component: Profile,
    },
}

export default Navigation;
