import { Hero, Login, Root } from '.';
import { createBrowserRouter } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      {
        index: true,
        element: <Hero />
      },
      {
        path: "login",
        element: <Login/>,
      }
    ]
  },
]);

export { router }
