import { configureStore } from '@reduxjs/toolkit';
import addressReducer from './adress';

const store = configureStore({
    reducer: {
        address: addressReducer,
    },
});

export default store;
