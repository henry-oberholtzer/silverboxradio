import { Container, Tabs } from "@mantine/core"
import { Navigate, Outlet } from "react-router-dom"
import { useAuth } from "../../hooks"
import { Restricted } from "../../components"

const AdminRoot = () => {
  const { user } = useAuth()

  if (!user) {
    return <Navigate to="/login" />
  }
  else if (user.is_admin === false) {
    return <Restricted />
  }

  return (
    <Container>
      <Tabs>
        <Tabs.List>
          <Tabs.Tab value="dashboard">Dashboard</Tabs.Tab>
          <Tabs.Tab value="invites">Invites</Tabs.Tab>
        </Tabs.List>
      </Tabs>
      <Outlet/>
    </Container>
  )
}

export { AdminRoot }
