import { Outlet } from "react-router-dom"
import { Header, Footer } from "../components"
import { AppShell } from "@mantine/core"

const Root = () => {
  return (
    <AppShell
      header={{ height: 56 }}
    >
      <AppShell.Header>
        <Header />
      </AppShell.Header>
      <AppShell.Navbar>

      </AppShell.Navbar>
      <AppShell.Main>
        <Outlet/>
      </AppShell.Main>
      <AppShell.Footer>
        <Footer />
      </AppShell.Footer>
    </AppShell>
  )
}

export { Root }
