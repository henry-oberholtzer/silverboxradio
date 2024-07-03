import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  RouterProvider
} from "react-router-dom"
import { router } from './routes'
import { CookiesProvider } from 'react-cookie'
import { MantineProvider } from '@mantine/core'
import { AuthProvider } from './hooks/useAuth'
import '@mantine/core/styles.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <CookiesProvider defaultSetOptions={{ path: '/'}}>
      <AuthProvider>
        <MantineProvider>
          <RouterProvider router={router} />
        </MantineProvider>
      </AuthProvider>
    </CookiesProvider>
  </React.StrictMode>
)
