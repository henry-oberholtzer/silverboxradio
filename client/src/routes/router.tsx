import { Hero, Login, Root } from '.';
import { createBrowserRouter } from 'react-router-dom';
import { AdminRoot, Dashboard } from './admin';
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
        element: <AdminRoot/>,
        children: [
          {
            index: true,
            element: <Dashboard/>
          },
          {
            path: "invite",
            element: <Invite/>,
            loader: api.invites.get,
            action: async ({ request }) => {
              const data = Object.fromEntries(await request.formData())
              return api.invites.post(data)
            },
            children: [
              {
                path: ":inviteId",
                action: async ({ params, request }) => {
                  if (params.inviteId) {
                    switch (request.method) {
                      case "DELETE": {
                        return api.invites.delete(params.inviteId)
                      }
                      default: {
                        throw new Response("No action specified.", { status: 405})
                      }
                    }
                  }
                }
              }
            ]
          },

        ]
      }
    ]
  },
]);

export { router }
