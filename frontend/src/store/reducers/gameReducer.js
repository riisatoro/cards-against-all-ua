import { createSlice } from '@reduxjs/toolkit';
import { fetchAvailableGames } from './apiRequests';

const initialState = {
    currentGame: {},
    availableGames: [],
}

const gameReducer = createSlice({
    name: 'game',
    initialState,
    reducers: { },
    extraReducers: {
        [fetchAvailableGames.fulfilled]: (state, action) => {
            console.log(action.payload);
        },
        // [fetchAvailableGames.rejected]: (state, action) => { },
    }
})

export default gameReducer.reducer;
