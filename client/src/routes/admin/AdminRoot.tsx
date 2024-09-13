import { Container, Tabs } from "@mantine/core"
import { Navigate, Outlet, useNavigate, useParams } from "react-router-dom"
import { useAuth } from "../../hooks"
import { Restricted } from "../../components"

const AdminRoot = () => {
  const navigate = useNavigate()
  const { user } = useAuth()
  const { tabValue } = useParams()

  if (!user) {
    return <Navigate to="auth/login" />
  }
  else if (user.is_admin === false) {
    return <Restricted />
  }

  return (
    <Container>
      <Tabs
        value={tabValue}
        onChange={(value) => value === "dashboard" ? navigate("") : navigate(`${value}`)}>
        <Tabs.List>
          <Tabs.Tab value="dashboard">Dashboard</Tabs.Tab>
          <Tabs.Tab value="invite">Invites</Tabs.Tab>
        </Tabs.List>
      </Tabs>
      <Outlet/>
    </Container>
  )
}

export { AdminRoot }
