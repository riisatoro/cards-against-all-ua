import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    accessToken: null,
    refreshToken: null,
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        register: (state, action) => { },
        login: (state, action) => { 
            state.accessToken = action.payload.accessToken;
            state.refreshToken = action.payload.refreshToken;
        },
        logout: (state, action) => { },
        refresh: (state, action) => { },
    }
});
export const { register, login, logout, refresh } = authSlice.actions;


export default authSlice.reducer;
