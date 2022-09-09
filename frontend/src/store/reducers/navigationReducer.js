import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    location: null,
}

const navigationSlice = createSlice({
    name: 'navigation',
    initialState,
    reducers: {
        setLocation: (state, action) => {
            state.location = action.payload.location;
        },
    }
})


export const { setLocation } = navigationSlice.actions;
export default navigationSlice.reducer;
