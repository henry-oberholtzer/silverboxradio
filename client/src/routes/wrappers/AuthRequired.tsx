import { Navigate, Outlet } from "react-router-dom"
import { useAuth } from "../../hooks"

const AuthRequired = () => {
  const { user } = useAuth()

  if (user) {
    return <Navigate to="/login" />
  }
  return <Outlet />
}

export { AuthRequired }
