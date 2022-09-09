import { configureStore } from '@reduxjs/toolkit';

import authReducer from './reducers/authSlice';
import navigationReducer from './reducers/navigationReducer';

const store = configureStore({
    reducer: {
        auth: authReducer,
        navigation: navigationReducer,
    },
});

export default store;
