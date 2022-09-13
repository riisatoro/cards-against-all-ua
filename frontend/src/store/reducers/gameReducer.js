import { createSlice } from '@reduxjs/toolkit';
import { fetchUserRoomData, joinUserToRoom, userLeaveRoom } from './apiRequests';

const initialState = {
    currentGame: {},
}

const gameReducer = createSlice({
    name: 'game',
    initialState,
    reducers: { },
    extraReducers: {
        [fetchUserRoomData.fulfilled]: (state, action) => {
            state.currentGame = action.payload;
        },
        // [fetchAvailableGames.rejected]: (state, action) => { },
        [joinUserToRoom.fulfilled]: (state, action) => {
            state.currentGame = action.payload;
        },
        // [joinUserToRoom.rejected]: (state, action) => { },
        [userLeaveRoom.fulfilled]: (state, action) => {
            state.currentGame = {};
        }
        // [userLeaveRoom.rejected]: (state, action) => { },
    }
})

export default gameReducer.reducer;
