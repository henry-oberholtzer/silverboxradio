import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  RouterProvider
} from "react-router-dom"
import { router } from './routes'
import { CookiesProvider } from 'react-cookie'
import { GlobalStyle, CustomThemeProvider } from './components'
import { AuthProvider } from './hooks/useAuth'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <CookiesProvider defaultSetOptions={{ path: '/'}}>
      <AuthProvider>
        <CustomThemeProvider>
          <GlobalStyle/>
          <RouterProvider router={router} />
        </CustomThemeProvider>
      </AuthProvider>
    </CookiesProvider>
  </React.StrictMode>
)
