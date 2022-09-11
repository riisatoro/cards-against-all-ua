import { createSlice } from '@reduxjs/toolkit';
import { fetchAccessTokens, fetchUserData } from './apiRequests';

const initialState = {
    accessToken: null,
    refreshToken: null,
    username: '',
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        deleteTokens: (state, action) => {
            state.accessToken = null;
            state.refreshToken = null;
         },
    },
    extraReducers: {
        [fetchAccessTokens.fulfilled]: (state, action) => {
            state.accessToken = action.payload.access;
            state.refreshToken = action.payload.refresh;
        },
        // [fetchAccessTokens.rejected]: (state, action) => { },

        [fetchUserData.fulfilled]: (state, action) => {
            state.username = action.payload.username;
        },
        [fetchUserData.rejected]: (state, action) => { },
    }
});

export const { register, login, logout, refresh } = authSlice.actions;


export default authSlice.reducer;
