import { Navigate, Outlet } from "react-router-dom"
import { useAuth } from "../../hooks"
import { useGlobalNotification } from "../../hooks"

const AuthRequired = () => {
  const { user } = useAuth()
  const { set } = useGlobalNotification()

  if (user) {
    set({
      sentiment: "neutral",
      message: "Please log in to access this page."
    })
    return <Navigate to="/auth/login"/>
  }
  return <Outlet />
}

export { AuthRequired }
