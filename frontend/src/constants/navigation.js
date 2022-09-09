import Login from '../components/Login'

const Navigation = {
    login: {
        name: 'login',
        component: Login,
    },
    registration: {
        name: 'registration',
        component: () => {},
    },
    availableRooms: {
        name: 'availableRooms',
        component: () => {},
    },
}

export default Navigation;
