import axios from 'axios';
import { LOGIN_URL } from '../../constants/api.js';
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

const initialState = {
    accessToken: null,
    refreshToken: null,
};

export const fetchAccessTokens = createAsyncThunk(
    'auth/fetchAccessTokens',
    async (payload) => {
        const response = await axios.post(LOGIN_URL, payload);
        return await response.data;
    }
)


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
