import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import WebsocketProvider from './context/websocketContext';

import App from './components/App';
import store from './store';

import './styles/index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Provider store={store}>
        <WebsocketProvider>
          <App />
        </WebsocketProvider>
      </Provider>
    </BrowserRouter>
  </React.StrictMode>
);
