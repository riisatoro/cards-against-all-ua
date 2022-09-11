import { configureStore } from '@reduxjs/toolkit';

import authReducer from './reducers/authSlice';
import gameReducer from './reducers/gameReducer';

const store = configureStore({
    reducer: {
        auth: authReducer,
        game: gameReducer,
    },
});

export default store;
