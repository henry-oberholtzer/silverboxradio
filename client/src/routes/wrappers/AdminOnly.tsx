import { Outlet, redirect } from "react-router-dom"
import { useAuth } from "../../hooks"
import { Restricted } from "../../components/Restricted"

const AdminOnly = () => {
  const { user } = useAuth()

  if (!user) {
    return redirect("/auth/login")
  }
  else if (user.is_admin === false) {
    return <Restricted />
  }

  return <Outlet />

}

export { AdminOnly }
