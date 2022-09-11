import axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';
import {
    LOGIN_URL,
    REGISTRATION_URL,
    USER_DATA_URL,
    AVAILABLE_GAMES_URL,
} from '../../constants/api';

export const fetchAccessTokens = createAsyncThunk(
    'auth/fetchAccessTokens',
    async (payload) => {
        const response = await axios.post(LOGIN_URL, payload);
        return await response.data;
    }
);

export const createAccount = createAsyncThunk(
    'auth/fetchAccessTokens',
    async (payload) => {
        const response = await axios.post(REGISTRATION_URL, payload);
        return await response.data;
    }
)

export const fetchUserData = createAsyncThunk(
    'auth/fetchUserData',
    async (payload, { getState }) => {
        const { auth: { accessToken } } = getState();
        const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
        const response = await apiInstance.get(USER_DATA_URL);
        return await response.data;
    }
)

export const fetchAvailableGames = createAsyncThunk(
    'game/fetchAvailableGames',
    async (payload, { getState }) => {
        const { auth: { accessToken } } = getState();
        const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
        const response = await apiInstance.get(AVAILABLE_GAMES_URL);
        return await response.data;
    }
)