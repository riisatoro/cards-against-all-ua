import { createSlice } from '@reduxjs/toolkit';
import { fetchUserRoomData, createUserRoom, joinUserRoom, userLeaveRoom } from './apiRequests';

const initialState = {
    roomID: null,
    roomData: {},
}

const gameReducer = createSlice({
    name: 'game',
    initialState,
    reducers: {
        updateGameData: (state, action) => {
            state.roomData = action.payload;
        }
    },
    extraReducers: {
        [fetchUserRoomData.fulfilled]: (state, action) => {
            state.roomID = action.payload.id;
            state.roomData = action.payload;
        },
        // [fetchAvailableGames.rejected]: (state, action) => { },
        [createUserRoom.fulfilled]: (state, action) => {
            state.roomData = action.payload;
        },
        // [createUserRoom.rejected]: (state, action) => { },
        [joinUserRoom.fulfilled]: (state, action) => {
            state.roomID = action.payload.id;
            state.roomData = action.payload;
        },
        // [joinUserRoom.rejected]: (state, action) => { },
        [userLeaveRoom.fulfilled]: (state, action) => {
            state.roomData = {};
            state.roomID = null;
        }
        // [userLeaveRoom.rejected]: (state, action) => { },
    }
})

export const { updateGameData } = gameReducer.actions;

export default gameReducer.reducer;
