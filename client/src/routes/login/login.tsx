import { useState } from "react"
import { useCookies  } from "react-cookie"

const Login = () => {
  const [username, setUsername] = useState<string>('')

  const [password, setPassword] = useState<string>('')
  const [errors, setError] =  useState<string>()
  const [,setCookie] = useCookies()

  const resetForm = () => {
    setPassword("")
    setUsername("")
  }

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (username && password) {
      const body: UserLoginSchema = {
        username: username,
        password: password
      }
      try {
        await fetch("http://localhost:5000/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
          },
          body: JSON.stringify(body)
        }).then(response => {
          if (response.ok) {
            const accessToken = response.headers.get('access_token_cookie')
            const refreshToken = response.headers.get('refresh_token_cookie')
            accessToken ?
            setCookie('access_token_cookie', accessToken) : ""
            refreshToken ?
            setCookie('refresh_token_cookie', refreshToken) : ""
            const data = response.json()
            console.log(data)
          }
          if (response.status === 401) {
            setError("Incorrect username or password.")
            resetForm()
          }

        })
      } catch (error) {
        console.error(error)
      }
    }

  }

  return (
    <>
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
      {errors && (
        <p>{errors}</p>
      )}
    </>
  )
}

export { Login }
