import { useState } from "react"
import { api } from ".."

const Login = () => {
  const [username, setUsername] = useState<string>('')

  const [password, setPassword] = useState<string>('')

  const handleFormSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (username && password) {
      const body: UserLoginSchema = {
        username: username,
        password: password
      }
      const response = api.login(body)
      console.log(response)
    }

  }

  return (
    <form onSubmit={handleFormSubmit}>
      <label htmlFor="username">Username</label>
      <input 
        type="text"
        name="username"
        value={username} 
        onChange={(e) => setUsername(e.target.value)}
      ></input>
      <label htmlFor="password">Password</label>
      <input 
        type="password" 
        name="password"
        value={password} 
        onChange={(e) => setPassword(e.target.value)}
      ></input>
      <button type="submit">Login</button>
    </form>
  )
}

export { Login }
