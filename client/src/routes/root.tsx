import { Outlet } from "react-router-dom"
import { GlobalBannerNotification, Header } from "../components"
import { AppShell } from "@mantine/core"

const Root = () => {
  return (
    <AppShell
      withBorder={false}
      header={{ height: 90 }}
    >
      <AppShell.Header>
        <Header />
        <GlobalBannerNotification/>
      </AppShell.Header>
      <AppShell.Navbar>

      </AppShell.Navbar>
      <AppShell.Main>
        <Outlet/>
      </AppShell.Main>
      {/* <AppShell.Footer>
        <Footer />
      </AppShell.Footer> */}
    </AppShell>
  )
}

export { Root }
