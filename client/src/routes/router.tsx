import { Hero, Login, Root } from '.';
import { createBrowserRouter } from 'react-router-dom';
import { AdminOnly } from './wrappers';
import { Dashboard } from './admin';
import { Invite } from './admin/invite/Invite';
import { api } from '.';

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
      },
      {
        path: "admin",
        element: <AdminOnly/>,
        children: [
          {
            index: true,
            element: <Dashboard/>
          },
          {
            path: "invite",
            element: <Invite/>,
            loader: api.invites.get,
          }
        ]
      }
    ]
  },
]);

export { router }
