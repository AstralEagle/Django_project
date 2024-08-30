import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Template from "./Template.jsx";
import Index from "./routes/index.jsx";
import Livraison from "./routes/livraison.jsx";
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Menu from "./routes/menu.jsx";
import {Provider} from "react-redux";
import store from "./store/store"
import {SnackbarProvider} from "notistack";
import Commande from "./routes/commande.jsx";



const router = createBrowserRouter([
    {
        path: "/",
        element: <Template />,
        children: [
            {
                path: "/",
                element: <Index />,
            },
            {
                path: "/menu",
                element: <Menu />,
            },
            {
                path: "/livraison",
                element: <Livraison />,
            },
            {
                path: "/commandes",
                element: <Commande />,
            },
        ],
    },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
      <Provider store={store}>
          <SnackbarProvider anchorOrigin={{ vertical: "top", horizontal: "right" }}>
            <RouterProvider router={router} />
          </SnackbarProvider>
      </Provider>
  </StrictMode>,
)
