import { createContext } from "react"

const AuthContext = createContext<UserContext>({
  user: null,
  message: null,
  login: () => 200,
  logout: () => 200,
  dismissMessage: () => {},
})

export { AuthContext }
