import { createContext } from "react"

const AuthContext = createContext<UserContext>({
  user: null,
  login: () => {},
  logout: () => {}
})

export { AuthContext }
