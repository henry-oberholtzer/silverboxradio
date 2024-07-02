import { Outlet } from "react-router-dom"
import { Header } from "../components"

const Root = () => {
  return (
    <>
    <Header></Header>
    <a href="/login">Login</a>
    <Outlet/>
    </>
  )
}

export { Root }
