import { createSlice } from '@reduxjs/toolkit';
import { fetchAccessTokens } from './apiRequests';

const initialState = {
    accessToken: null,
    refreshToken: null,
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
        [fetchAccessTokens.pending]: (state, action) => { },
        [fetchAccessTokens.fulfilled]: (state, action) => {
            state.accessToken = action.payload.access;
            state.refreshToken = action.payload.refresh;
        },
        [fetchAccessTokens.rejected]: (state, action) => { },
    }
});

export const { register, login, logout, refresh } = authSlice.actions;


export default authSlice.reducer;
