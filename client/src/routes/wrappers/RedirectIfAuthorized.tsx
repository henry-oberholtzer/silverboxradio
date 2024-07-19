import { Navigate, Outlet } from "react-router-dom"
import { useAuth } from "../../hooks"

const RedirectIfAuthorized = (props: RedirectProps) => {
  const { user } = useAuth()

  if (user) {
    return <Navigate to={props.to ? props.to : `/users/${user.username}` }/>
  }
  return <Outlet />
}

export { RedirectIfAuthorized }
