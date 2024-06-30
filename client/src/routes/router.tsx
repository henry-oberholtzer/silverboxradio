import { Login, Root } from '.';
import { createBrowserRouter } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      {
        path: "login",
        element: <Login/>
      }
    ]
  },
]);

export { router }
