import axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';
import { LOGIN_URL, REGISTRATION_URL } from '../../constants/api';

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