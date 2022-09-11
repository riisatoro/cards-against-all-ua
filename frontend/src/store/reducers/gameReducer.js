import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    currentGame: {},
    availableGames: [],
}

const gameRedicer = createSlice({
    name: 'game',
    initialState,
    reducers: { },
    extraReducers: {
        []: (state, action) => {
            
        }
    }
})