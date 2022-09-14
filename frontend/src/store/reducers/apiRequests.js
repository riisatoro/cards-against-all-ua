import axios from 'axios';
import { createAsyncThunk } from '@reduxjs/toolkit';
import {
  LOGIN_URL,
  REGISTRATION_URL,
  USER_DATA_URL,
  GET_OR_CREATE_USER_ROOM,
  USER_LEAVE_ROOM,
  JOIN_USER_ROOM_URL,
} from '../../constants';


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

export const fetchUserRoomData = createAsyncThunk(
  'game/fetchUserRoomData',
  async (payload, { getState }) => {
    const { auth: { accessToken } } = getState();
    const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
    const response = await apiInstance.get(GET_OR_CREATE_USER_ROOM);
    return await response.data;
  }
)

export const createUserRoom = createAsyncThunk(
  'game/joinUserToRoom',
  async (payload, { getState }) => {
    const { auth: { accessToken } } = getState();
    const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
    const response = await apiInstance.post(GET_OR_CREATE_USER_ROOM);
    return await response.data;
  }
)

export const userLeaveRoom = createAsyncThunk(
  'game/userLeaveRoom',
  async (payload, { getState }) => {
    const { auth: { accessToken } } = getState();
    const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
    const response = await apiInstance.post(USER_LEAVE_ROOM, payload);
    return await response.data;
  }
)

export const joinUserRoom = createAsyncThunk(
  'game/joinUserRoom',
  async (payload, { getState }) => {
    const { auth: { accessToken } } = getState();
    const apiInstance = axios.create({ headers: { "Authorization": `Bearer ${accessToken}` } })
    const response = await apiInstance.post(JOIN_USER_ROOM_URL, payload);
    return await response.data;
  }
)