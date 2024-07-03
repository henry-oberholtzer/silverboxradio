import { useState } from "react"
import { useCookies } from "react-cookie"
import { PasswordInput, TextInput, Button, Container, Paper, Alert} from "@mantine/core"
import { IconInfoCircle } from '@tabler/icons-react'
import { useAuth } from "../../hooks"

const Login = () => {
  const [username, setUsername] = useState<string>('')

  const [password, setPassword] = useState<string>('')
  const [errors, setError] =  useState<string>()
  const [,setCookie] = useCookies()
  const { login } = useAuth()

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
            response.json().then(data => login(data))
          }
          if (response.status === 401) {
            setError("Incorrect username or password.")
            resetForm()
          }

        }).then()
      } catch (error) {
        console.error(error)
      }
    }

  }

  const icon = <IconInfoCircle/>

  return (
    <Container size={420} my={40}>
      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <form onSubmit={handleFormSubmit}>
          <TextInput
            label="Username"
            value={username}
            required 
            onChange={(e) => setUsername(e.target.value)}
          />
          <PasswordInput
            mt="md"
            label="Password"
            value={password}
            required 
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button type="submit" fullWidth mt="xl">Login</Button>
        </form>
      </Paper>
      {errors && (
      <Alert variant="light" color="red" title={errors} icon={icon}  mt={30} withCloseButton closeButtonLabel="Dismiss" onClose={() => setError("")}/>
      )}
    </Container>
  )
}

export { Login }
