import { createSlice } from '@reduxjs/toolkit';
import { fetchUserRoomData, createUserRoom, joinUserRoom, userLeaveRoom } from './apiRequests';

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
        [createUserRoom.fulfilled]: (state, action) => {
            state.currentGame = action.payload;
        },
        // [createUserRoom.rejected]: (state, action) => { },
        [joinUserRoom.fulfilled]: (state, action) => {
            state.currentGame = action.payload;
        },
        // [joinUserRoom.rejected]: (state, action) => { },
        [userLeaveRoom.fulfilled]: (state, action) => {
            state.currentGame = {};
        }
        // [userLeaveRoom.rejected]: (state, action) => { },
    }
})

export default gameReducer.reducer;
